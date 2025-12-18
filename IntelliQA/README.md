# 🚀 IntelliQA

> **Ask any document. Get grounded, citation-ready answers.**  
> A production-grade **Retrieval Augmented Generation (RAG)** system that transforms PDFs, Word files, HTML, and more into a **private, conversational knowledge base**.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=for-the-badge&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Apache_Tika-D22128?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white" />
</p>

---

## ⚡ Why IntelliQA

Turn static documents into a **living, searchable intelligence layer**.

- 📄 Ask questions in natural language  
- 🧠 Get answers grounded in your documents  
- 🚫 Reduced hallucinations via strict context grounding  
- 📚 Works across dozens of file formats  
- ☁️ Runs locally or on cloud infrastructure  

> Built for **production-style RAG reliability**, not toy demos.

---

## 🧠 What Makes It Different

IntelliQA is designed like a real-world AI system, not just a notebook experiment:

- 🔍 Deduplicated ingestion pipeline (clean vector store)
- 🧵 Session-aware multi-turn conversation memory
- 📦 Modular `rag_pipeline/` architecture
- ⚡ Low-latency inference via Groq (Llama 3.3 70B)
- 🎯 Deterministic outputs (`temperature = 0`)
- ☁️ Docker + AWS EC2 deployable system

---

## 🏗️ Architecture

![IntelliQA RAG Flow](./RAG%20Flow.png)

### 🔹 1. Ingestion Pipeline

Documents → Clean text → Chunking → Embeddings → Vector DB

- Parse documents using **Apache Tika**
- Deduplicate content before indexing
- Chunk with overlap for semantic continuity
- Embed using `all-MiniLM-L6-v2`
- Store in **ChromaDB (persistent vector store)**

---

### 🔹 2. Query Pipeline

Question → Retrieval → Context → LLM → Answer

- Embed user query
- Retrieve top-K relevant chunks via similarity search
- Build context-aware prompt with session history
- Generate response using **Llama 3.3 70B (Groq)**
- Return grounded answer with minimal hallucination risk

---

## ✨ Key Features

- 📄 Multi-format ingestion (PDF, DOCX, HTML, TXT, RTF, ODT, etc.)
- 🔁 Smart deduplication to prevent vector noise
- 💬 Multi-turn conversational memory
- 🎯 Grounded responses with strict context usage
- ⚡ Sub-second inference via Groq LPU
- 🧠 Open-weight LLM approach (no vendor lock-in)
- 📦 Modular, reusable RAG pipeline package
- 🐳 Dockerized for reproducibility
- ☁️ AWS EC2 deployment ready

---

## 🧱 Tech Stack

- **Language:** Python, Jupyter  
- **RAG Framework:** LangChain, ChromaDB  
- **LLM:** Llama 3.3 70B (Groq)  
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2`  
- **Parsing:** Apache Tika  
- **Infrastructure:** Docker, AWS EC2  

---

## 🚀 Quick Start

### 📦 Local Setup

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
pip install -e .

export GROQ_API_KEY="your-key"

jupyter notebook IntelliQA.ipynb