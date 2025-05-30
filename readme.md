# 🧠 Multi-Agent LLM System

A lightweight multi-agent system in Python that demonstrates collaboration among agents, each powered by a different Large Language Model (LLM) client. This project showcases how multiple AI agents can interact, delegate tasks, and generate insights through inter-agent communication.

---

## 🚀 Features

- 🧩 Modular agent architecture
- 🔁 Multi-agent communication and collaboration
- 🤖 Integration with multiple LLM clients (e.g., OpenAI, Claude, Gemini)
- 📦 Easily extendable for additional agents or tasks

---

## 📂 Project Structure

```
multi-agent-app/
|- agent.py # Defines Agent class and its behavior
|- llmclients.py # Abstractions for connecting to various LLMs
|- main.py # Orchestrates agent creation and execution
|- README.md
```

---

## ⚙️ How It Works

Each agent is initialized with a specific LLM client (like GPT-4, Claude, Gemini). These agents can be given individual tasks or work collaboratively on a problem by exchanging responses and augmenting each other’s outputs.

### Example Workflow:
1. Create multiple agents using different LLM APIs.
2. Assign a shared goal or problem.
3. Let agents respond, reference each other’s answers, and refine outputs in a loop.

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tripathiaman2511/multi-agent-app.git
   cd multi-agent-app
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Add API Keys**
   ```env
   OPENAI_API_KEY=your_openai_key
   CLAUDE_API_KEY=your_claude_key
   GEMINI_API_KEY=your_gemini_key
   ```
4. **Run the application**
   ```bash
   python main.py
   ```

---

## 🔧 Customization

You can easily add more agents or LLMs by modifying:

1. llmclients.py: Add new client wrappers
2. main.py: Instantiate additional agents with different roles
3. agent.py: Add memory, tool use, or agent capabilities

---

## 📌 Use Cases
1. 🧠 AI task orchestration and brainstorming
2. 📊 Collaborative summarization or report generation
3. 🛠️ Auto-documentation or code review bots
4. 🕵️ Competitive analysis from multiple LLMs



