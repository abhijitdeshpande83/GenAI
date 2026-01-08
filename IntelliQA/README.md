# IntelliQA: Document-Grounded RAG System

> **TL;DR** &nbsp; IntelliQA is a packaged RAG backend for grounded document Q&A. Each session is **isolated** (no cross-user document leakage), limited to **5 uploads** (abuse prevention), **deduplicates** content at ingestion, and a **scheduled cron job** manages disk space. Powered by **Llama 3.3 70B via Groq** and a persistent **ChromaDB** store. Shipped as the `rag_pipeline` Python wheel and currently powering the document Q&A on [theanalyticmind.com](https://theanalyticmind.com).

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** built around the operational concerns that separate prototypes from real services: tenant isolation, upload quotas, scheduled cleanup, deduplication, and deterministic generation. The core logic ships as an installable Python wheel so the same package can power a notebook demo, a portfolio site, or a future API service without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

Most document Q&A prototypes break when promoted to production:

- LLMs hallucinate when questions fall outside training data
- repeated ingestion bloats the vector store with duplicate chunks
- no per-user isolation leaks one user's documents to another
- unbounded uploads exhaust storage and degrade retrieval quality
- one-shot notebook code cannot be reused as a service
- no operational layer for cleanup, quotas, or session lifecycle

IntelliQA addresses each of these directly, not as future work.

## 🧠 System Design Philosophy

**1. Grounded Generation.** LLM runs at `temperature=0` and answers only from retrieved chunks. No speculation.

**2. Multi-Tenant Isolation.** Documents and queries are namespaced by session. Each user retrieves only from their own uploads.

**3. Operational Discipline.** Upload quotas, scheduled cleanup, and dedup are first-class features, not afterthoughts.

**4. Package-First Distribution.** Core RAG logic ships as a Python wheel. The notebook is a demo. The wheel is the product, and it powers the live portfolio site.

## 🏗️ High-Level Architecture

The system is organized into four layers:

**Ingestion** &nbsp;·&nbsp; Apache Tika parses multi-format input; deduplication and chunking happen before vectors touch the store.

**Storage** &nbsp;·&nbsp; ChromaDB persists 384-dimensional vectors from `all-MiniLM-L6-v2`, namespaced by session.

**Generation** &nbsp;·&nbsp; Llama 3.3 70B Versatile (served on Groq LPU) generates answers bounded to retrieved context.

**Operations** &nbsp;·&nbsp; Session lifecycle, per-session upload quotas, and a daily cron job for cleanup.

## 🔄 Core Execution Flow

1. User opens a new session (a session ID is issued)
2. User uploads up to 5 documents
3. Apache Tika parses; deduplication checks against the session's existing index
4. New chunks are embedded and indexed under the session namespace
5. User asks a question
6. Retrieval is scoped to the session; top-K chunks returned
7. Llama 3.3 70B generates a grounded answer at `temperature=0`
8. A daily cron job removes expired sessions, orphaned vectors, and Tika temp files

## ✨ Key Features

- **Multi-format ingestion**: PDF, DOCX, HTML, TXT, RTF, ODT and dozens more via a single Apache Tika layer
- **Grounded answer generation**: `temperature=0` and retrieval-bounded context to prevent hallucination
- **Session-aware Q&A**: follow-up questions resolve correctly against earlier turns in the same conversation
- **Sub-second inference**: Llama 3.3 70B served on Groq's LPU hardware
- **Persistent vector store**: ChromaDB on disk, so sessions reuse the existing index without re-ingestion
- **Multi-tenant session isolation**: documents and queries namespaced per session, no cross-user leakage
- **Upload quota**: hard limit of 5 documents per session to prevent abuse and storage exhaustion
- **Scheduled cleanup**: daily cron job removes expired sessions, orphaned vectors, and Tika temp files
- **Chunk-level deduplication**: hash-based checks at ingestion keep the index clean across re-uploads
- **Pip-installable distribution**: shipped as a versioned wheel (`rag_pipeline-3.0`) for production use

## 🛡️ Production Safeguards

| Safeguard | Mechanism |
| --- | --- |
| **Session isolation** | Documents and queries namespaced by session ID. No cross-tenant access. |
| **Upload quota** | Hard limit of 5 documents per session to prevent abuse. |
| **Scheduled cleanup** | Daily cron job removes expired sessions, orphaned chunks, and Tika temp files. |
| **Chunk deduplication** | Hash-based checks at ingestion prevent index pollution. |
| **Deterministic generation** | `temperature=0` ensures repeatable answers for the same question. |
| **Grounded retrieval** | LLM is restricted to retrieved context. No training-data bleed. |

## 🧠 Design Decision: Open Stack Over Managed APIs

A managed approach (GPT-4 + OpenAI embeddings + Pinecone) was rejected for several production reasons:

- recurring embedding API costs at ingestion scale
- vendor lock-in across LLM, embeddings, and vector store
- rate limits on bulk ingestion
- no control over embedding dimensionality or model behavior
- data leaving the deployment environment

**Decision** &nbsp;·&nbsp; Llama 3.3 70B (open weight, Groq LPU inference) + HuggingFace local embeddings + ChromaDB on disk + Apache Tika for parsing.

**Result** &nbsp;·&nbsp; Zero per-document embedding cost, no API rate limits, full portability with the wheel, and Groq inference latency that rivals managed-LLM APIs.

## 🧩 System Components

| Component | Engine / Module | Function |
| --- | --- | --- |
| **Document Parser** | Apache Tika | Extracts text from PDF, DOCX, HTML, TXT, RTF, ODT, and dozens of additional formats |
| **Ingestion Pipeline** | `rag_pipeline.utils` | Parsing, chunking, deduplication, metadata extraction |
| **Session Manager** | `rag_pipeline` (custom logic) | Namespaces documents by session, enforces 5-file upload quota |
| **Vector Store** | ChromaDB | Cosine similarity search over 384-dim embeddings, disk-persisted |
| **Query Engine** | `rag_pipeline.query_engine` | Embeds questions, retrieves top-K chunks, orchestrates generation |
| **LLM Layer** | Llama 3.3 70B (Groq LPU) | Deterministic, grounded generation at `temperature=0` |
| **Storage Manager** | Cron + cleanup scripts | Daily removal of expired sessions, orphaned vectors, temp files |
| **Infrastructure** | Docker + AWS EC2 | Reproducible runtime, cloud deployment |

## 🛠️ Tech Stack

| **LLM & Inference** | ![Llama 3.3 70B](https://img.shields.io/badge/Llama%203.3%2070B-0467DF?logo=meta&logoColor=white) ![Groq LPU](https://img.shields.io/badge/Groq%20LPU-F55036?logo=lightning&logoColor=white) |
| --- | --- |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black) ![all-MiniLM-L6-v2](https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?logo=pytorch&logoColor=white) |
| **RAG Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?logo=databricks&logoColor=white) |
| **Document Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache%20Tika-D22128?logo=apache&logoColor=white) |
| **Deployment** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?logo=amazonaws&logoColor=white) |
| **Packaging** | ![Wheel](https://img.shields.io/badge/setup.py%20%2B%20wheel-3776AB?logo=pypi&logoColor=white) |
| **Programming Language** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white) |

