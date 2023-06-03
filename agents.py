from utils import ChatGPTAgent

original_text = "Hello World"
chatgpt_agent = ChatGPTAgent(original_text)
print(f"> Translating characters num: {len(original_text)}")
chatgpt_agent.run()
print(chatgpt_agent.translated_text)
