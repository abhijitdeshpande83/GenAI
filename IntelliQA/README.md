<h1 align="center">🤖 IntelliQA</h1>

<p align="center">
  <b>Ask any document. Get grounded answers.</b><br/>
  <sub>A production-oriented Retrieval-Augmented Generation (RAG) system that turns your PDFs, Word docs, HTML files, and more into a private, conversational knowledge base.</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Inference-Groq_LPU-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/Deployment-AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white" alt="AWS EC2"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
</p>

---

## 📖 Overview

Large Language Models (LLMs) are incredibly powerful, but they lack access to your private, domain-specific documents and are prone to hallucinations when operating outside their training data. 

**IntelliQA solves both challenges.** By combining semantic search with local vector persistence, it retrieves the most contextually relevant chunks from your document library and passes them to a high-performance open-weight LLM as strict, grounded context. Operating at a deterministic `temperature=0`, the model answers *only* from verified retrieved data, creating an enterprise-grade QA engine you can trust.

> [!NOTE]
> **Production-Ready Packaging:** The core RAG logic is decoupled from developer notebooks, fully modularized within the `rag_pipeline` Python package, and compiled as a **prebuilt wheel** for instantaneous distribution and enterprise integration.

---

## ✨ Key Features

<table align="center">
<tr>
<td align="center" width="33%" valign="top">
  <h3>🗂️</h3>
  <h4><b>Multi-Format Ingestion</b></h4>
  <p>Parse <code>PDF</code>, <code>DOCX</code>, <code>HTML</code>, <code>TXT</code>, <code>RTF</code>, and <code>ODT</code> out-of-the-box via a unified, robust extraction layer.</p>
  <sub><i>Powered by Apache Tika</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>🔁</h3>
  <h4><b>Smart Deduplication</b></h4>
  <p>Detects and bypasses previously indexed content automatically, preserving vector space and keeping retrieval precise.</p>
  <sub><i>Custom dedup pipeline</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>💬</h3>
  <h4><b>Session-Aware Q&A</b></h4>
  <p>Tracks and maintains conversational state seamlessly so complex, multi-turn follow-up questions resolve correctly.</p>
  <sub><i>LangChain Memory Window</i></sub>
</td>
</tr>
<tr>
<td align="center" width="33%" valign="top">
  <h3>🎯</h3>
  <h4><b>Grounded Context</b></h4>
  <p>Enforces deterministic model generation to eliminate hallucinations, guaranteeing responses strictly trace back to source text.</p>
  <sub><i>Zero-variance inference</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>⚡</h3>
  <h4><b>Sub-Second Inference</b></h4>
  <p>Blazing-fast generation speeds delivered by Groq's LPU hardware architecture running <b>Llama 3.3 70B Versatile</b>.</p>
  <sub><i>Groq + Meta Llama</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>📦</h3>
  <h4><b>Pip-Installable Wheel</b></h4>
  <p>Core pipeline logic is compiled into a standalone asset in <code>dist/</code> for drop-in use across upstream applications.</p>
  <sub><i>rag_pipeline v3.0</i></sub>
</td>
</tr>
<tr>
<td align="center" width="33%" valign="top">
  <h3>🐳</h3>
  <h4><b>Containerized Runtime</b></h4>
  <p>Fully Dockerized environment configuration guarantees predictable, isolated runs across local dev environments and clouds.</p>
  <sub><i>Docker Engine</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>☁️</h3>
  <h4><b>Cloud Architecture</b></h4>
  <p>Engineered for production deployment on scalable cloud compute infrastructure, validating real-world scalability.</p>
  <sub><i>AWS EC2 Hosting</i></sub>
</td>
<td align="center" width="33%" valign="top">
  <h3>🆓</h3>
  <h4><b>Open-Weight Stack</b></h4>
  <p>Complete infrastructural independence. Built entirely on open-weight models and transparent core libraries.</p>
  <sub><i>Meta Llama + HuggingFace</i></sub>
</td>
</tr>
</table>

---

## 🏗️ Architecture & Pipeline Flow

<p align="center">
  <img src="./RAG%20Flow.png" alt="IntelliQA RAG Flow"/>
</p>

IntelliQA follows a clean two phase RAG design.

<details open>
<summary><b>📥 Phase 1: Ingestion</b> (run once per document set)</summary>

1. **Upload** documents in any supported format.
2. **Parse** with Apache Tika to extract clean text.
3. **Deduplicate** already indexed content.
4. **Chunk** the text into overlapping segments.
5. **Embed** each chunk into a 384 dimensional vector using `all-MiniLM-L6-v2`.
6. **Index** vectors into ChromaDB, persisted in `chroma_db/`.

</details>

<details open>
<summary><b>🔎 Phase 2: Query</b> (runs per question)</summary>