## 🧪 Workflow Visualization

![IntelliQA RAG Flow](./RAG%20Flow.png)

## 🚀 Installation & Usage

### Option 1: Install the Prebuilt Wheel  
*Use this if you want IntelliQA as a ready-to-use RAG backend in your own application.* This is the path used by the live portfolio site. No source code required, just the wheel.

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA
pip install dist/rag_pipeline-3.0-py3-none-any.whl
export GROQ_API_KEY="your-key-here"
```

Import and use anywhere:

```python
from rag_pipeline import query_engine, vector_store, utils
# See IntelliQA.ipynb for end-to-end usage examples
```

### Option 2: Install from Source  
*Use this if you want to read, modify, or extend the core RAG logic.* The editable install (`pip install -e .`) means your source changes are picked up immediately without reinstalling the wheel.

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

## 🚧 Current Status

- Core RAG pipeline complete and shipped as an installable wheel (`rag_pipeline-3.0`)
- Production deployment live on AWS EC2, powering document Q&A on the portfolio site
- Session isolation, 5-file upload quota, and cron-based cleanup operational
- Multi-format ingestion via Apache Tika integrated end to end
- Formal RAG evaluation framework in progress

## 🚀 Future Improvements

- RAG evaluation pipeline (faithfulness, answer relevance, context precision)
- Cross-encoder reranking on retrieved chunks
- Inline citations linking answers back to source chunks
- Hybrid retrieval (BM25 + dense vector)
- Streaming responses for lower perceived latency

## 💡 System Value

IntelliQA shows that a RAG backend can be **grounded, multi-tenant, operationally sound, and portable** without depending on managed APIs. The production discipline (session isolation, upload quotas, scheduled cleanup, deduplication) is built into the package, not bolted on later.

> Production-grade RAG, distributed as a wheel, powering a live portfolio site today.