<style>
  /* Global Containers */
  .rag-container { font-family: 'Inter', system-ui, sans-serif; background: #0f172a; padding: 48px; border-radius: 24px; max-width: 1000px; margin: 0 auto 40px auto; border: 1px solid #1e293b; box-sizing: border-box; }
  .rag-container-gradient { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 56px 48px; border-radius: 24px; max-width: 1000px; margin: 0 auto; border: 1px solid #334155; box-sizing: border-box; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); }
  .rag-container-shadow { background: #0f172a; border: 1px solid #334155; border-radius: 16px; padding: 48px; max-width: 1000px; margin: 0 auto 40px auto; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5); }
  
  /* Grid Fixes (Forces equal heights in table cells) */
  .rag-grid { width: 100%; border-collapse: separate; border-spacing: 20px; table-layout: fixed; margin: -20px; }
  .rag-grid td { vertical-align: stretch; height: 1px; padding: 0; } /* height:1px forces inner divs to 100% height */
  
  /* Problem Statement Cards */
  .grid-card { background: #1e293b; border: 1px solid #334155; border-radius: 16px; height: 100%; min-height: 100%; display: flex; flex-direction: column; overflow: hidden; }
  .pillar-header { padding: 24px; background: rgba(239, 68, 68, 0.03); border-bottom: 1px solid #334155; }
  .pillar-body { padding: 24px; background: rgba(56, 189, 248, 0.05); flex-grow: 1; }
  
  /* Key Features Cards */
  .feature-card { background: #ffffff; border-radius: 16px; padding: 28px 24px; height: 100%; min-height: 190px; box-sizing: border-box; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2); display: flex; flex-direction: column; }
  
  /* Architecture Layout & Badge Fix */
  .arch-grid { width: 100%; border-collapse: separate; border-spacing: 24px 0; table-layout: fixed; margin: 0 -12px; }
  .arch-grid td { vertical-align: stretch; height: 1px; padding: 0; }
  .arch-card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; height: 100%; margin-top: 15px; box-sizing: border-box; }
  .arch-card-open { background: #0f172a; border: 1px solid #38bdf8; border-radius: 12px; padding: 24px; position: relative; height: 100%; margin-top: 15px; box-sizing: border-box; }
  .arch-badge { position: absolute; top: -12px; right: 24px; background: #38bdf8; color: #0f172a; padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; text-transform: uppercase; }
  
  /* Typography */
  .paradigm-label { color: #38bdf8; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px; font-weight: 700; }
  .card-title { margin: 0 0 10px 0; font-size: 18px; font-weight: 800; color: #0f172a; }
  .section-title { margin: 0 0 16px 0; font-size: 32px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; }
  .section-subtitle { margin: 0 auto; color: #94a3b8; font-size: 16px; line-height: 1.6; max-width: 700px; }
</style>

<p align="center">
  <a href="https://theanalyticmind.com/projects/IntelliQA/">
    <img src="https://img.shields.io/badge/Live_Demo-IntelliQA-38bdf8?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=0f172a" alt="Live Demo: IntelliQA on theanalyticmind.com"/>
  </a>
</p>

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** for grounded question answering over private documents. Core logic ships as a Python wheel so the same package can power a notebook demo today and an API service tomorrow without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

<p align="center">
  <img src="./docs/problem-statement.svg" alt="Why Standard RAG Fails in Production: three pillars covering hallucination, prototype fragility, and vendor lock-in" width="100%"/>
</p>

## TL;DR

IntelliQA is a packaged RAG backend that directly addresses each of the failure modes above. Sessions are **isolated** (no cross-user leakage), capped at **5 uploads** (abuse prevention), content is **deduplicated** at ingestion, and a **scheduled cron job** manages disk space. Generation runs on **Llama 3.3 70B via Groq** against a persistent **ChromaDB** store. Shipped as the `rag_pipeline` Python wheel and powering the live demo at [theanalyticmind.com/projects/IntelliQA](https://theanalyticmind.com/projects/IntelliQA/).

## 🛠️ Tech Stack

<div align="center">

| | |
|:---|:---|
| **LLM & Inference** | ![Llama 3.3 70B][llama] ![Groq LPU][groq] |
| **Embeddings** | ![Hugging Face][hf] ![all-MiniLM-L6-v2][minilm] |
| **RAG Framework** | ![LangChain][langchain] ![ChromaDB][chroma] |
| **Document Parsing** | ![Apache Tika][tika] |
| **Deployment** | ![Docker][docker] ![AWS EC2][ec2] |
| **Packaging** | ![setup.py + wheel][wheel] |
| **Language** | ![Python][python] ![Jupyter][jupyter] |

</div>

[llama]: https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=for-the-badge&logo=meta&logoColor=white
[groq]: https://img.shields.io/badge/Groq_LPU-F55036?style=for-the-badge&logo=lightning&logoColor=white
[hf]: https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black
[minilm]: https://img.shields.io/badge/all--MiniLM--L6--v2-6E6E6E?style=for-the-badge&logo=pytorch&logoColor=white
[langchain]: https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white
[chroma]: https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge&logo=databricks&logoColor=white
[tika]: https://img.shields.io/badge/Apache_Tika-D22128?style=for-the-badge&logo=apache&logoColor=white
[docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[ec2]: https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white
[wheel]: https://img.shields.io/badge/setup.py_%2B_wheel-3776AB?style=for-the-badge&logo=pypi&logoColor=white
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[jupyter]: https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white


## ✨ Key Features

<p align="center">
  <img src="./docs/key-features.svg" alt="Six production-ready features: universal ingestion, session isolation, self-cleaning storage, smart deduplication, abuse-proof uploads, one pip install" width="100%"/>
</p>

## 🧠 System Design Philosophy

**1. Grounded Generation.** LLM runs at `temperature=0` and answers only from retrieved chunks. No speculation.

**2. Multi-Tenant Isolation.** Documents and queries are namespaced per session. Each user retrieves only from their own uploads.

**3. Operational Discipline.** Upload quotas, scheduled cleanup, and deduplication are first-class features, not afterthoughts.

**4. Package-First Distribution.** Core RAG logic ships as a Python wheel. The notebook is a demo. The wheel is the product, and it powers the live portfolio site.

**5. Honest Boundaries.** The system can fail in known ways: retrieval misses, ambiguous source documents, questions outside the indexed content. Design decisions surface these failure modes rather than hide them. `temperature=0` is for reproducibility, not zero hallucination; the prompt instructs the model to say "I don't know" when retrieved context is insufficient.

## 🏗️ How RAG Works in IntelliQA

At a high level, IntelliQA wraps four functional stages into one installable pipeline: a parser converts documents to text, an embedder converts text to vectors, a vector store holds them for similarity search, and an LLM generates answers grounded in the retrieved chunks.

<p align="center">
  <img src="./docs/intelliQA.svg" alt="How RAG works in IntelliQA: parsing, embedding, retrieval, generation" width="100%"/>
</p>

## 🏗️ System Architecture

The real system adds operational layers around the RAG core. Four layers in total:

**Ingestion** &nbsp;·&nbsp; Apache Tika parses multi-format input; deduplication and chunking happen before vectors touch the store.

**Storage** &nbsp;·&nbsp; ChromaDB persists 384-dimensional vectors from `all-MiniLM-L6-v2`, namespaced by session.

**Generation** &nbsp;·&nbsp; Llama 3.3 70B Versatile (served on Groq LPU) generates answers bounded to retrieved context.

**Operations** &nbsp;·&nbsp; Session lifecycle, per-session upload quotas, and a daily cron job for cleanup.

<p align="center">
  <img src="./docs/RAG%20Flow.png"
       alt="IntelliQA architecture: full system with session isolation and lifecycle management"
       style="height: 700px; width: auto;"/>
</p>

## 🧠 Design Decision: Open Stack Over Managed APIs

<p align="center">
  <img src="./docs/design-decision.svg" alt="Architecture Rationale: comparison between managed-API trap and open-stack reality across cost, privacy, rate limits, and portability" width="100%"/>
</p>

## 🛠️ Challenges & Lessons Learned

A few real engineering hurdles surfaced during the IntelliQA build that shaped the current architecture.

### 1. Apache Tika JVM warm-up cost

Tika runs on the JVM, and spawning a fresh JVM per request caused unacceptable cold-start latency on first document upload. The fix was to run a long-lived Tika server on EC2 and proxy requests to it, reducing parse time from seconds to milliseconds. Tika is fast when warm, but slow if treated like a CLI tool.

---

### 2. Disk pressure on shared EC2

The same EC2 instance hosts both the portfolio site and IntelliQA. Without lifecycle management, ChromaDB storage would grow unbounded and Tika temp files would accumulate. This directly led to a cron-based cleanup approach instead of relying on managed storage. Lesson: shared infrastructure requires explicit cleanup design.

---

### 3. Embedding model trade-off

`all-MiniLM-L6-v2` (384 dims) was chosen over larger models like `bge-large-en` (1024 dims) despite lower accuracy. The trade-off was CPU efficiency, no API cost, and a smaller vector store. Performance is sufficient for most Q&A tasks, but worth revisiting if retrieval quality drops.

---

### 4. Hallucination outside retrieved context

Even at temperature=0, the LLM occasionally answered from training data when retrieved context was weak. Updating the system prompt to enforce <span style="color:#ff7f50;"> answer only from the provided context; if the context does not contain the answer, say so </span> reduced this significantly. This reflects the _Honest Boundaries_ design principle.

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
```

The package exposes three modules:

- `rag_pipeline.utils`: parsing, chunking, deduplication
- `rag_pipeline.vector_store`: Chroma setup and indexing
- `rag_pipeline.query_engine`: retrieval, prompt assembly, generation

See `IntelliQA.ipynb` for end-to-end usage examples.

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
| **In progress** | RAG evaluation framework (see below) |

## 📏 Evaluation Approach

The in-progress evaluation framework is being built around four RAG-specific metrics rather than generic LLM benchmarks:

- **Faithfulness** &nbsp;·&nbsp; Does the generated answer follow from the retrieved chunks, or does the model introduce unsupported claims?
- **Answer Relevance** &nbsp;·&nbsp; Does the response actually address the question that was asked?
- **Context Precision** &nbsp;·&nbsp; Of the chunks retrieved, what fraction are actually relevant to the question?
- **Context Recall** &nbsp;·&nbsp; Of the chunks that *should* have been retrieved for a question, how many were?

A held-out evaluation set is being assembled from public RAG benchmarks (covering general knowledge documents) plus synthetic question-answer pairs generated against sample uploads. Once the harness is wired up, results will be tracked over time to catch regressions when components change (different chunk sizes, alternative embedding models, or future reranking experiments).

## 🚫 Out of Scope

A few capabilities are explicitly **not** part of IntelliQA's design. These are deliberate non-goals, not gaps:

- **User authentication.** Sessions are isolated by ID; authentication and user-account management are the responsibility of the calling application. IntelliQA is a backend, not a SaaS product.
- **Long-term knowledge accumulation.** Each session is ephemeral. IntelliQA does not build a persistent knowledge base across users or across time. Documents are scoped to the session that uploaded them and are subject to scheduled cleanup.
- **Document editing or partial updates.** Modifying an indexed document requires re-uploading it. There is no in-place edit path.

## 🚀 Future Improvements

- Cross-encoder reranking on retrieved chunks
- Inline citations linking answers back to source chunks
- Hybrid retrieval (BM25 + dense vector)
- Streaming responses for lower perceived latency

## 💡 System Value

IntelliQA shows that a RAG backend can be **grounded, multi-tenant, operationally sound, and portable** without depending on managed APIs. The production discipline (session isolation, upload quotas, scheduled cleanup, deduplication) is built into the package, not bolted on later.

> Production-grade RAG, distributed as a wheel, powering a live portfolio site today.