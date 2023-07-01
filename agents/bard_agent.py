import os
import shutil
from termcolor import colored
from utils import init_os_envs

# python -m pip install git+https://github.com/dsdanielpark/Bard-API.git
import bardapi
from bardapi import Bard


init_os_envs()


class BardAgent:
    def __init__(
        self,
        prompts=[
            "Today's Weather of Shanghai Minhang. For temperature, you should Celsius Degree instead of Fahrenheit.",
            "You should output the above statistics in a format which is friendly readable in terminal output.",
        ],
    ):
        self.prompts = prompts
        self.bard_session = bardapi.core.Bard(token=os.environ["BARD_API_KEY"])

    def run(self):
        for prompt in self.prompts:
            print(f"[Human]: {colored(prompt,'green')}")
            response = self.bard_session.get_answer(prompt)
            answer = response["content"]
            print(f"[Bard]: {colored(answer,'cyan')}")
            print("-" * shutil.get_terminal_size()[0])
