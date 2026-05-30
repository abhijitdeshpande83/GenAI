# IntelliQA: Document-Grounded RAG System

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) system** designed for grounded document question answering using a combination of:

- multi-format document parsing
- semantic chunk retrieval over a persistent vector store
- deterministic LLM generation bounded to retrieved context

The system is built to explore a key production challenge in modern GenAI:

> How to make LLM answers **traceable and reliable** when working with private documents the model has never seen.
---


## Problem Statement

Most document Q&A systems built on LLMs fail in production due to:

- hallucinated answers when questions fall outside training data
- inability to cite or trace the source of an answer
- repeated re-indexing of the same content, degrading retrieval quality
- one-shot Q&A with no follow-up understanding
- monolithic notebook designs that cannot be reused as a service

This leads to:

- unreliable outputs that erode user trust
- bloated vector stores filled with duplicate chunks
- tightly coupled code that breaks when promoting from prototype to production

IntelliQA is designed to address these issues using a **grounded, deduplicated, and packaged** architecture.

---


## 🧠 System Design Philosophy

IntelliQA follows a **retrieval-first GenAI architecture**:

### 1. Grounded Generation Principle

All answers are generated from retrieved document context only. The LLM operates with `temperature=0` and is constrained to use the retrieval payload, eliminating speculative output.

### 2. Persistence Over Recomputation

Documents are parsed, chunked, embedded, and indexed once. ChromaDB persists vectors to disk, so subsequent sessions reuse the existing index without re-ingestion.

### 3. Package-First Distribution

Core RAG logic ships as the `rag_pipeline` Python wheel, not as a notebook-only artifact. The notebook is a demo. The wheel is the product.

---


## 🏗️ High-Level Architecture

The system follows a **three-layer design pattern**:

### 1. Ingestion Layer

- Apache Tika multi-format text extraction
- chunk-level deduplication against the existing index
- semantic chunking with overlap

### 2. Storage Layer

- ChromaDB persistent vector store
- HuggingFace `all-MiniLM-L6-v2` embeddings (384 dimensional)

### 3. Generation Layer

- Llama 3.3 70B Versatile served via Groq LPU
- session-aware prompt assembly
- retrieval-bounded answer generation

---


## 🔄 Core Execution Flow

1. User uploads documents in supported formats
2. Ingestion pipeline parses, deduplicates, chunks, embeds, and indexes
3. User submits a question via chat interface
4. Query engine retrieves top-K chunks via cosine similarity
5. LLM generates a grounded answer at `temperature=0`
6. Response returned with session state preserved for follow-up questions

---


## 🧠 Design Decision: Why Open Stack Instead of Managed APIs

A fully managed approach (GPT-4 + OpenAI embeddings + Pinecone) was initially considered for simplicity but introduced several production constraints:

### Constraints Observed:

- recurring embedding API costs at ingestion scale
- vendor lock-in across LLM, embeddings, and vector store
- rate limits on bulk ingestion of large document sets
- no control over embedding model or dimensionality
- data leaves the deployment environment

### Final Decision:

An **open stack architecture was adopted**:

- Llama 3.3 70B (open weight) served on Groq for hosted inference
- HuggingFace `all-MiniLM-L6-v2` for local, CPU-friendly embeddings
- ChromaDB persisted on disk, no hosted vector database
- Apache Tika for unified, open-source document parsing

This improved:

- ingestion cost (zero per-document embedding cost)
- portability (the entire stack runs anywhere the wheel is installed)
- control (model and dimensionality choices are explicit)
- speed (Groq LPU inference rivals API-served closed models)

---


## 🧩 System Components

### 🔹 Document Parser

Engine: Apache Tika
Function: extracts clean text from PDF, DOCX, HTML, TXT, RTF, ODT, and dozens of additional formats through a single interface

---


### 🔹 Ingestion Pipeline

