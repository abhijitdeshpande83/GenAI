# IntelliQA: Document-Grounded RAG System

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** for grounded question answering over private documents. Core logic ships as a Python wheel so the same package can power a notebook demo today and an API service tomorrow without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

Document Q&A systems built on LLMs face well-known production failure modes:

- **Hallucination** when questions reach beyond the model's training data
- **Storage bloat** when documents get re-ingested across sessions, polluting retrieval
- **Cross-tenant data leakage** in shared deployments without proper isolation
- **Disk exhaustion** when uploads grow unbounded and sessions live forever
- **Non-deterministic outputs** that make the same question yield different answers on different runs
- **Notebook-only architectures** that work as prototypes but cannot be promoted to a service

## TL;DR

IntelliQA is a packaged RAG backend that directly addresses each of the failure modes above. Sessions are **isolated** (no cross-user leakage), capped at **5 uploads** (abuse prevention), content is **deduplicated** at ingestion, and a **scheduled cron job** manages disk space. Generation runs on **Llama 3.3 70B via Groq** against a persistent **ChromaDB** store. Shipped as the `rag_pipeline` Python wheel and currently powering document Q&A on [theanalyticmind.com](https://theanalyticmind.com).

## 🛠️ Tech Stack

| **LLM & Inference** | ![Llama 3.3 70B](https://img.shields.io/badge/Llama%203.3%2070B-0467DF?logo=meta&logoColor=white) ![Groq LPU](https://img.shields.io/badge/Groq%20LPU-F55036?logo=lightning&logoColor=white) |
| --- | --- |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?logo=huggingface&logoColor=black) ![all-MiniLM-L6-v2](https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?logo=pytorch&logoColor=white) |
| **RAG Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?logo=databricks&logoColor=white) |
| **Document Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache%20Tika-D22128?logo=apache&logoColor=white) |
| **Deployment** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?logo=amazonaws&logoColor=white) |
| **Packaging** | ![Wheel](https://img.shields.io/badge/setup.py%20%2B%20wheel-3776AB?logo=pypi&logoColor=white) |
| **Programming Language** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white) |

## 🧠 System Design Philosophy

**1. Grounded Generation.** LLM runs at `temperature=0` and answers only from retrieved chunks. No speculation.

**2. Multi-Tenant Isolation.** Documents and queries are namespaced per session. Each user retrieves only from their own uploads.

**3. Operational Discipline.** Upload quotas, scheduled cleanup, and deduplication are first-class features, not afterthoughts.

**4. Package-First Distribution.** Core RAG logic ships as a Python wheel. The notebook is a demo. The wheel is the product, and it powers the live portfolio site.

## 🏗️ High-Level Architecture

The system is organized into four layers:

**Ingestion** &nbsp;·&nbsp; Apache Tika parses multi-format input; deduplication and chunking happen before vectors touch the store.

**Storage** &nbsp;·&nbsp; ChromaDB persists 384-dimensional vectors from `all-MiniLM-L6-v2`, namespaced by session.

**Generation** &nbsp;·&nbsp; Llama 3.3 70B Versatile (served on Groq LPU) generates answers bounded to retrieved context.

**Operations** &nbsp;·&nbsp; Session lifecycle, per-session upload quotas, and a daily cron job for cleanup.

![IntelliQA RAG Flow](./RAG%20Flow.png)

## ✨ Key Features

<table>
<tr>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/lucide:files.svg?color=%23D22128" width="56" height="56"/>
<br/><br/>
<b>Universal Ingestion</b>
<br/><br/>
<sub>PDF, DOCX, HTML, TXT, RTF, ODT, and dozens more, parsed through a single Apache Tika layer.</sub>
<br/><br/>
</td>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/lucide:shield-check.svg?color=%232563EB" width="56" height="56"/>
<br/><br/>
<b>Tenant-Safe by Design</b>
<br/><br/>
<sub>Per-session ChromaDB namespacing. Zero cross-user data leakage, enforced at retrieval.</sub>
<br/><br/>
</td>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/lucide:gauge.svg?color=%23F59E0B" width="56" height="56"/>
<br/><br/>
<b>Abuse-Proof Uploads</b>
<br/><br/>
<sub>Hard cap of 5 documents per session. Storage exhaustion blocked at the source.</sub>
<br/><br/>
</td>
</tr>
<tr>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/lucide:sparkles.svg?color=%2310B981" width="56" height="56"/>
<br/><br/>
<b>Self-Cleaning Storage</b>
<br/><br/>
<sub>Daily cron job purges expired sessions, orphaned vectors, and Tika temp files.</sub>
<br/><br/>
</td>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/lucide:fingerprint.svg?color=%237C3AED" width="56" height="56"/>
<br/><br/>
<b>Smart Deduplication</b>
<br/><br/>
<sub>Hash-based ingestion checks. The same content is never indexed twice.</sub>
<br/><br/>
</td>
<td align="center" width="33%" valign="top">
<br/>
<img src="https://api.iconify.design/simple-icons:pypi.svg?color=%233776AB" width="56" height="56"/>
<br/><br/>
<b>One Pip Install</b>
<br/><br/>
<sub>Shipped as <code>rag_pipeline-3.0</code>. Drop it into any application as a backend.</sub>
<br/><br/>
</td>
</tr>
</table>

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

## 🚀 Installation & Usage

### Option 1: Install the Prebuilt Wheel
*Use this if you want IntelliQA as a ready-to-use RAG backend in your own application.* This is the path used by the live portfolio site.

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
*Use this if you want to read, modify, or extend the core RAG logic.* The editable install (`pip install -e .`) picks up source changes immediately without reinstalling.

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

|  |  |
| --- | --- |
| **Shipped** | Core pipeline, session isolation, upload quota, scheduled cleanup, AWS EC2 deployment, `rag_pipeline-3.0` wheel |
| **In progress** | RAG evaluation framework (faithfulness, answer relevance, context precision) |

## 🚀 Future Improvements

- RAG evaluation pipeline (faithfulness, answer relevance, context precision)
- Cross-encoder reranking on retrieved chunks
- Inline citations linking answers back to source chunks
- Hybrid retrieval (BM25 + dense vector)
- Streaming responses for lower perceived latency

## 💡 System Value

IntelliQA shows that a RAG backend can be **grounded, multi-tenant, operationally sound, and portable** without depending on managed APIs. The production discipline (session isolation, upload quotas, scheduled cleanup, deduplication) is built into the package, not bolted on later.

> Production-grade RAG, distributed as a wheel, powering a live portfolio site today.