from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.models.auto.modeling_auto import AutoModelForSeq2SeqLM
import numpy as np
import spacy
import math

nlp = spacy.load("xx_sent_ud_sm")
max_context_len = 512
print("aa")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

print("aa")
# Chunks based on text length, cutting off context if necessary
# Technically breaks on weird text that has a token:text ratio > 1
def harsh_chunk(text):
    chunks = []

    for x in range(math.ceil(len(text) / max_context_len)):
        begin = x * max_context_len
        chunk = text[begin:begin + max_context_len]
        chunks.append(chunk)

    return chunks

def chunk_nlp(text):
    doc = nlp(text)

    # Chunk along sentences, remove empty sentences
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    chunks = []
    max_chunk = ""

    for sentence in sentences:
        if count_tokens(sentence) > max_context_len:
            chunks.extend(harsh_chunk(sentence))

        elif count_tokens(max_chunk + sentence) > max_context_len:
            chunks.append(max_chunk)
        else:
            max_chunk += sentence

    chunks.append(max_chunk)

    return chunks

def count_tokens(text):
    return len(tokenizer(text).input_ids)


def large_translate(text, lang):
    chunks = chunk_nlp(text)
    print(chunks)
    translated_chunks = []
    for chunk in chunks:
        translated_chunks.append(translate(chunk, lang).strip())

    return " ".join(translated_chunks)


def translate(text, lang):
    text = f"translate to {lang}: {text}"
    print(text)
    inputs = tokenizer(text, return_tensors="pt")
    output_ids = model.generate(**inputs, max_new_tokens=max_context_len)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(output_text)
    return output_text

print("agagag")
print(large_translate("GNMT improved on the quality of translation by applying an example-based (EBMT) machine translation method in which the system learns from millions of examples of language translation.[2] GNMT's proposed architecture of system learning was first tested on over a hundred languages supported by Google Translate.[2] With the large end-to-end framework, the system learns over time to create better, more natural translations.[1] GNMT attempts to translate whole sentences at a time, rather than just piece by piece.[1] The GNMT network can undertake interlingual machine translation by encoding the semantics of the sentence, rather than by memorizing phrase-to-phrase translations.", "Spanish"))
print("agfag")