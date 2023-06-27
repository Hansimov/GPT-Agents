#%%
from faker import Faker
from langchain.llms.fake import FakeListLLM
from langchain.agents import load_tools, initialize_agent, AgentType


tools = load_tools(["python_repl"])


def generate_fake_emojis():
    faker = Faker()
    for i in range(10):
        yield faker.emoji()


fake_emojis = list(generate_fake_emojis())


def generate_fake_jobs():
    faker = Faker()
    for i in range(10):
        yield faker.job()


fake_jobs = list(generate_fake_jobs())


def generate_fake_responses():
    responses = []
    for i in range(10):
        action_str = fake_jobs[i]
        answer_str = fake_emojis[i]
        responses.extend(
            [
                f"Action: Python REPL\nAction Input: print('{action_str}')",
                f"Final Answer: {answer_str}",
            ]
        )
    return responses


responses = generate_fake_responses()
print(responses)

llm = FakeListLLM(responses=responses)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


for i in range(10):
    agent.run("New Action")
