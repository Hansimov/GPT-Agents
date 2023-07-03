# from utils import ChatGPTAgent, BardAgent, ClaudeAgent, BingAgent, LangchainAgent
from agents import (
    LangchainAgent,
    BardAgent,
    ClaudeAgent,
    ChatGPTAgent,
    BingAgent,
    OrcaMini3BAgent,
)

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

orca_mini_13b_agent = OrcaMini3BAgent()
orca_mini_13b_agent.run()
