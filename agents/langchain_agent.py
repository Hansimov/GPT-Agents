from utils import init_os_envs
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

init_os_envs()


class LangchainAgent:
    def __init__(self):
        pass

    def run(self):
        llm = OpenAI(
            model_name="text-davinci-002",
        )
        res = llm.predict(
            "Tell me the latest president of the United States of America. Your answer should be as short as possible."
        )
        print(res)
