import os
from gpt4all import GPT4All
from utils import init_os_envs

init_os_envs()


class OrcaMini3BAgent:
    def __init__(self):
        pass

    def run(self):
        model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
        # output = model.generate("The capital of France is ", max_tokens=3)
        # print(output)
        output = model.generate(
            "Provide me a plan and necessary components for creating a World Simulator"
        )
        print(output)