Module: `rag_pipeline.utils`
Function: handles parsing, chunking, deduplication, and metadata extraction before indexing

---


### 🔹 Vector Store

Engine: ChromaDB (persisted in `chroma_db/`)
Function: cosine similarity search over 384 dimensional embeddings, with metadata filtering and disk persistence

---


### 🔹 Query Engine

Module: `rag_pipeline.query_engine`
Function: embeds questions, retrieves top-K chunks, assembles prompts, and orchestrates generation

---


### 🔹 LLM Layer

Model: Llama 3.3 70B Versatile served via Groq LPU
Function: deterministic, grounded answer generation at `temperature=0`

---


### 🔹 Infrastructure Layer

- Docker
- AWS EC2
- Python wheel packaging (`setup.py` + `dist/rag_pipeline-3.0-py3-none-any.whl`)

---


## 🛠 Tech Stack

| **LLM & Inference** | ![Llama 3.3 70B](https://img.shields.io/badge/Llama%203.3%2070B-0467DF?logo=meta&logoColor=white) ![Groq LPU](https://img.shields.io/badge/Groq%20LPU-F55036?logo=lightning&logoColor=white) |
| --- | --- |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black) ![all-MiniLM-L6-v2](https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?logo=pytorch&logoColor=white) |
| **RAG Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?logo=databricks&logoColor=white) |
| **Document Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache%20Tika-D22128?logo=apache&logoColor=white) |
| **Deployment** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?logo=amazonaws&logoColor=white) |
| **Packaging** | ![setup.py + wheel](https://img.shields.io/badge/setup.py%20%2B%20wheel-3776AB?logo=pypi&logoColor=white) |
| **Programming Language** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white) |

---


## 📊 Key System Characteristics

- Grounded generation (retrieval-only context, `temperature=0`)
- Multi-format ingestion via a single parsing layer (Apache Tika)
- Persistent on-disk vector store (no re-indexing across sessions)
- Chunk-level deduplication at ingestion
- Session-aware conversational state
- Open stack (open weight LLM + local embeddings + local vector store)
- Pip-installable distribution (`rag_pipeline-3.0-py3-none-any.whl`)
- Containerized via single `dockerfile`

---


## 🧪 Workflow Visualization

![IntelliQA RAG Flow](./RAG%20Flow.png)

---


## 🚀 Installation & Usage

### Option 1: Install the Prebuilt Wheel (Fastest)

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA
pip install dist/rag_pipeline-3.0-py3-none-any.whl
export GROQ_API_KEY="your-key-here"
```

### Option 2: Install from Source (For Development)

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

python -m venv venv
source venv/bin/activate              # Windows: venv\Scripts\activate

pip install -r requirements.txt
pip install -e .

export GROQ_API_KEY="your-key-here"
jupyter notebook IntelliQA.ipynb
```

### Option 3: Run with Docker

```bash
docker build -t intelliqa -f dockerfile .

docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

---


## 🚧 Current Status

- Core RAG pipeline complete and packaged as an installable wheel
- Multi-format ingestion via Apache Tika operational
- ChromaDB persistence integrated
- Llama 3.3 70B Versatile inference live on AWS EC2
- Formal evaluation framework in progress

---


## 🚀 Future Improvements

- RAG evaluation pipeline (faithfulness, answer relevance, context precision)
- Cross-encoder reranking on retrieved chunks
- Inline citations linking answers to source chunks
- Hybrid retrieval (BM25 + dense vector)
- Streaming responses for lower perceived latency
- Web UI layer to replace the notebook entry point

---


## 💡 System Value

IntelliQA demonstrates how modern RAG systems can be designed using:

- retrieval-bounded generation
- open weight model serving
- persistent local indexing
- distributable Python packaging

It reflects real-world production constraints where **groundedness, cost control, and portability matter more than chasing the largest closed-source model**.

---

> This project focuses on **production-grade RAG system design, with an installable package as the primary artifact.**