1. **Embed** the user question with the same embedding model.
2. **Retrieve** the top K nearest chunks via cosine similarity.
3. **Assemble** a prompt combining the question, retrieved context, and session history.
4. **Generate** the answer with Llama 3.3 70B at `temperature=0`.
5. **Return** the response while preserving session state for follow ups.

</details>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|:------|:-----------|:--------|
| **Language** | ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white) | Core implementation |
| **Notebook** | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) | Interactive demo and development |
| **RAG Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) | Ingestion and retrieval orchestration |
| **Vector Store** | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logoColor=white) | Persistent similarity search |
| **LLM** | ![Llama](https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white) | Answer generation |
| **LLM Serving** | ![Groq](https://img.shields.io/badge/Groq_LPU-F55036?style=flat-square&logoColor=white) | Low latency inference |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/all--MiniLM--L6--v2-FFD21E?style=flat-square&logo=huggingface&logoColor=black) | 384 dim semantic vectors |
| **Document Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache_Tika-D22128?style=flat-square&logo=apache&logoColor=white) | Unified multi format extraction |
| **Packaging** | ![Wheel](https://img.shields.io/badge/setup.py_%2B_wheel-3776AB?style=flat-square&logo=pypi&logoColor=white) | Distributable Python package |
| **Containerization** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | Reproducible runtime |
| **Deployment** | ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) | Cloud hosting |

---

## 📁 Project Structure

```
IntelliQA/
├── 📓 IntelliQA.ipynb                          # Main notebook: end-to-end RAG demo
├── 📦 rag_pipeline/                            # Core RAG package source
│   ├── __init__.py
│   ├── query_engine.py                         # Query embedding, retrieval, generation
│   ├── vector_store.py                         # Chroma vector store setup and indexing
│   └── utils.py                                # Parsing, chunking, deduplication helpers
├── 📂 dist/
│   └── rag_pipeline-3.0-py3-none-any.whl       # Prebuilt installable package
├── 🗃️  chroma_db/                              # Persisted Chroma vector store
├── 🖼️  RAG Flow.png                            # Architecture diagram
├── 🐳 dockerfile                               # Container definition
├── 📜 requirements.txt                         # Python dependencies
├── ⚙️  setup.py                                # Package build configuration
└── 📘 README.md
```

---

## 🚀 Installation & Usage

> 🎯 Three paths, each for a different goal. Pick what fits your use case.

<br/>

### ⚡ Option 1: Install the Prebuilt Wheel <sub><i>(fastest, recommended)</i></sub>

Install the `rag_pipeline` package directly from the prebuilt wheel shipped in `dist/`. Cleanest path if you want to use IntelliQA as a library in your own code.

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Install the prebuilt wheel
pip install dist/rag_pipeline-3.0-py3-none-any.whl

# Set your Groq API key
export GROQ_API_KEY="your-key-here"
```

Use it anywhere in your code:

```python
from rag_pipeline import vector_store, query_engine, utils

# See IntelliQA.ipynb for full usage examples
```

<br/>

### 🛠️ Option 2: Install from Source <sub><i>(for development)</i></sub>

Use this path if you want to modify the RAG logic, contribute, or run the demo notebook end to end.

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate              # Windows: venv\Scripts\activate

# Install dependencies and the package in editable mode
pip install -r requirements.txt
pip install -e .

# Set your Groq API key
export GROQ_API_KEY="your-key-here"

# Launch the notebook
jupyter notebook IntelliQA.ipynb
```

<br/>

### 🐳 Option 3: Run with Docker <sub><i>(fully isolated)</i></sub>

Use this path for a fully isolated, reproducible runtime.

```bash
# Build the image
docker build -t intelliqa -f dockerfile .

# Run the container
docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

The container exposes Jupyter on port `8888`. Open the printed URL in your browser to interact with `IntelliQA.ipynb`.

---

## 🧠 Design Decisions

> The choices a hiring manager or senior engineer is most likely to ask about.

| 🔑 Decision | 💡 Rationale |
|:--|:--|
| **Groq + Llama 3.3 70B** | Sub second inference via LPU serving, with open weight flexibility and no LLM vendor lock in |
| **`temperature=0`** | Deterministic, repeatable answers, which is critical for document Q&A where the same question should return the same response |
| **`all-MiniLM-L6-v2` embeddings** | 384 dimensional vectors, fast on CPU, no API cost, strong quality for general semantic search |
| **ChromaDB (local persistence)** | Simple to operate, no separate infrastructure to manage, supports metadata filtering and persistence out of the box |
| **Apache Tika for parsing** | One extraction layer across dozens of formats, eliminating format specific parser maintenance |
| **Deduplication at ingestion** | Prevents the vector store from being polluted with repeated content, which would skew similarity scores |
| **Reusable `rag_pipeline` package** | Core logic decoupled from the notebook and shipped as a wheel, so it can be imported into a future API or web app without rewrites |

---
