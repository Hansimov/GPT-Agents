import requests
import os
from utils import init_os_envs

init_os_envs("chimera")


class ChimeraAgent:
    """
    OpenAI API doc:
      * https://platform.openai.com/docs/api-reference/chat/create
    Chimera FastAPI doc:
      * https://chimeragpt.adventblocks.cc/docs#/
    """

    api = "https://chimeragpt.adventblocks.cc"

    def __init__(
        self,
        prompt=None,
        system_message=None,
        model="gpt-3.5-turbo",
    ):
        self.chat_api = f"{self.api}/v1/chat/completions"
        self.requests_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['CHIMERA_API_KEY']}",
        }
        self.model = model
        self.system_message = system_message

    def content_to_message(self, role, content):
        return {"role": role, "content": content}

    def construct_messages(self, prompt):
        messages = []
        if self.system_message:
            messages.append(self.content_to_message("system", self.system_message))
        messages.append(self.content_to_message("user", prompt))
        return messages

    def chat(
        self,
        messages,
        model,
        temperature=0,
        top_p=1,
        n=1,
        stream=False,
        stop=None,
        max_tokens=8096,
        functions=None,
        function_call=None,
        presence_penalty=0,
        frequency_penalty=0,
        logit_bias=None,
        user=None,
    ):
        """
        ## Request:
        ```sh
        curl -X 'POST' \
            'https://chimeragpt.adventblocks.cc/v1/chat/completions' \
            -H 'accept: application/json' \
            -H 'Authorization: Bearer <YOUR_CHIMERA_KEY>' \
            -H 'Content-Type: application/json' \
            -d '{
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "Say this is a test!"}],
                "temperature": 0
            }'
        ```
        ## Response
        ```json
        {
            "id": "chatcmpl-W0zJUER1GNIcrN3mLRp00fy6Tb8GO",
            "object": "chat.completion",
            "created": 1689055727,
            "model": "gpt-3.5-turbo",
            "choices": [
                {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "This is a test!"
                },
                "finish_reason": "stop"
                }
            ],
            "usage": {
                "completion_tokens": 5,
                "prompt_tokens": 14,
                "total_tokens": 19
            }
        }
        ```
        """
        self.requests_payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }
        response = requests.post(
            self.chat_api,
            headers=self.requests_headers,
            data=self.requests_payload,
        )
        return response.json()

    def test_prompt(self):
        self.system_message = (
            f"你是一个专业的中英双语专家。如果给出中文，你需要如实翻译成英文；如果给出中文，你需要如实翻译成英文。"
            f"你的翻译应当是严谨的和自然的，不要删改原文。请按照要求翻译如下文本："
        )
        prompt = "In this paper, we introduce Semantic-SAM, a universal image segmentation model to enable segment and recognize anything at any desired granularity."
        messages = self.construct_messages(prompt)
        model = "gpt-3.5-turbo"
        self.chat(messages, model)
