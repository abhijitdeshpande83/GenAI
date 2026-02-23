<style>
  .rag-container { font-family: 'Inter', system-ui, sans-serif; background: #0f172a; padding: 48px; border-radius: 24px; max-width: 1000px; margin: 0 auto 40px auto; border: 1px solid #1e293b; box-sizing: border-box; }
  .rag-grid { width: 100%; border-collapse: separate; border-spacing: 20px 0; table-layout: fixed; margin: 0 -20px; }
  .grid-card { background: #1e293b; border: 1px solid #334155; border-radius: 16px; height: 100%; overflow: hidden; }
  .pillar-header { padding: 24px; background: rgba(239, 68, 68, 0.03); border-bottom: 1px solid #334155; }
  .pillar-body { padding: 24px; background: rgba(56, 189, 248, 0.05); }
  .feature-card { background:#ffffff; border-top: 4px solid #ccc; border-radius:16px; padding:28px 24px; height:100%; min-height:190px; box-sizing:border-box; box-shadow:0 10px 25px -5px rgba(0,0,0,0.2); }
  .paradigm-label { color: #38bdf8; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px; font-weight: 700; }
  .card-title { margin: 0 0 10px 0; font-size:18px; font-weight:800; color:#0f172a; }
</style>

# IntelliQA: Document-Grounded RAG System

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** for grounded question answering over private documents. Core logic ships as a Python wheel so the same package can power a notebook demo today and an API service tomorrow without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

<div class="rag-container">
  <div style="text-align: center; margin-bottom: 48px;">
    <h2 style="margin: 0 0 16px; font-size: 32px; font-weight: 800; color: #ffffff;">Why Standard RAG Fails in Production</h2>
    <p style="color: #94a3b8; font-size: 16px; max-width: 700px; margin: 0 auto;">Transitioning from "Hello World" scripts to reliable, multi-tenant services exposes fundamental flaws in the modern AI stack.</p>
  </div>
  <table class="rag-grid" role="presentation">
    <tr>
      <td><div class="grid-card"><div class="pillar-header"><h3 style="color:#fff; font-size:17px; margin:0 0 12px;"><img src="https://api.iconify.design/lucide:brain-circuit.svg?color=%23ef4444" width="20"/> The Knowledge Gap</h3><p style="color:#94a3b8; font-size:13px; margin:0;">Models hallucinate when questions reach beyond their fixed training data.</p></div><div class="pillar-body"><span class="paradigm-label">IntelliQA Paradigm</span><p style="color:#cbd5e1; font-size:13px; margin:0;">Strictly bounds generation to your retrieved document context only.</p></div></div></td>
      <td><div class="grid-card"><div class="pillar-header"><h3 style="color:#fff; font-size:17px; margin:0 0 12px;"><img src="https://api.iconify.design/lucide:server-crash.svg?color=%23ef4444" width="20"/> The Prototype Trap</h3><p style="color:#94a3b8; font-size:13px; margin:0;">Notebook scripts fail under multi-tenant load and lack operational safety.</p></div><div class="pillar-body"><span class="paradigm-label">IntelliQA Paradigm</span><p style="color:#cbd5e1; font-size:13px; margin:0;">Ships as a robust, isolated Python wheel, production-ready by design.</p></div></div></td>
      <td><div class="grid-card"><div class="pillar-header"><h3 style="color:#fff; font-size:17px; margin:0 0 12px;"><img src="https://api.iconify.design/lucide:coins.svg?color=%23ef4444" width="20"/> The API Tax</h3><p style="color:#94a3b8; font-size:13px; margin:0;">Proprietary embedding APIs scale costs exponentially as documents grow.</p></div><div class="pillar-body"><span class="paradigm-label">IntelliQA Paradigm</span><p style="color:#cbd5e1; font-size:13px; margin:0;">Leverages local open-weight models, dropping bulk ingestion costs to zero.</p></div></div></td>
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

<div class="rag-container" style="margin-bottom: 40px; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
  <div style="border-bottom: 1px solid #1e293b; padding-bottom: 24px; margin-bottom: 32px;">
    <h3 style="margin: 0 0 12px 0; color: #ffffff; font-size: 24px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
      <img src="https://api.iconify.design/lucide:git-branch.svg?color=%2338bdf8" width="28"/> Architecture Rationale
    </h3>
    <p style="margin: 0; color: #94a3b8; font-size: 16px; line-height: 1.6; max-width: 800px;">Why bypass managed services like OpenAI and Pinecone? Because prototype economics rarely survive production scale. We designed IntelliQA to maintain high inference quality without the compounding costs of proprietary APIs.</p>
  </div>
  <table role="presentation" style="width: 100%; border-collapse: separate; border-spacing: 24px 0; table-layout: fixed; margin: 0 -12px;">
    <tr>
      <td class="grid-card" style="padding: 24px;">
        <h4 style="margin: 0 0 16px 0; color: #fca5a5; font-size: 15px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">The Managed Trap</h4>
        <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 14px; line-height: 1.7;">
          <li style="margin-bottom: 8px;"><strong>Recurring Costs:</strong> Paying per-token for embedding bulk documents destroys margins.</li>
          <li style="margin-bottom: 8px;"><strong>Data Privacy:</strong> Sending proprietary documents to third-party endpoints violates strict compliance rules.</li>
          <li style="margin-bottom: 8px;"><strong>Rate Limits:</strong> Bulk ingestion hits API throttling caps instantly.</li>
          <li><strong>Vendor Lock-in:</strong> Tightly coupling your vector store to a specific embedding model makes future migrations painful.</li>
        </ul>
      </td>
      <td class="grid-card" style="padding: 24px; border: 1px solid #38bdf8; position: relative;">
        <span style="position: absolute; top: -10px; right: 24px; background: #38bdf8; color: #0f172a; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; text-transform: uppercase;">Our Stack</span>
        <h4 style="margin: 0 0 16px 0; color: #38bdf8; font-size: 15px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">The Open Reality</h4>
        <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 14px; line-height: 1.7;">
          <li style="margin-bottom: 8px;"><strong>Zero-Cost Embeddings:</strong> <code>all-MiniLM-L6-v2</code> runs locally via HuggingFace, making ingestion permanently free.</li>
          <li style="margin-bottom: 8px;"><strong>Blistering Speed:</strong> Offloading LLM generation to Groq LPUs provides inference latency that beats managed GPT APIs.</li>
          <li style="margin-bottom: 8px;"><strong>Data Sovereignty:</strong> ChromaDB stores vectors locally on-disk. Your data never leaves your environment.</li>
          <li><strong>Ultimate Portability:</strong> Local dependencies mean the entire RAG backend ships reliably inside a single Python wheel.</li>
        </ul>
      </td>
    </tr>
  </table>
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