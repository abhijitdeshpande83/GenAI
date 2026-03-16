# TaskPilot 🚀

**TaskPilot** is a autonomous agent built with **LangGraph**, designed for real-time web research and stateful conversations.

---

## 💡 The Idea
The goal is to provide a lightweight, modular agent that leverages the inference speed of **Groq LLM** and the precision of **Tavily Search**. It uses ephemeral memory to maintain context during a session without the need for a heavy external database.

## 🛠️ Tech Stack
* **Orchestration:** [LangGraph](https://github.com/langchain-ai/langgraph)
* **Inference:** [Groq LLM](https://groq.com/)
* **Search:** [Tavily API](https://tavily.com/)
* **State:** `MemorySaver` (Checkpointing)

## ⚡ Quick Start

### 1. Setup
```bash
# Clone the entire GenAI repo
git clone https://github.com/abhijitdeshpande83/GenAI.git

# Navigate to the project
cd GenAI/TaskPilot
pip install -r requirements.txt