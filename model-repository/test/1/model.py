from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.models.auto.modeling_auto import AutoModelForSeq2SeqLM
import triton_python_backend_utils as pb_utils
import numpy as np

class TritonPythonModel:
    def initialize(self, args):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
        self.model.to("cuda")
        self.model.eval()

    def execute(self, requests):
        responses = []

        for request in requests:
            input_tensor = pb_utils.get_input_tensor_by_name(request, "text_input")
            input_text = input_tensor.as_numpy()[0].decode("utf-8")

            inputs = self.tokenizer(input_text, return_tensors="pt").to("cuda")
            output_ids = self.model.generate(**inputs, max_new_tokens=512)
            output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

            out_tensor = pb_utils.Tensor("text_output", np.array([output_text.encode("utf-8")]))
            responses.append(pb_utils.InferenceResponse(output_tensors=[out_tensor]))

        return responses

