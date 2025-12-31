cat << 'EOF' > README.md
<h1 align="center">🤖 IntelliQA</h1>

<p align="center">
  <b>Ask any document. Get grounded answers.</b><br/>
  <sub>A production-oriented Retrieval-Augmented Generation (RAG) system that turns your PDFs, Word docs, HTML files, and more into a private, conversational knowledge base.</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Inference-Groq_LPU-F55036?style=flat-square" alt="Groq"/>
  <img src="https://img.shields.io/badge/Build-rag__pipeline_v3.0-blue?style=flat-square" alt="Build"/>
  <img src="https://img.shields.io/badge/Deployed-AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white" alt="Deployed"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
</p>

<p align="center">
  <img src="./RAG%20Flow.png" alt="IntelliQA Architecture" width="85%"/>
</p>

<p align="center">
  <b>Drop in a document. Ask a question. Get an answer grounded in your own sources.</b><br/>
  <sub>Powered by Llama 3.3 70B over a persistent vector store, packaged as an installable Python wheel.</sub>
</p>

---

## 📖 Overview

Large language models are powerful, but they do not know your private documents and they hallucinate on topics outside their training data. **IntelliQA solves both** by retrieving the most relevant chunks from your uploaded documents and passing them to the LLM as grounded context. The model answers only from what was retrieved, making the system reliable for enterprise document Q&A.

> [!NOTE]
> Core RAG logic is packaged in the `rag_pipeline` Python package and shipped as a **prebuilt wheel**, so anyone can install it with a single `pip install` and start asking questions.

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone [https://github.com/abhijitdeshpande83/GenAI.git](https://github.com/abhijitdeshpande83/GenAI.git)
cd GenAI/IntelliQA

# Install the prebuilt wheel
pip install dist/rag_pipeline-3.0-py3-none-any.whl

# Set your Groq API key
export GROQ_API_KEY="your-key-here"
```

Then open `IntelliQA.ipynb` for the end-to-end demo.

## In Action

```text
Q: Summarize the key risks identified in section 4 of the policy document.

A: Section 4 identifies three primary risks:

   1. Regulatory non-compliance from incomplete audit trails.
   2. Data exposure in third-party integrations lacking encryption at rest.
   3. Vendor lock-in due to proprietary API dependencies.

   Source: policy_v3.pdf, pages 12 to 14.
```

## Features

<table>
<tr>
<td width="50%" valign="top">

#### Multi-format ingestion
PDF, DOCX, HTML, TXT, RTF, ODT and dozens more, parsed through a single Apache Tika layer.

</td>
<td width="50%" valign="top">

#### Smart deduplication
Already-indexed documents and chunks are detected and skipped, keeping the vector store clean.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Session-aware Q&A
Follow-up questions resolve correctly against earlier turns in the same conversation.

</td>
<td width="50%" valign="top">

#### Grounded answers
`temperature=0` and retrieval-only context to minimize hallucination and keep responses traceable.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Sub-second inference
Llama 3.3 70B served on Groq's LPU hardware for fast, deterministic responses.

</td>
<td width="50%" valign="top">

#### Pip-installable package
The `rag_pipeline` package ships as a versioned wheel for instant installation anywhere.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Containerized
A single `dockerfile` defines a reproducible runtime for local and cloud deployment.

</td>
<td width="50%" valign="top">

#### Cloud-deployed
Running live on AWS EC2, demonstrating the system beyond a local environment.

</td>
</tr>
</table>

## 🛠️ Tech Stack

| Layer | Technologies & Frameworks |
| :--- | :--- |
| **LLM & Inference** | `Llama 3.3 70B` • `Groq LPU Engine` ![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square&logoColor=white) |
| **Orchestration** | `LangChain` ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) • `Python 3.x` • `Apache Tika` |
| **Vector Index** | `ChromaDB` ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square) • `all-MiniLM-L6-v2` (Hugging Face) |
| **Infrastructure** | `Docker` ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) • `AWS EC2` ![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) |
| **Workspace** | `Jupyter Notebooks` |

## Install from Source

For development or running the demo notebook end-to-end.

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
├── 📓 IntelliQA.ipynb                          # End-to-end interactive demo notebook
├── 📦 rag_pipeline/                            # Modularized production core source
│   ├── query_engine.py                         # Retrieval and generation orchestration
│   ├── vector_store.py                         # ChromaDB schema and index management
│   └── utils.py                                # Parsing, text chunking, and deduplication
├── 📂 dist/
│   └── rag_pipeline-3.0-py3-none-any.whl       # Prebuilt distributable package asset
├── 🗃️  chroma_db/                              # Persisted vector database storage
├── 🖼️  RAG Flow.png                            # Architecture diagram asset
├── 🐳 dockerfile                               # Unified container engine setup
├── 📜 requirements.txt                         # Pipeline micro-dependencies
└── ⚙️  setup.py                                # Packaging layout properties
```

## Design Notes

<table>
<tr>
<td width="50%" valign="top">

**`temperature=0`**
Deterministic, repeatable answers. Critical for document Q&A where the same question should return the same response.

</td>
<td width="50%" valign="top">

**Local embeddings**
`all-MiniLM-L6-v2` runs on CPU with no API cost and strong general-purpose quality.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**ChromaDB on disk**
Avoids the overhead and cost of a hosted vector database while supporting metadata filters and persistence.

</td>
<td width="50%" valign="top">

**Deduplication at ingestion**
Prevents repeated chunks from polluting the index and skewing similarity scores.

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Open weight model**
Llama 3.3 70B avoids LLM vendor lock-in while still offering frontier-grade quality.

</td>
<td width="50%" valign="top">

**Core as a wheel**
The `rag_pipeline` package decouples RAG logic from the notebook so it can drop into any future service.

</td>
</tr>
</table>

