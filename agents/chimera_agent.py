import requests
from requests.adapters import HTTPAdapter, Retry
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
        name,  # name of the agent, also use "role" as alias
        model="gpt-3.5-turbo-16k",
        temperature=0,
        system_message=None,
    ):
        self.name = name
        self.chat_api = f"{self.api}/v1/chat/completions"
        self.requests_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['CHIMERA_API_KEY']}",
        }
        self.model = model
        self.temperature = temperature
        self.system_message = system_message

    def content_to_message(self, role, content):
        return {"role": role, "content": content}

    def construct_request_messages_with_prompt(self, prompt):
        request_messages = []
        if self.system_message:
            request_messages.append(
                self.content_to_message("system", self.system_message)
            )
        request_messages.append(self.content_to_message("user", prompt))
        return request_messages

    def chat(
        self,
        # model,
        # temperature,
        messages,
        history_messages=None,
        stream=False,
        top_p=1,
        n=1,
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
            "temperature": self.temperature,
            "stream": stream,
        }
        requests_session = requests.session()

        retires = Retry(total=3, backoff_factor=0.1)
        requests_session.mount("https://", HTTPAdapter(max_retries=retires))

        response = requests_session.post(
            self.chat_api,
            headers=self.requests_headers,
            json=self.requests_payload,
        )
        response_data = response.json()
        # print(f'{[self.name]}: {response_data["choices"][0]["message"]["content"]}')
        return response_data

    def get_available_models(self):
        """
        ## Available models
        * https://chimeragpt.adventblocks.cc/v1/models

        ```py
        [
            'gpt-4', 'gpt-4-32k', 'gpt-4-0613',
            'gpt-3.5-turbo', 'gpt-3.5-turbo-openai', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-16k-openai',
            'gpt-4-poe', 'gpt-3.5-turbo-poe', 'sage',
            'claude-instant', 'claude+', 'claude-instant-100k', 'chat-bison-001',
        ]
        ```
        """
        self.models_api = f"{self.api}/v1/models"
        response = requests.get(self.models_api)
        data = response.json()["data"]
        self.available_models = []

        for item in data:
            if "/v1/chat/completions" in item["endpoints"]:
                self.available_models.append(item["id"])
        print(self.available_models)

    def test_prompt(self):
        self.system_message = (
            f"你是一个专业的中英双语专家。如果给出中文，你需要如实翻译成英文；如果给出中文，你需要如实翻译成英文。"
            f"你的翻译应当是严谨的和自然的，不要删改原文。请按照要求翻译如下文本："
        )
        prompt = "In this paper, we introduce Semantic-SAM, a universal image segmentation model to enable segment and recognize anything at any desired granularity."
        messages = self.construct_request_messages_with_prompt(prompt)
        model = "gpt-3.5-turbo"
        print(messages)
        self.chat(messages, model)

    def run(self):
        # self.get_available_models()
        # self.test_prompt()
        pass
