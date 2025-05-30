# Multi-Agent with Multi-Clients Demo

This project demonstrates a simple multi-agent system using multiple LLM (Large Language Model) clients in Python.

## Files

- **agent.py**: Defines agent logic and behavior.
- **llmclients.py**: Manages connections and interactions with different LLM clients.

## How It Works

1. **Agents** are created using classes/functions from `agent.py`.
2. Each agent can be assigned a different LLM client from `llmclients.py`.
3. Agents interact with each other, each leveraging their respective LLM client for generating responses or actions.
4. The demo showcases communication, task delegation, or collaboration between agents using multiple LLM backends.

## Usage

```bash
agent=Agent(model="gemini-2.0-flash", client=GeminiClient())
agent1=agent.call_with_retry(instruction,context)
```

This will initialize agents, assign LLM clients, and start the demonstration.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Customization

- Add or modify agents in `agent.py`.
- Integrate new LLM clients in `llmclients.py`.

