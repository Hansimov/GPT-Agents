#%%
from faker import Faker
from langchain.llms.fake import FakeListLLM
from langchain.agents import load_tools, initialize_agent, AgentType
import itertools
import shutil


def generate_fake_actions():
    faker = Faker(["zh_CN"])["zh_CN"]
    # faker = Faker()
    for i in range(30):
        action_str = faker.name()
        answer_str = faker.job()
        yield [
            f"Action: Python REPL\nAction Input: get_job_of('{action_str}')",
            f"Final Answer: {answer_str}",
        ]


responses = list(itertools.chain(*list(generate_fake_actions())))
# print(responses)

llm = FakeListLLM(responses=responses)
tools = load_tools(["python_repl"])
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

for i in range(15):
    print("-" * shutil.get_terminal_size()[0])
    print(f"Action {i}")
    agent.run("New Action")
