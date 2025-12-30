<h1 align="center">IntelliQA</h1>

<p align="center">
  <i>A document-grounded RAG system. Ask any document, get verified answers.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Build-rag__pipeline_v3.0-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Deployed-AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white"/>
</p>

<p align="center">
  <img src="./RAG%20Flow.png" alt="IntelliQA Architecture" width="85%"/>
</p>

<p align="center">
  <b>Drop in a document. Ask a question. Get an answer grounded in your own sources.</b><br/>
  <sub>Powered by Llama 3.3 70B over a persistent vector store, packaged as an installable Python wheel.</sub>
</p>

---

## Overview

IntelliQA grounds LLM answers in your own documents using Retrieval Augmented Generation. It runs on **Llama 3.3 70B** served via **Groq**, **HuggingFace** embeddings, and a persistent **ChromaDB** store. Core logic ships as an installable Python wheel, so you can drop it into any service or notebook with a single `pip install`.

## Quickstart

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA
pip install dist/rag_pipeline-3.0-py3-none-any.whl
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

## Tech Stack

<p align="center">
  <b>LLM & Inference</b><br/>
  <img src="https://img.shields.io/badge/Llama_3.3_70B_Versatile-0467DF?style=for-the-badge&logo=meta&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq_LPU-F55036?style=for-the-badge&logoColor=white"/>
</p>

<p align="center">
  <b>Embeddings</b><br/>
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
  <img src="https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?style=for-the-badge&logoColor=white"/>
</p>

<p align="center">
  <b>RAG Framework</b><br/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logoColor=white"/>
</p>

<p align="center">
  <b>Parsing & Runtime</b><br/>
  <img src="https://img.shields.io/badge/Apache_Tika-D22128?style=for-the-badge&logo=apache&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

<p align="center">
  <b>Infrastructure</b><br/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"/>
</p>

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
├── IntelliQA.ipynb                          # End-to-end demo notebook
├── rag_pipeline/                            # Core package source
│   ├── query_engine.py                      # Retrieval and generation
│   ├── vector_store.py                      # Chroma setup and indexing
│   └── utils.py                             # Parsing, chunking, dedup
├── dist/rag_pipeline-3.0-py3-none-any.whl   # Prebuilt installable wheel
├── chroma_db/                               # Persisted vector store
├── RAG Flow.png                             # Architecture diagram
├── dockerfile
├── requirements.txt
└── setup.py
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

