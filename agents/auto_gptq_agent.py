import argparse
from pathlib import Path
import os
from utils import init_os_envs

init_os_envs("huggingface", set_proxy=False)
from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig


class AutoGPTQAgent:
    def __init__(self, model_name=None, streaming=True):
        self.model_name = "TheBloke/Nous-Hermes-13B-GPTQ"
        self.model_basename = "nous-hermes-13b-GPTQ-4bit-128g.no-act.order"

    def load_model(self, model_name=None):
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            use_fast=True,
        )
        self.model = AutoGPTQForCausalLM.from_quantized(
            model_name_or_path=self.model_name,
            model_basename=self.model_basename,
            use_safetensors=True,
            trust_remote_code=True,
            device="cuda:0",
            use_triton=False,
            quantize_config=None,
        )

    def run(self):
        self.load_model()

        print("\n\n*** Generate:")

        prompt = "Tell me about AI"
        prompt_template = f"""### Human: {prompt}
        ### Assistant:"""

        input_ids = self.tokenizer(
            prompt_template,
            return_tensors="pt",
        ).input_ids.cuda()
        output = self.model.generate(
            inputs=input_ids,
            temperature=0.7,
            max_new_tokens=512,
        )
        print(self.tokenizer.decode(output[0]))

        # Inference can also be done using transformers' pipeline

        # Prevent printing spurious transformers error when using pipeline with AutoGPTQ
        # logging.set_verbosity(logging.CRITICAL)

        # print("*** Pipeline:")
        # pipe = pipeline(
        #     task="text-generation",
        #     model=self.model,
        #     tokenizer=self.tokenizer,
        #     max_new_tokens=512,
        #     temperature=0.7,
        #     top_p=0.95,
        #     repetition_penalty=1.15,
        # )

        # print(pipe(prompt_template)[0]["generated_text"])
