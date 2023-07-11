from agents.chimera_agent import ChimeraAgent

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

chimera_agent = ChimeraAgent()
chimera_agent.run()
