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
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-3.3B")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-3.3B")
        self.model.to("cuda")
        self.model.eval()

    # Chunks based on text length, cutting off context if necessary
    # Technically breaks on weird text that has a token:text ratio > 1
    def harsh_chunk(self, text):
        chunks = []

        for x in range(math.ceil(len(text) / max_context_len)):
            begin = x * max_context_len
            chunk = text[begin:begin + max_context_len]
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

            inputs = self.tokenizer(input_text, return_tensors="pt").to("cuda")
            output_ids = self.model.generate(**inputs, max_new_tokens=max_context_len)
            output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

            out_tensor = pb_utils.Tensor("text_output", np.array([output_text.encode("utf-8")]))
            responses.append(pb_utils.InferenceResponse(output_tensors=[out_tensor]))

        return responses


if __name__ == "__main__":
        text= "The Intel 8080 is Intel's second 8-bit microprocessor. Introduced in April 1974, the 8080 was an enhanced successor to the earlier Intel 8008 microprocessor, although without binary compatibility.[3] Originally intended for use in embedded systems such as calculators, cash registers, computer terminals, and industrial robots,[4] its robust performance soon led to adoption in a broader range of systems, ultimately helping to launch the microcomputer industry. Several key design choices contributed to the 8080’s success. Its 40‑pin package simplified interfacing compared to the 8008’s 18‑pin design, enabling a more efficient data bus. The transition to NMOS technology provided faster transistor speeds than the 8008's PMOS while also simplifying interfacing by making it TTL compatible. An expanded instruction set and a full 16-bit address bus allowed the 8080 to access up to 64 KB of memory, quadrupling the capacity of its predecessor. A broader selection of support chips further enhanced its functionality. Many of these improvements stemmed from customer feedback, as designer Federico Faggin and others at Intel heard about shortcomings in the 8008 architecture. The 8080 found its way into early personal computers such as the Altair 8800 and subsequent S-100 bus systems, and it served as the original target CPU for the CP/M operating systems. It also directly influenced the later x86 architecture which was designed so that its assembly language closely resembled that of the 8080, permitting many instructions to map directly from one to the other.[5] Originally operating at a clock rate of 2 MHz, with common instructions taking between 4 and 11 clock cycles, the 8080 was capable of executing several hundred thousand instructions per second. Later, two faster variants, the 8080A-1 and 8080A-2, offered improved clock speeds of 3.125 MHz and 2.63 MHz, respectively.[6] In most applications, the processor was paired with two support chips, the 8224 clock generator/driver and the 8228 bus controller, to manage its timing and data flow. "
        print(chunk(text))