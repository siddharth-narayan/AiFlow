from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.models.auto.modeling_auto import AutoModelForSeq2SeqLM
import triton_python_backend_utils as pb_utils
import numpy as np
import spacy
import math

nlp = spacy.load("xx_sent_ud_sm")


class TritonPythonModel:
    max_context_len = 512
    def initialize(self, args):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
        self.model.to("cuda")
        self.model.eval()

    # Chunks based on text length, cutting off context if necessary
    # Technically breaks on weird text that has a token:text ratio > 1
    def harsh_chunk(self, text):
        chunks = []

        for x in range(math.ceil(len(text) / self.max_context_len)):
            begin = x * self.max_context_len
            chunk = text[begin:begin + self.max_context_len]
            chunks.append(chunk)

        return chunks

    def chunk(self, text):
        doc = nlp(text)

        # Chunk along sentences, remove empty sentences
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

        chunks = []
        max_chunk = ""

        for sentence in sentences:
            if self.count_tokens(sentence) > self.max_context_len:
                chunks.extend(self.harsh_chunk(sentence))

            elif self.count_tokens(max_chunk + sentence) > self.max_context_len:
                chunks.append(max_chunk)
            else:
                max_chunk += sentence

        chunks.append(max_chunk)

        return chunks

    def count_tokens(self, text):
        return len(self.tokenizer(text).input_ids)

    def execute(self, requests):
        responses = []

        for request in requests:
            input_tensor = pb_utils.get_input_tensor_by_name(request, "text_input")
            input_text = input_tensor.as_numpy()[0].decode("utf-8")
            
            lang = "Spanish"
            output_text = self.large_translate(input_text, lang)
            out_tensor = pb_utils.Tensor("text_output", np.array([output_text.encode("utf-8")]))
            responses.append(pb_utils.InferenceResponse(output_tensors=[out_tensor]))
        return responses
    
    def large_translate(self, text, lang):
        chunks = self.chunk(text)
        print(chunks)
        translated_chunks = []
        for chunk in chunks:
            translated_chunks.append(self.translate(chunk, lang).strip())

        return " ".join(translated_chunks)


    def translate(self, text, lang):
        text = f"translate to {lang}: {text}"
        print(text)
        inputs = self.tokenizer(text, return_tensors="pt").to("cuda")
        output_ids = self.model.generate(**inputs, max_new_tokens=self.max_context_len)
        output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        print(output_text)
        return output_text