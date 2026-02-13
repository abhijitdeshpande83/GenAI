# IntelliQA: Document-Grounded RAG System

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** for grounded question answering over private documents. Core logic ships as a Python wheel so the same package can power a notebook demo today and an API service tomorrow without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

<div style="
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: #0f172a;
  padding: 56px 48px;
  border-radius: 24px;
  max-width: 1000px;
  margin: 0 auto 40px auto;
  border: 1px solid #1e293b;
  box-sizing: border-box;
">
  <div style="text-align: center; margin-bottom: 40px;">
    <h2 style="margin: 0 0 16px 0; font-size: 32px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">
      The Production Reality
    </h2>
    <p style="margin: 0 auto; color: #94a3b8; font-size: 16px; line-height: 1.6; max-width: 650px;">
      Document Q&A prototypes built on standard tutorials face severe failure modes when exposed to real users. Here is why they break, and exactly how IntelliQA fixes them.
    </p>
  </div>

  <table role="presentation" style="
    width: 100%;
    border-collapse: separate;
    border-spacing: 16px;
    table-layout: fixed;
    margin: -16px;
  ">
    <tr>
      <td style="vertical-align: top;">
        <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
          <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
            <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
            <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Hallucination</h4>
            <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Models invent answers when questions reach beyond retrieved context.</p>
          </div>
          <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
            <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
            <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Locked at <code>temperature=0</code> with strict system prompts bounding generation to chunks only.</p>
          </div>
        </div>
      </td>
      <td style="vertical-align: top;">
        <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
          <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
            <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
            <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Storage Bloat</h4>
            <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Identical documents re-ingested across sessions pollute retrieval arrays.</p>
          </div>
          <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
            <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
            <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Cryptographic hash-based parsing prevents indexing identical content twice.</p>
          </div>
        </div>
      </td>
      <td style="vertical-align: top;">
        <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
          <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
            <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
            <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Data Leakage</h4>
            <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Users in shared deployments accidentally retrieve other users' uploads.</p>
          </div>
          <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
            <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
            <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Strict, per-session ChromaDB namespacing enforces absolute vector isolation.</p>
          </div>
        </div>
      </td>
    </tr>

  <tr>
    <td style="vertical-align: top;">
      <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
        <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
          <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
          <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Disk Exhaustion</h4>
          <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Dormant sessions live forever, eventually crashing the host server.</p>
        </div>
        <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
          <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
          <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Automated cron jobs permanently purge expired collections and temp files.</p>
        </div>
      </div>
    </td>
    <td style="vertical-align: top;">
      <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
        <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
          <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
          <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Context Poisoning</h4>
          <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Users uploading massive libraries dilute the relevance of vector search.</p>
        </div>
        <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
          <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
          <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Hard limits capped at 5 documents per session maintain high signal-to-noise.</p>
        </div>
      </div>
    </td>
    <td style="vertical-align: top;">
      <div style="background: #1e293b; border: 1px solid #334155; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);">
        <div style="padding: 16px; background: rgba(239, 68, 68, 0.05); border-bottom: 1px solid #334155; border-left: 3px solid #ef4444;">
          <strong style="color: #fca5a5; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Problem</strong>
          <h4 style="margin: 6px 0; color: #ffffff; font-size: 16px;">Prototype Purgatory</h4>
          <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.4;">Notebook-only architectures break when transitioning to a live API service.</p>
        </div>
        <div style="padding: 16px; background: rgba(16, 185, 129, 0.05); border-left: 3px solid #10b981;">
          <strong style="color: #6ee7b7; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">The Solution</strong>
          <p style="margin: 6px 0 0; color: #cbd5e1; font-size: 13px; line-height: 1.4;">Shipped entirely as a production-ready Python wheel, dropping into any backend.</p>
        </div>
      </div>
    </td>
  </tr>
  </table>
</div>

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

## ✨ Key Features

<div style="
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  padding: 56px 48px;
  border-radius: 24px;
  max-width: 1000px;
  margin: 0 auto;
  border: 1px solid #334155;
  box-sizing: border-box;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
