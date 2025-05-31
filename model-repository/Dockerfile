# Dockerfile
FROM nvcr.io/nvidia/tritonserver:25.04-py3

RUN pip install transformers torch sentencepiece spacy
RUN rm -rf /usr/local/lib/python3.12/dist-packages/numpy-1.26.4.dist-info/
RUN pip install numpy==1.26.4
RUN python3 -m spacy download xx_sent_ud_sm
