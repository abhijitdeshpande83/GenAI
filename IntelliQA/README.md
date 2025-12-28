<p align="center">
  <img src="./assets/banner.png" width="100%" />
</p>

<h1 align="center">🤖 IntelliQA</h1>

<p align="center">
  <b>Ask any document. Get grounded answers.</b><br/>
  <sub>
    A production-ready Retrieval Augmented Generation (RAG) system that transforms PDFs, DOCX, HTML, and more into a private conversational knowledge base.
  </sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/RAG-Powered-8A2BE2?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Stable-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Deployed-AWS%20EC2-FF9900?style=flat-square&logo=amazonaws" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>

---

## 📖 Overview

Large language models are powerful—but they don’t know your private data and often hallucinate outside their training distribution.

**IntelliQA solves this by grounding every answer in your documents.**

It retrieves the most relevant chunks from your knowledge base and injects them into the LLM context, ensuring responses are:

- 📌 Fact-based  
- 📌 Context-aware  
- 📌 Source-grounded  

> 💡 The core RAG engine is packaged as a reusable Python wheel (`rag_pipeline`), so it can be installed and used anywhere with a single command.

---

## ✨ Key Features

### 🗂️ Universal Document Support
Supports PDFs, DOCX, HTML, TXT, RTF, and more via a unified parsing layer.

### 🔍 Intelligent Retrieval
Semantic search using embeddings + ChromaDB for precise context matching.

### 💬 Context-Aware Conversations
Maintains session history for follow-up question understanding.

### 🎯 Grounded Responses
Temperature = 0 ensures deterministic, non-hallucinated outputs.

### ⚡ High-Speed Inference
Powered by Groq’s LPU runtime with Llama 3.3 70B for sub-second responses.

### 📦 Plug & Play Package
Core engine shipped as a pip-installable wheel (`rag_pipeline`).

### 🐳 Fully Containerized
Runs consistently across local machines and cloud via Docker.

### ☁️ Cloud Deployed
Live deployment on AWS EC2 for production-grade demonstration.

---

## 🏗️ Architecture

<p align="center">
  <img src="./RAG%20Flow.png" width="85%" />
</p>

IntelliQA follows a **two-stage RAG pipeline**:

### 📥 Ingestion Flow
Upload → Parse (Apache Tika) → Deduplicate → Chunk → Embed → Store (ChromaDB)

### 🔎 Query Flow
User Query → Embed → Retrieve Top-K → Build Context → LLM Generation → Response

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python 3.x |
| Framework | LangChain |
| Vector DB | ChromaDB |
| LLM | Llama 3.3 70B |
| Inference | Groq LPU |
| Embeddings | all-MiniLM-L6-v2 |
| Parsing | Apache Tika |
| Packaging | Python Wheel |
| Container | Docker |
| Deployment | AWS EC2 |

---

## 🚀 Quick Start

### ⚡ Install (Recommended)

```bash
pip install dist/rag_pipeline-3.0-py3-none-any.whl