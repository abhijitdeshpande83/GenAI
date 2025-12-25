<h1 align="center">IntelliQA</h1>

<p align="center">
  <b>Ask any document. Get grounded answers.</b><br/>
  A production oriented Retrieval Augmented Generation (RAG) system that turns your PDFs, Word docs, HTML files, and more into a private, conversational knowledge base.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Build-rag__pipeline_v3.0-blue?style=flat-square" alt="Build"/>
  <img src="https://img.shields.io/badge/Status-Stable-success?style=flat-square" alt="Status"/>
</p>

---

## 📖 Overview

Large language models are powerful but they do not know your private documents and they hallucinate on topics outside their training data. **IntelliQA solves both** by retrieving the most relevant chunks from your uploaded documents and passing them to the LLM as grounded context. The model answers only from what was retrieved, making the system reliable for enterprise document Q&A.

Core RAG logic is packaged in the `rag_pipeline` Python package and shipped as a prebuilt wheel, so you can install it with a single `pip install` and start asking questions.

---

## ✨ Key Features

<table>
<tr>
<td width="50%" valign="top">

### 🗂️ Multi Format Ingestion
Parse **PDF, DOCX, HTML, TXT, RTF, ODT** and dozens more formats through a single Apache Tika extraction layer. No format specific parsers to maintain.

</td>
<td width="50%" valign="top">

### 🔁 Smart Deduplication
Detects and skips already indexed documents and repeated chunks, keeping the vector store clean and retrieval precise across re ingestions.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💬 Session Aware Q&A
Maintains conversation state per session so follow up questions like *"what about the next point?"* resolve correctly against earlier turns.

</td>
<td width="50%" valign="top">

### 🎯 Grounded Answers
LLM runs at `temperature=0` and answers only from retrieved context, drastically reducing hallucination and keeping responses traceable to sources.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ⚡ Fast Inference
Powered by **Groq's LPU based serving** of Llama 3.3 70B, delivering sub second response times for typical questions.

</td>
<td width="50%" valign="top">

### 📦 Pip Installable Package
Core logic lives in the reusable `rag_pipeline` package, distributed as a prebuilt wheel in `dist/` for instant installation.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🐳 Containerized
Fully Dockerized via the included `dockerfile` for consistent, reproducible runs across local machines and cloud servers.

</td>
<td width="50%" valign="top">

### ☁️ Deployed on AWS EC2
Live deployment on AWS EC2 demonstrates the system runs in a real cloud environment, not just on a laptop.

</td>
</tr>
</table>

---

## 🏗️ Architecture

![IntelliQA RAG Flow](./RAG%20Flow.png)

IntelliQA follows a clean two phase RAG design.

### 1. Ingestion (run once per document set)

1. **Upload** documents in any supported format.
2. **Parse** with Apache Tika to extract clean text.
3. **Deduplicate** already indexed content.
4. **Chunk** the text into overlapping segments.
5. **Embed** each chunk into a 384 dimensional vector using `all-MiniLM-L6-v2`.
6. **Index** vectors into ChromaDB, persisted in `chroma_db/`.

### 2. Query (runs per question)

