import asyncio
import json
import logging
import os
import shutil
import sys
from pathlib import Path

# python -m pip install --upgrade openai
import openai

# python -m pip install git+https://github.com/dsdanielpark/Bard-API.git
import bardapi
from bardapi import Bard

# python -m pip install poe-api
import poe

# poe.logger.setLevel(logging.INFO)

# python -m pip install EdgeGPT --upgrade
# from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.EdgeUtils import Query, Cookie


def init_os_envs():
    with open(Path(__file__).parent / "secrets.json", "r") as rf:
        secrets = json.load(rf)

    for proxy_env in ["http_proxy", "https_proxy"]:
        os.environ[proxy_env] = secrets["http_proxy"]

    os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]
    os.environ["BARD_API_KEY"] = secrets["bard_api_key"]
    os.environ["CLAUDE_API_KEY"] = secrets["claude_api_key"]


init_os_envs()
openai.api_key = os.environ["OPENAI_API_KEY"]


class ChatGPTAgent:
    """
    * openai-cookbook: How to format inputs to ChatGPT models
      * https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
    """

    def __init__(
        self,
        original_text,
        model="gpt-3.5-turbo",
        task="en2zh",
    ):
        task_system_message_dict = {
            "en2zh": "你是一个英译中翻译专家。你的任务是将给定的英文如实翻译成中文。",
        }
        self.model = model
        self.system_message = task_system_message_dict[task]
        self.original_text = original_text

    def run(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": self.system_message + self.original_text,
                },
            ],
            temperature=0,
        )

        self.translated_text = response["choices"][0]["message"]["content"]
        return self.translated_text


class BardAgent:
    def __init__(self):
        pass

    def run(self):
        question = "Today's Weather of Shanghai Minhang. For temperature, you should Celsius Degree instead of Fahrenheit. You should output the statistics in table format."
        # answer = Bard().get_answer(question)["content"]
        # print(answer)
        bard_session = bardapi.core.Bard(token=os.environ["BARD_API_KEY"])
        response = bard_session.get_answer(question)
        answer = response["content"]
        print(answer)


class ClaudeAgent:
    def __init__(self, model="Claude-instant"):
        self.poe_model_name_map = {
            "Sage": "capybara",
            "Claude-instant": "a2",
            "Claude-instant-100k": "a2_100k",
            "Claude+": "a2_2",
            "ChatGPT": "chinchilla",
            "GPT-4": "beaver",
        }
        self.poe_model_id_map = {v: k for k, v in self.poe_model_name_map.items()}

        self.model = model
        self.model_id = self.poe_model_name_map[model]
        # print(f"> Poe LLM Model: {self.model}")
        self.claude_client = poe.Client(
            token=os.environ["CLAUDE_API_KEY"],
            proxy=os.environ["http_proxy"],
        )

    def prompt(self, message):
        for chunk in self.claude_client.send_message(
            self.model_id,
            message,
            with_chat_break=True,
        ):
            print(chunk["text_new"], end="", flush=True)
        print()

    def get_history(self, count=5):
        history = self.claude_client.get_message_history(
            self.model_id,
            count=count,
        )
        for message in history:
            author = message["node"]["author"]
            text = message["node"]["text"]
            if author == "chat_break":
                print("-" * shutil.get_terminal_size()[0])
            else:
                if author != "human":
                    author = self.poe_model_id_map[author]
                print(f"[{author}]:" f"{text}")
        print()

    def run(self):
        # self.get_history()
        self.prompt("Introduce yourself in less than 10 words.")
        self.prompt("Repeat my last question.")


class BingAgent:
    def __init__(self):
        pass

    def run(self):
        cookie_file = Path(__file__).parent / "bing_cookies_main.json"
        q = Query(
            "Hello world",
            style="precise",
            proxy=os.environ["http_proxy"],
            cookie_file=cookie_file,
        )
        print(q.output)


if __name__ == "__main__":
    translater = ChatGPTAgent(
        "Evaluation of GPT-3.5 and GPT-4 for supporting real-world information needs in healthcare delivery"
    )
    translater.run()
    print(translater.translated_text)
