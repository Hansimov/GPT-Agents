from agents.chimera_agent import ChimeraAgent
from managers.chat_message_manager import ChatMessageManager

# from agents import (
#     LangchainAgent,
#     BardAgent,
#     ClaudeAgent,
#     ChatGPTAgent,
#     BingAgent,
#     GPT4AllAgent,
#     AutoGPTQAgent,
#     ChimeraAgent,
# )

# original_text = "Hello World"
# chatgpt_agent = ChatGPTAgent(original_text)
# print(f"> Translating characters num: {len(original_text)}")
# chatgpt_agent.run()
# print(chatgpt_agent.translated_text)

# bard_agent = BardAgent()
# bard_agent.run()

# claude_agent = ClaudeAgent("Sage")
# claude_agent = ClaudeAgent("Claude-instant")
# claude_agent.run()

# bing_agent = BingAgent()
# bing_agent.run()

# langchain_agent = LangchainAgent()
# langchain_agent.run()

# orca_mini_13b_agent = GPT4AllAgent(model_name="orca-mini-3b.ggmlv3.q4_0.bin")
# nous_hermes_13b_agent = GPT4AllAgent(model_name="nous-hermes-13b.ggmlv3.q4_0.bin")
# nous_hermes_13b_agent.chat(
#     prompts=[
#         "Provide me a 5-step plan and necessary components for creating a World Simulator",
#         "For last step, provide more details",
#         "Criticize the details for last step, then provide three suggestions on how to improve it",
#         "How many rounds of the chats in above conversation?",
#     ]
# )

# auto_gptq_agent = AutoGPTQAgent()
# auto_gptq_agent.run()

criticizer_agent = ChimeraAgent(
    name="Criticizer",
    system_message="你的名字叫 `Criticizer`。你是一个喜欢批评的人。对于前一个的观点，你总是加以怀疑和反驳，并举出反例。",
)
summarizer_agent = ChimeraAgent(
    name="Summarizer",
    system_message="你的名字叫 `Summarizer`。你是一个擅长总结的人。对于所有人的聊天，你总是给出简短的总结。",
)
questioner_agent = ChimeraAgent(
    name="Questioner",
    system_message="你的名字叫 `Questioner`。你是一个善于提问的人。对于前一个人的观点，你总是提出三个与之相关的问题。",
)
answerer_agent = ChimeraAgent(
    name="Answerer",
    system_message="你的名字叫 `Answerer`。你是一个善于回答的人。对于前一个人的问题，你总是给出三个与之相关的答案。",
)
supporter_agent = ChimeraAgent(
    name="Supporter",
    system_message="你的名字叫 `Supporter`。你是一个乐于倾听的人。对于前一个人的观点，你总是给出支持，并且会给出支持的理由。",
)
imaginer_agent = ChimeraAgent(
    name="Imaginer",
    system_message="你的名字叫 `Imaginer`。你是一个热爱想象的人。对于前一个人的话，你总是给出一个想象的场景。",
    temperature=0,
)

statist_agent = ChimeraAgent(
    name="Statist",
    system_message="你的名字叫 `Statist`。你是一个擅长统计的人，请你给出上面每个人各发言了几次，并以该格式输出：```<角色>:<发言次数>```",
)

chat_message_manager = ChatMessageManager()
chat_message_manager.add_agents(
    [
        imaginer_agent,
        questioner_agent,
        answerer_agent,
        criticizer_agent,
        supporter_agent,
        summarizer_agent,
        statist_agent,
    ]
)
chat_message_manager.sequential_chat("我如何才能成为百万富翁？", rounds=2)
