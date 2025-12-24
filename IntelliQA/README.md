# IntelliQA

> **Ask any document. Get grounded answers.**
> A Retrieval Augmented Generation (RAG) system that turns your PDFs, Word docs, HTML files, and more into a private, conversational knowledge base.

---

## ⚡ TL;DR

* **What it does**: Upload documents in dozens of formats, ask questions in plain English, get answers grounded in your sources.
* **Why it's interesting**: Production oriented design with content deduplication, session aware chat, and a persistent vector store.
* **What powers it**: Llama 3.3 70B served on Groq for low latency inference, with HuggingFace embeddings and a local ChromaDB vector store.
* **Where it runs**: Containerized with Docker, deployed on AWS EC2.
* **Status**: Working end to end. Formal RAG evaluation (faithfulness, answer relevance, context precision) is in progress.

---

## 🛠️ Tech Stack

### Language & Runtime
<p align="left">
  <img src="https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

### RAG Framework
<p align="left">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logoColor=white"/>
</p>

### LLM & Embeddings
<p align="left">
  <img src="https://img.shields.io/badge/Llama_3.3_70B_Versatile-0467DF?style=for-the-badge&logo=meta&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq_LPU_Inference-F55036?style=for-the-badge&logoColor=white"/>
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
  <img src="https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?style=for-the-badge&logoColor=white"/>
</p>

### Document Processing
<p align="left">
  <img src="https://img.shields.io/badge/Apache_Tika-D22128?style=for-the-badge&logo=apache&logoColor=white"/>
</p>

### Infrastructure
<p align="left">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"/>
</p>

---

## 🏗️ Architecture

![IntelliQA RAG Flow](./RAG%20Flow.png)

IntelliQA follows a clean two phase RAG design.

### 1. Ingestion (run once per document set)

1. **Upload** documents in any supported format.
2. **Parse** with Apache Tika to extract clean text (PDF, DOCX, HTML, TXT, RTF, ODT, and more).
3. **Deduplicate** so already indexed content is detected and skipped.
4. **Chunk** the text into overlapping segments to preserve meaning across boundaries.
5. **Embed** each chunk into a 384 dimensional vector using `sentence-transformers/all-MiniLM-L6-v2`.
6. **Index** vectors into ChromaDB, persisted locally in `chroma_db/`.

### 2. Query (runs per question)

1. **Embed** the user question with the same embedding model used during ingestion.
2. **Retrieve** the top K nearest chunks from Chroma using cosine similarity.
3. **Assemble** a prompt combining the question, retrieved context, and session history.
4. **Generate** the answer with Llama 3.3 70B (via Groq) at `temperature=0` for deterministic, grounded output.
5. **Return** the answer while preserving session state for follow up questions.

---

## ✨ Key Features

* 🗂️ **Multi format ingestion** via Apache Tika: PDF, DOCX, HTML, TXT, RTF, ODT, and dozens more
* 🔁 **Smart deduplication** to keep the vector store clean and retrieval precise
* 💬 **Session aware Q&A** so follow up questions like "what about the next point?" resolve correctly
* 🎯 **Grounded answers only** with `temperature=0` to minimize hallucination
* ⚡ **Fast inference** via Groq's LPU based serving of Llama 3.3 70B
* 🆓 **Open weight model** with no LLM vendor lock in
* 📦 **Reusable package** with core RAG logic in `rag_pipeline/`, decoupled from the demo notebook
* 🐳 **Containerized** for reproducible local and cloud runs
* ☁️ **Deployed on AWS EC2**

---

## 📁 Project Structure

```
IntelliQA/
├── IntelliQA.ipynb         # Main notebook: end-to-end RAG demo
├── rag_pipeline/           # Core RAG package
│   ├── __init__.py
│   ├── query_engine.py     # Query embedding, retrieval, answer generation
│   ├── vector_store.py     # Chroma vector store setup and indexing
│   └── utils.py            # Document parsing, chunking, deduplication
├── chroma_db/              # Persisted Chroma vector store
├── RAG Flow.png            # Architecture diagram
├── dockerfile              # Container definition
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation config
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* A [Groq API key](https://console.groq.com/keys)
* Docker (optional, for containerized runs)

### Run Locally

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Set up environment
python -m venv venv
source venv/bin/activate            # On Windows: venv\Scripts\activate

# Install dependencies and the rag_pipeline package
pip install -r requirements.txt
pip install -e .

# Set the Groq API key
export GROQ_API_KEY="your-key-here"

# Launch the notebook
jupyter notebook IntelliQA.ipynb
```

### Run with Docker

```bash
docker build -t intelliqa -f dockerfile .

docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

---

## 🧠 Design Decisions

The choices a hiring manager is most likely to ask about.

| Decision | Why |
|----------|-----|
| **Groq + Llama 3.3 70B** | Sub-second inference via LPU serving, with open weight flexibility and no vendor lock in on the LLM |
| **`temperature=0`** | Deterministic, repeatable answers, which is critical for document Q&A where the same question should return the same response |
| **all-MiniLM-L6-v2 embeddings** | 384 dimensional vectors, fast on CPU, no API cost, strong quality for general semantic search |
| **ChromaDB (persisted locally)** | Simple to operate, no separate infrastructure to manage, supports metadata filtering and persistence out of the box |
| **Apache Tika for parsing** | Single extraction layer across dozens of formats, no need to maintain format specific parsers |
| **Deduplication at ingestion** | Prevents the vector store from being polluted with repeated content, which would skew similarity scores |
| **Reusable `rag_pipeline` package** | Core logic decoupled from the notebook, so it can be imported into a future API or web app without rewrites |

---

## 🗺️ Roadmap

* [ ] **Evaluation pipeline** (in progress): faithfulness, answer relevance, and context precision via RAGAS or a custom eval set
* [ ] **Reranking step** with a cross encoder to improve top K precision
* [ ] **Inline citations** linking each answer sentence back to its source chunk
* [ ] **Hybrid search**: combine BM25 keyword retrieval with vector search for better recall on exact term queries
* [ ] **Streaming responses** for faster perceived latency
* [ ] **Web UI**: replace the notebook entry point with a Streamlit or FastAPI app
* [ ] **Authentication and per user document isolation**

---

## 🔗 Related Projects

IntelliQA is part of my broader Generative AI portfolio. See the parent [GenAI repository](https://github.com/abhijitdeshpande83/GenAI) for other projects covering agentic workflows, fine tuning, and multi agent systems.

---