">

  <div style="text-align: center; margin-bottom: 40px;">
    <span style="
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
    ">Now Available</span>
    <h2 style="
      margin: 20px 0 16px 0;
      font-size: 38px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.5px;
    ">The Ultimate RAG Engine.</h2>
    <p style="
      margin: 0 auto;
      color: #94a3b8;
      font-size: 17px;
      line-height: 1.6;
      max-width: 600px;
    ">
      Drop it into any backend and watch your vector storage manage itself. Secure, self-cleaning, and infinitely scalable.
    </p>
  </div>

  <table role="presentation" style="
    width: 100%;
    border-collapse: separate;
    border-spacing: 20px;
    table-layout: fixed;
    margin: -20px; /* Offsets the spacing padding for perfect alignment */
  ">
    
<tr>
  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #D22128; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/lucide:files.svg?color=%23D22128" width="38" style="margin-bottom: 12px;" alt="Files"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">Universal Ingestion</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        PDF, DOCX, HTML, TXT, RTF, ODT via Apache Tika. We process it all.
      </p>
    </div>
  </td>

  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #2563EB; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/material-symbols:lock-person.svg?color=%232563EB" width="38" style="margin-bottom: 12px;" alt="Lock"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">Session Isolation</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        Per-session ChromaDB namespacing prevents cross-user data leakage.
      </p>
    </div>
  </td>

  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #10B981; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/material-symbols:auto-delete.svg?color=%2310B981" width="38" style="margin-bottom: 12px;" alt="Clean"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">Self-Cleaning Storage</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        Automatic background cleanup of expired sessions and temp vectors.
      </p>
    </div>
  </td>
</tr>

<tr>
  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #7C3AED; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/tabler:copy-off.svg?color=%237C3AED" width="38" style="margin-bottom: 12px;" alt="Dedupe"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">Smart Deduplication</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        Hash-based ingestion ensures identical content is never indexed twice.
      </p>
    </div>
  </td>

  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #F59E0B; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/lucide:gauge.svg?color=%23F59E0B" width="38" style="margin-bottom: 12px;" alt="Limits"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">Abuse-Proof Uploads</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        Intelligent hard caps and rate limits prevent storage abuse instantly.
      </p>
    </div>
  </td>

  <td style="vertical-align: top;">
    <div style="background:#ffffff; border-top: 4px solid #3776AB; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2);">
      <img src="https://api.iconify.design/simple-icons:pypi.svg?color=%233776AB" width="36" style="margin-bottom: 12px;" alt="PyPI"/>
      <h3 style="margin:0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a;">One Pip Install</h3>
      <p style="margin:0; color:#475569; font-size:14px; line-height:1.5;">
        Ready to plug into any backend. Install <code style="background:#f1f5f9; padding:2px 6px; border-radius:4px; font-size:13px; color:#0f172a; border:1px solid #e2e8f0; font-weight:600;">rag_pipeline-3.0</code>.
      </p>
    </div>
  </td>
</tr>

  </table>
</div>

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

## 🧠 Design Decision: Open Stack Over Managed APIs

<div style="
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background: linear-gradient(to right, #0f172a, #1e293b);
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 32px;
  max-width: 1000px;
  margin: 0 auto 32px auto;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
    <div style="background: #3b82f6; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
      <img src="https://api.iconify.design/lucide:git-pull-request.svg?color=white" width="24"/>
    </div>
    <h3 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: 700;">Design Decision: Open Stack over Managed APIs</h3>
  </div>
  
  <p style="color: #94a3b8; font-size: 15px; line-height: 1.6; margin: 0 0 20px 0;">
    A managed approach (GPT-4 + OpenAI embeddings + Pinecone) was rejected for several production reasons: recurring embedding API costs at scale, vendor lock-in, rate limits on bulk ingestion, and data leaving the deployment environment.
  </p>

  <div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); padding: 16px; border-radius: 8px;">
      <strong style="color: #38bdf8; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">The Decision</strong>
      <p style="margin: 6px 0 0 0; color: #cbd5e1; font-size: 15px;">Llama 3.3 70B (open weight, Groq LPU inference) + HuggingFace local embeddings + ChromaDB on disk + Apache Tika for parsing.</p>
    </div>
    <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.1); padding: 16px; border-radius: 8px;">
      <strong style="color: #10b981; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">The Result</strong>
      <p style="margin: 6px 0 0 0; color: #cbd5e1; font-size: 15px;">Zero per-document embedding cost, no API rate limits, full portability with the wheel, and Groq inference latency that rivals managed-LLM APIs.</p>
    </div>
  </div>
</div>

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