# python -m pip install --upgrade openai
import openai
from utils import init_os_envs

init_os_envs("openai")


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
            "en2zh": "你是一个英译中翻译专家。你的任务是将给定的英文如实翻译成中文。\n",
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
