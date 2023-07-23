# GPT-Agents

Multiple GPT Agents to have brainstorms and make decisions

## Architecture

![GPT-Agents Architecture](./examples/gpt-agents.png)

## Examples

```py
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
```

![Agents Sequential Chats](./examples/agents-sequential-chats.png)


## Todos

No longer develop the UI part, as I move it to another repo: [GPT-WebUI](https://github.com/Hansimov/GPT-WebUI).

- [ ] [UI] A group chat UI
  - [ ] multiple styles for different agents and messages


- [ ] [CLI] Command line args to specify agents or api
- [ ] Fork or new chat branch
  - [ ] Chat history replay
- [ ] Session history
- [ ] User commands in chat input area
  - [ ] `/help` - list commands and usage
  - [ ] `/list agents` - list agents
  - [ ] `/list chats` - list chat history
  - [ ] `/list chats @<agent>` - list chat history
  - [ ] `/create` - create agent with random name and random prompt
  - [ ] `/create @<name>` - create agent with name
  - [ ] `/create :<prompt>` - create agent with initial prompt
  - [ ] `/create @<name> :<prompt>` - create agent with name and initial prompt
  - [ ] `/set @<agent> :<prompt>` - set `agent` with `prompt`
  - [ ] `/set @<agent>` - set `agent` with random prompt
  - [ ] `/inject` - inject random memory and prompt to all agents
  - [ ] `/inject @<agent> :<prompt>` - inject `prompt` to `agent`
  - [ ] `/inject @<agent> #<memory>` - inject `memory` to `agent`
  - [ ] `/reset` - reset the memory and chat history of all agents
  - [ ] `/reset @<agent>` - reset the memory and chat history of `agent`
  - [ ] `/reset memory` - reset memory of all agents
  - [ ] `/reset memory @<agent>` - reset the memory of `agent`
  - [ ] `/reset prompt` - reset the prompt of all agents
  - [ ] `/reset prompt @<agent>` - reset the prompt of `agent`
  - [ ] `/reset chat` - reset the chat history of all agents
  - [ ] `/reset chat @<agent>` - reset the chat history of `agent`
  - [ ] `/remove` - remove all agents
  - [ ] `/remove @<agent>` - remove `agent`
  - [ ] `/undo` - undo last command
  - [ ] `/redo` - redo last command
  - [ ] `/call @<agent>` - call `agent` with `prompt`
  - [ ] `/call @<agent> :<prompt>` - call `agent` with `prompt`
- [ ] Multiple types of agent engine
  - [ ] Traditional NLP
  - [ ] Python / Mathematica
  - [ ] Web Searcher
  - [ ] Other LLMs


## Setup

Create python venv:

```bash
python -m venv llm
./llm/Scripts/activate # Windows
source ./llm/bin/activate # Linux
```

Install packages:

```bash
python -m pip install --upgrade --force-reinstall -r requirements.txt
```


## References
* ading2210/poe-api: A reverse engineered Python API wrapper for Quora's Poe, which provides free access to ChatGPT, GPT-4, and Claude.
  * https://github.com/ading2210/poe-api

* dsdanielpark/Bard-API: The unofficial python package that returns response of Google Bard through cookie value.
  * https://github.com/dsdanielpark/Bard-API

* acheong08/EdgeGPT: Reverse engineered API of Microsoft's Bing Chat AI
  * https://github.com/acheong08/EdgeGPT