1. **Embed** the user question with the same embedding model.
2. **Retrieve** the top K nearest chunks via cosine similarity.
3. **Assemble** a prompt combining the question, retrieved context, and session history.
4. **Generate** the answer with Llama 3.3 70B at `temperature=0`.
5. **Return** the response while preserving session state for follow ups.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Language** | Python 3.x | Core implementation |
| **Notebook** | Jupyter | Interactive demo and development |
| **RAG Framework** | LangChain | Orchestration of ingestion and retrieval |
| **Vector Store** | ChromaDB | Persistent similarity search over embeddings |
| **LLM** | Llama 3.3 70B Versatile | Answer generation |
| **LLM Serving** | Groq (LPU inference) | Low latency model serving |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` | Semantic vector representation |
| **Embedding Hub** | Hugging Face | Model hosting and distribution |
| **Document Parsing** | Apache Tika | Unified extraction across formats |
| **Packaging** | `setup.py` + wheel | Distributable Python package |
| **Containerization** | Docker | Reproducible runtime |
| **Deployment** | AWS EC2 | Cloud hosting |

---

## 📁 Project Structure

```
IntelliQA/
├── IntelliQA.ipynb                          # Main notebook: end-to-end RAG demo
├── rag_pipeline/                            # Core RAG package source
│   ├── __init__.py
│   ├── query_engine.py                      # Query embedding, retrieval, generation
│   ├── vector_store.py                      # Chroma vector store setup and indexing
│   └── utils.py                             # Parsing, chunking, deduplication helpers
├── dist/
│   └── rag_pipeline-3.0-py3-none-any.whl    # Prebuilt installable package
├── chroma_db/                               # Persisted Chroma vector store
├── RAG Flow.png                             # Architecture diagram
├── dockerfile                               # Container definition
├── requirements.txt                         # Python dependencies
├── setup.py                                 # Package build configuration
└── README.md
```

---

## 🚀 Installation & Usage

You have three ways to get IntelliQA running, depending on your goal.

### Option 1: Install the Prebuilt Wheel (Fastest)

Install the `rag_pipeline` package directly from the prebuilt wheel shipped in `dist/`. This is the cleanest path if you just want to use IntelliQA as a library in your own code.

```bash
# Clone the repository (or download just the wheel from GitHub)
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Install the prebuilt wheel
pip install dist/rag_pipeline-3.0-py3-none-any.whl

# Set the Groq API key
export GROQ_API_KEY="your-key-here"
```

You can now import and use the package anywhere:

```python
from rag_pipeline import vector_store, query_engine, utils

# See IntelliQA.ipynb for full usage examples
```

### Option 2: Install from Source (For Development)

Use this path if you want to modify the RAG logic, contribute, or run the demo notebook end to end.

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate              # On Windows: venv\Scripts\activate

# Install dependencies and the package in editable mode
pip install -r requirements.txt
pip install -e .

# Set the Groq API key
export GROQ_API_KEY="your-key-here"

# Launch the notebook
jupyter notebook IntelliQA.ipynb
```

### Option 3: Run with Docker

Use this path for a fully isolated, reproducible runtime.

```bash
# Build the image
docker build -t intelliqa -f dockerfile .

# Run the container
docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

The container exposes Jupyter on port 8888. Open the printed URL in your browser to interact with `IntelliQA.ipynb`.

---

## 🧠 Design Decisions

The choices a hiring manager or senior engineer is most likely to ask about.

| Decision | Rationale |
|----------|-----------|
| **Groq + Llama 3.3 70B** | Sub second inference via LPU serving, with open weight flexibility and no LLM vendor lock in |
| **`temperature=0`** | Deterministic, repeatable answers, which is critical for document Q&A where the same question should return the same response |
| **`all-MiniLM-L6-v2` embeddings** | 384 dimensional vectors, fast on CPU, no API cost, strong quality for general semantic search |
| **ChromaDB (local persistence)** | Simple to operate, no separate infrastructure to manage, supports metadata filtering and persistence out of the box |
| **Apache Tika for parsing** | One extraction layer across dozens of formats, eliminating format specific parser maintenance |
| **Deduplication at ingestion** | Prevents the vector store from being polluted with repeated content, which would skew similarity scores |
| **Reusable `rag_pipeline` package** | Core logic is decoupled from the notebook and shipped as a wheel, so it can be imported into a future API or web app without rewrites |

---

## 👤 About the Author

**Abhijit Deshpande**, Business Systems Analyst (AI/ML Systems) at Charter Communications, actively transitioning into Data Science, ML, and AI Engineering roles. M.S. Industrial Engineering, University of Texas at Arlington (GPA 3.9/4.0).

<p align="left">
  <a href="https://theanalyticmind.com"><img src="https://img.shields.io/badge/Portfolio-theanalyticmind.com-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>
  <a href="https://linkedin.com/in/abhijit-deshpande/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/abhijitdeshpande83"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

---

## 📄 License

This project is open source under the **MIT License**. See [LICENSE](./LICENSE) for details.

<p align="center">
  <sub>Built with ❤️ as part of the <a href="https://github.com/abhijitdeshpande83/GenAI">GenAI portfolio</a>.</sub>
</p>