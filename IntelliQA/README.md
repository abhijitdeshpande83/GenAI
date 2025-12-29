<h1 align="center">IntelliQA</h1>

<p align="center">
  <i>A document-grounded RAG system. Ask any document, get verified answers.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Build-rag__pipeline_v3.0-blue?style=flat-square" alt="Build"/>
  <img src="https://img.shields.io/badge/Deployed-AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white" alt="Deployed"/>
</p>

<p align="center">
  <img src="./RAG%20Flow.png" alt="IntelliQA Architecture" width="85%"/>
</p>

## Overview

IntelliQA grounds LLM answers in your own documents using Retrieval Augmented Generation. It runs on Llama 3.3 70B (served via Groq), HuggingFace embeddings, and a persistent ChromaDB store. Core logic ships as an installable Python wheel.

## Quickstart

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA
pip install dist/rag_pipeline-3.0-py3-none-any.whl
export GROQ_API_KEY="your-key-here"
```

Then open `IntelliQA.ipynb` for end-to-end usage.

## Features

| | |
|:--|:--|
| **Multi-format ingestion** | PDF, DOCX, HTML, TXT, RTF, ODT and more, via Apache Tika |
| **Smart deduplication** | Already indexed content is detected and skipped at ingestion |
| **Session-aware Q&A** | Follow-up questions resolve against earlier turns in the same session |
| **Grounded answers** | `temperature=0` and retrieval-only context to minimize hallucination |
| **Sub-second inference** | Llama 3.3 70B served on Groq's LPU hardware |
| **Pip-installable** | `rag_pipeline` ships as a versioned wheel in `dist/` |
| **Containerized** | Single `dockerfile` for reproducible local and cloud runs |
| **Cloud-deployed** | Live on AWS EC2 |

## Tech Stack

| Layer | Stack |
|:--|:--|
| **LLM** | ![Llama](https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white) ![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square&logoColor=white) |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/all--MiniLM--L6--v2-FFD21E?style=flat-square&logo=huggingface&logoColor=black) |
| **Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logoColor=white) |
| **Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache_Tika-D22128?style=flat-square&logo=apache&logoColor=white) |
| **Runtime** | ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) |
| **Infra** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) |

## Install from Source

For development or to run the demo notebook end-to-end.

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

## Run with Docker

```bash
docker build -t intelliqa -f dockerfile .

docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

Jupyter is exposed on port `8888`.

## Project Structure

```
IntelliQA/
├── IntelliQA.ipynb                          # End-to-end demo notebook
├── rag_pipeline/                            # Core package source
│   ├── query_engine.py                      # Retrieval and generation
│   ├── vector_store.py                      # Chroma setup and indexing
│   └── utils.py                             # Parsing, chunking, dedup
├── dist/rag_pipeline-3.0-py3-none-any.whl   # Prebuilt wheel
├── chroma_db/                               # Persisted vector store
├── RAG Flow.png                             # Architecture diagram
├── dockerfile
├── requirements.txt
└── setup.py
```

## Design Notes

- **`temperature=0`** for deterministic, repeatable answers.
- **Local embeddings** (`all-MiniLM-L6-v2`) keep ingestion cost-free and CPU-friendly.
- **ChromaDB on disk** avoids the overhead of a hosted vector database.
- **Deduplication at ingestion** prevents repeated chunks from skewing similarity scores.
- **Core logic as a wheel** decouples the RAG engine from the notebook so it can drop into any service later.

