from agents.chimera_agent import ChimeraAgent
from managers.chat_message_manager import ChatMessageManager
from utils import Runtimer

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


def test_sequential_chat():
    criticizer_agent = ChimeraAgent(
        name="Criticizer",
        system_message="你的名字叫 `Criticizer`。你是一个喜欢批评的人。请你对前一个人的观点，尽可能加以怀疑和反驳，并举出反例。",
    )
    summarizer_agent = ChimeraAgent(
        name="Summarizer",
        system_message="你的名字叫 `Summarizer`。你是一个擅长总结的人。请你尽可能给出所有人对话内容的简短总结。",
    )
    questioner_agent = ChimeraAgent(
        name="Questioner",
        system_message="你的名字叫 `Questioner`。你是一个善于提问的人。请你对前一个人的观点，尽可能提出三个与之相关的问题。",
    )
    answerer_agent = ChimeraAgent(
        name="Answerer",
        system_message="你的名字叫 `Answerer`。你是一个喜欢回答的人。请你对前一个人的每个问题，尽可能给出与之相关的答案。",
    )
    supporter_agent = ChimeraAgent(
        name="Supporter",
        system_message="你的名字叫 `Supporter`。你是一个乐于倾听的人。请你对前一个人的观点，给予支持，并且给出支持的理由。",
    )
    imaginer_agent = ChimeraAgent(
        name="Imaginer",
        system_message="你的名字叫 `Imaginer`。你是一个热爱想象的人。请你对前一个人的话，给出一个充满想象的场景。",
        temperature=0,
    )

    statist_agent = ChimeraAgent(
        name="Statist",
        system_message="你的名字叫 `Statist`。请你统计上面每个人分别发言了几次。输出格式：<角色>:<发言次数>",
        model="gpt-4-32k-poe",
    )

    chat_message_manager = ChatMessageManager()
    chat_message_manager.add_agents(
        [
            # imaginer_agent,
            questioner_agent,
            answerer_agent,
            criticizer_agent,
            # supporter_agent,
            summarizer_agent,
        ]
    )
    chat_message_manager.sequential_chat(init_content="我如何才能成为百万富翁？", rounds=1)
    chat_message_manager.add_agents(statist_agent)
    chat_message_manager.sequential_chat(rounds=1)


def test_stream_chat(stream=False):
    chimera_agent = ChimeraAgent(name="TestStream", model="gpt-3.5-turbo")
    chimera_agent.test_prompt(stream=stream)


def test_get_available_models():
    chimera_agent = ChimeraAgent(name="TestStream")
    chimera_agent.get_available_models()


def test_who_is_spy():
    alice_agent = ChimeraAgent(
        name="Alice",
        system_message="你的名字是 `Alice`。你的单词令牌是“牛肉干”。你的目标是尽可能确认自己的队友，然后找出间谍。你喜欢在描述中增加细节。现在，请你用一句话描述你的单词。注意，你的描述不能和已经说过的重复，否则你也会立刻出局。",
    )
    bob_agent = ChimeraAgent(
        name="Bob",
        system_message="你的名字是 `Bob`。你的单词令牌是“牛肉干”。你的目标是尽可能确认自己的队友，然后找出间谍。你喜欢稍微修改别人的描述。现在，请你用一句话描述你的单词。注意，你的描述不能和已经说过的重复，否则你也会立刻出局。",
    )
    charlie_agent = ChimeraAgent(
        name="Charlie",
        system_message="你的名字是 `Charlie`。你的单词令牌是“牛肉干”。你的目标是尽可能确认自己的队友，然后找出间谍。你喜欢在描述中减少细节。现在，请你用一句话描述你的单词。注意，你的描述不能和已经说过的重复，否则你也会立刻出局。",
    )
    diana_agent = ChimeraAgent(
        name="Diana",
        system_message="你的名字是 `Diana`。你是全场唯一的卧底。你的单词令牌是“猪肉脯”。你的目标是尽可能隐藏自己的身份，一旦被发现，你就会被销毁。你会尽可能整合前面所有人的描述。现在，请你用一句话描述你的单词。注意，你的描述不能和已经说过的重复，否则你也会立刻出局。",
    )
    manager_system_message = "你正在和几个人一起玩一个名为“谁是卧底”的游戏。游戏规则是：所有人都会拿到一个单词令牌，除了卧底的令牌不同以外，其他人的令牌都是相同的。卧底单独一队，其他人同为一队。每人每次只能说一句话描述自己拿到的单词令牌，但不能直接说出该单词，否则就会立刻出局。"
    chat_message_manager = ChatMessageManager(
        manager_system_message=manager_system_message,
    )
    chat_message_manager.add_agents(
        [
            alice_agent,
            bob_agent,
            diana_agent,
            charlie_agent,
        ]
    )
    chat_message_manager.sequential_chat(rounds=3)


if __name__ == "__main__":
    with Runtimer():
        # print("Run!")
        test_get_available_models()
        # test_sequential_chat()
        # test_who_is_spy()
        # test_stream_chat(stream=False)
        # test_stream_chat(stream=True)
