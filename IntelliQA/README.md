# IntelliQA: Document-Grounded RAG System

## System Overview

IntelliQA is a **production-oriented Retrieval Augmented Generation (RAG) backend** for grounded question answering over private documents. Core logic ships as a Python wheel so the same package can power a notebook demo today and an API service tomorrow without rewrites.

> The driving question: **how do you make LLM answers reliable, multi-tenant, and operationally sustainable on private documents?**

## Problem Statement

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 480" width="1100" height="480">
<defs>
  <linearGradient id="bg-grad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="100%" stop-color="#0b1120"/>
  </linearGradient>
</defs>
<rect width="1100" height="480" rx="24" fill="url(#bg-grad)"/>
<rect width="1100" height="480" rx="24" fill="none" stroke="#1e293b" stroke-width="1"/>

<!-- Header -->
<text x="550.0" y="78" text-anchor="middle" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="30" font-weight="800" letter-spacing="-0.5">Why Standard RAG Fails in Production</text>
<text x="550.0" y="112" text-anchor="middle" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15">Transitioning from notebook prototypes to reliable, multi-tenant services exposes fundamental flaws</text>
<text x="550.0" y="132" text-anchor="middle" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15">in the standard AI stack.</text>

<!-- 3 cards -->

<defs>
  <clipPath id="clip-44.0-168">
    <rect x="44.0" y="168" width="320" height="270" rx="16"/>
  </clipPath>
</defs>
<g clip-path="url(#clip-44.0-168)">
  <!-- card base -->
  <rect x="44.0" y="168" width="320" height="270" fill="#1e293b"/>
  <!-- problem section (top) with subtle red tint -->
  <rect x="44.0" y="168" width="320" height="135.0" fill="#2a1d22"/>
  <!-- paradigm section (bottom) with subtle cyan tint -->
  <rect x="44.0" y="303.0" width="320" height="135.0" fill="#1a2436"/>
  <!-- divider line -->
  <line x1="44.0" y1="303.0" x2="364.0" y2="303.0" stroke="#334155" stroke-width="1"/>
</g>
<!-- card border on top -->
<rect x="44.0" y="168" width="320" height="270" rx="16" fill="none" stroke="#334155" stroke-width="1"/>

<!-- icon -->
<g transform="translate(66.0,190) scale(0.8333)" fill="none" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="3.5"/><circle cx="8.5" cy="8.5" r="1.4" fill="#ef4444"/><circle cx="15.5" cy="8.5" r="1.4" fill="#ef4444"/><circle cx="12" cy="15.5" r="1.4" fill="#ef4444"/><line x1="8.5" y1="8.5" x2="15.5" y2="8.5"/><line x1="9.5" y1="9.5" x2="11.5" y2="14.5"/><line x1="14.5" y1="9.5" x2="12.5" y2="14.5"/></g>
<!-- title -->
<text x="96.0" y="205" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15" font-weight="700">The Knowledge Gap</text>
<!-- problem description -->
<text x="66.0" y="238" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="66.0" dy="0">Models hallucinate when questions reach</tspan>
  <tspan x="66.0" dy="18">beyond their fixed training data.</tspan>
</text>

<!-- paradigm label -->
<text x="66.0" y="335.0" fill="#38bdf8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="1.5">INTELLIQA PARADIGM</text>
<!-- paradigm text -->
<text x="66.0" y="361.0" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="66.0" dy="0">Strictly bounds generation to your</tspan>
  <tspan x="66.0" dy="18">retrieved document context only.</tspan>
</text>

<defs>
  <clipPath id="clip-390.0-168">
    <rect x="390.0" y="168" width="320" height="270" rx="16"/>
  </clipPath>
</defs>
<g clip-path="url(#clip-390.0-168)">
  <!-- card base -->
  <rect x="390.0" y="168" width="320" height="270" fill="#1e293b"/>
  <!-- problem section (top) with subtle red tint -->
  <rect x="390.0" y="168" width="320" height="135.0" fill="#2a1d22"/>
  <!-- paradigm section (bottom) with subtle cyan tint -->
  <rect x="390.0" y="303.0" width="320" height="135.0" fill="#1a2436"/>
  <!-- divider line -->
  <line x1="390.0" y1="303.0" x2="710.0" y2="303.0" stroke="#334155" stroke-width="1"/>
</g>
<!-- card border on top -->
<rect x="390.0" y="168" width="320" height="270" rx="16" fill="none" stroke="#334155" stroke-width="1"/>

<!-- icon -->
<g transform="translate(412.0,190) scale(0.8333)" fill="none" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/><circle cx="6.5" cy="7" r="0.4" fill="#ef4444"/><circle cx="6.5" cy="17" r="0.4" fill="#ef4444"/><path d="M14 6 L11 11 L13 11 L10 13"/></g>
<!-- title -->
<text x="442.0" y="205" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15" font-weight="700">The Prototype Trap</text>
<!-- problem description -->
<text x="412.0" y="238" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="412.0" dy="0">Notebook scripts fail under multi-tenant</tspan>
  <tspan x="412.0" dy="18">load and lack operational safety.</tspan>
</text>

<!-- paradigm label -->
<text x="412.0" y="335.0" fill="#38bdf8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="1.5">INTELLIQA PARADIGM</text>
<!-- paradigm text -->
<text x="412.0" y="361.0" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="412.0" dy="0">Ships as a robust, isolated Python wheel,</tspan>
  <tspan x="412.0" dy="18">production-ready by design.</tspan>
</text>

<defs>
  <clipPath id="clip-736.0-168">
    <rect x="736.0" y="168" width="320" height="270" rx="16"/>
  </clipPath>
</defs>
<g clip-path="url(#clip-736.0-168)">
  <!-- card base -->
  <rect x="736.0" y="168" width="320" height="270" fill="#1e293b"/>
  <!-- problem section (top) with subtle red tint -->
  <rect x="736.0" y="168" width="320" height="135.0" fill="#2a1d22"/>
  <!-- paradigm section (bottom) with subtle cyan tint -->
  <rect x="736.0" y="303.0" width="320" height="135.0" fill="#1a2436"/>
  <!-- divider line -->
  <line x1="736.0" y1="303.0" x2="1056.0" y2="303.0" stroke="#334155" stroke-width="1"/>
</g>
<!-- card border on top -->
<rect x="736.0" y="168" width="320" height="270" rx="16" fill="none" stroke="#334155" stroke-width="1"/>

<!-- icon -->
<g transform="translate(758.0,190) scale(0.8333)" fill="none" stroke="#ef4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="9" cy="9" rx="6.5" ry="2.5"/><path d="M2.5 9 v3.5 c0 1.4 2.9 2.5 6.5 2.5 s6.5-1.1 6.5-2.5 v-3.5"/><ellipse cx="15" cy="15" rx="6.5" ry="2.5"/><path d="M8.5 15 v3.5 c0 1.4 2.9 2.5 6.5 2.5 s6.5-1.1 6.5-2.5 v-3.5"/></g>
<!-- title -->
<text x="788.0" y="205" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15" font-weight="700">The API Tax</text>
<!-- problem description -->
<text x="758.0" y="238" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="758.0" dy="0">Proprietary embedding APIs scale costs</tspan>
  <tspan x="758.0" dy="18">exponentially as documents grow.</tspan>
</text>

<!-- paradigm label -->
<text x="758.0" y="335.0" fill="#38bdf8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="1.5">INTELLIQA PARADIGM</text>
<!-- paradigm text -->
<text x="758.0" y="361.0" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12.5">
  <tspan x="758.0" dy="0">Leverages local open-weight models,</tspan>
  <tspan x="758.0" dy="18">dropping bulk ingestion costs to zero.</tspan>
</text>

</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 620" width="1100" height="620">
<defs>
  <linearGradient id="feat-grad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0f172a"/>
    <stop offset="100%" stop-color="#1e293b"/>
  </linearGradient>
</defs>
<rect width="1100" height="620" rx="24" fill="url(#feat-grad)"/>
<rect width="1100" height="620" rx="24" fill="none" stroke="#334155" stroke-width="1"/>

<!-- pill -->
<rect x="475.0" y="58" width="150" height="28" rx="14" fill="rgba(56, 189, 248, 0.12)" stroke="#38bdf8" stroke-opacity="0.4" stroke-width="1"/>
<text x="550.0" y="76" text-anchor="middle" fill="#38bdf8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="11" font-weight="700" letter-spacing="2">PRODUCTION-READY</text>

<!-- title -->
<text x="550.0" y="135" text-anchor="middle" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="36" font-weight="800" letter-spacing="-0.5">Key Features</text>
<text x="550.0" y="175" text-anchor="middle" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="15">Six engineered capabilities that take RAG from prototype to production.</text>

<!-- 6 cards in 2x3 grid -->

<rect x="44.0" y="220" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-44.0-220">
    <rect x="44.0" y="220" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="44.0" y="220" width="320" height="4" fill="#D22128" clip-path="url(#stripe-44.0-220)"/>
<!-- icon -->
<g transform="translate(68.0,250) scale(1.5000)" fill="none" stroke="#D22128" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15.5 2H8.6c-.4 0-.8.2-1.1.5-.3.3-.5.7-.5 1.1v12.8c0 .4.2.8.5 1.1.3.3.7.5 1.1.5h9.8c.4 0 .8-.2 1.1-.5.3-.3.5-.7.5-1.1V6.5L15.5 2z"/><polyline points="15,2 15,7 20,7"/><path d="M4 7v13c0 .5.2 1 .6 1.4.4.4.9.6 1.4.6h10"/></g>
<!-- title -->
<text x="68.0" y="314" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">Universal Ingestion</text>
<!-- description -->
<text x="68.0" y="340" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="68.0" dy="0">PDF, DOCX, HTML, TXT, RTF, ODT via</tspan><tspan x="68.0" dy="17">Apache Tika. One parsing layer.</tspan>
</text>

<rect x="390.0" y="220" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-390.0-220">
    <rect x="390.0" y="220" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="390.0" y="220" width="320" height="4" fill="#2563EB" clip-path="url(#stripe-390.0-220)"/>
<!-- icon -->
<g transform="translate(414.0,250) scale(1.5000)" fill="none" stroke="#2563EB" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5.5" y="11" width="13" height="9" rx="1.5"/><path d="M8.5 11V8a3.5 3.5 0 0 1 7 0v3"/><circle cx="12" cy="14.5" r="1.2"/><path d="M12 15.7v1.6"/></g>
<!-- title -->
<text x="414.0" y="314" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">Session Isolation</text>
<!-- description -->
<text x="414.0" y="340" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="414.0" dy="0">Per-session ChromaDB namespacing.</tspan><tspan x="414.0" dy="17">Zero cross-user data leakage.</tspan>
</text>

<rect x="736.0" y="220" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-736.0-220">
    <rect x="736.0" y="220" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="736.0" y="220" width="320" height="4" fill="#10B981" clip-path="url(#stripe-736.0-220)"/>
<!-- icon -->
<g transform="translate(760.0,250) scale(1.5000)" fill="none" stroke="#10B981" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16"/><path d="M18 7l-1 12.5a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2L6 7"/><path d="M9.5 7V5a1.5 1.5 0 0 1 1.5-1.5h2A1.5 1.5 0 0 1 14.5 5v2"/><path d="M14 12 L17 14.5 L14 17" /><path d="M17 14.5 H12" /></g>
<!-- title -->
<text x="760.0" y="314" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">Self-Cleaning Storage</text>
<!-- description -->
<text x="760.0" y="340" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="760.0" dy="0">Daily cron job purges expired</tspan><tspan x="760.0" dy="17">sessions and orphaned vectors.</tspan>
</text>

<rect x="44.0" y="409" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-44.0-409">
    <rect x="44.0" y="409" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="44.0" y="409" width="320" height="4" fill="#7C3AED" clip-path="url(#stripe-44.0-409)"/>
<!-- icon -->
<g transform="translate(68.0,439) scale(1.5000)" fill="none" stroke="#7C3AED" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="8" width="13" height="13" rx="2"/><path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4H4.5A1.5 1.5 0 0 0 3 5.5v10A1.5 1.5 0 0 0 4.5 17H8"/><line x1="3" y1="3" x2="21" y2="21" stroke-width="2.2"/></g>
<!-- title -->
<text x="68.0" y="503" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">Smart Deduplication</text>
<!-- description -->
<text x="68.0" y="529" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="68.0" dy="0">Hash-based ingestion checks.</tspan><tspan x="68.0" dy="17">Identical content indexed once.</tspan>
</text>

<rect x="390.0" y="409" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-390.0-409">
    <rect x="390.0" y="409" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="390.0" y="409" width="320" height="4" fill="#F59E0B" clip-path="url(#stripe-390.0-409)"/>
<!-- icon -->
<g transform="translate(414.0,439) scale(1.5000)" fill="none" stroke="#F59E0B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 13 L16 9" stroke-width="2.4"/><circle cx="12" cy="13" r="1.2" fill="#F59E0B"/><line x1="12" y1="6" x2="12" y2="7"/><line x1="19" y1="13" x2="18" y2="13"/><line x1="6" y1="13" x2="5" y2="13"/></g>
<!-- title -->
<text x="414.0" y="503" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">Abuse-Proof Uploads</text>
<!-- description -->
<text x="414.0" y="529" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="414.0" dy="0">Hard cap of 5 documents per session.</tspan><tspan x="414.0" dy="17">Storage exhaustion blocked.</tspan>
</text>

<rect x="736.0" y="409" width="320" height="165" rx="14" fill="#ffffff"/>
<!-- top color stripe (rounded only on top corners via clip) -->
<defs>
  <clipPath id="stripe-736.0-409">
    <rect x="736.0" y="409" width="320" height="18" rx="14"/>
  </clipPath>
</defs>
<rect x="736.0" y="409" width="320" height="4" fill="#3776AB" clip-path="url(#stripe-736.0-409)"/>
<!-- icon -->
<g transform="translate(760.0,439) scale(1.5000)"><path fill="#3776AB" d="M11.6 2c-4.6 0-4.3 2-4.3 2v2.1h4.4v.6H5.5S2.6 6.4 2.6 11s2.5 4.5 2.5 4.5h1.5v-2.2s-.1-2.5 2.4-2.5h4.4s2.4 0 2.4-2.3V4.3S15.8 2 11.6 2zm-2.4 1.4c.4 0 .8.3.8.8s-.4.8-.8.8-.8-.3-.8-.8.3-.8.8-.8z"/><path fill="#3776AB" opacity="0.7" d="M12.4 22c4.6 0 4.3-2 4.3-2v-2.1h-4.4v-.6h6.2s2.9.3 2.9-4.3-2.5-4.5-2.5-4.5h-1.5v2.2s.1 2.5-2.4 2.5h-4.4s-2.4 0-2.4 2.3v4.2S8.2 22 12.4 22zm2.4-1.4c-.4 0-.8-.3-.8-.8s.4-.8.8-.8.8.3.8.8-.3.8-.8.8z"/></g>
<!-- title -->
<text x="760.0" y="503" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="17" font-weight="800">One Pip Install</text>
<!-- description -->
<text x="760.0" y="529" fill="#475569" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">
  <tspan x="760.0" dy="0">Shipped as rag_pipeline-3.0.</tspan><tspan x="760.0" dy="17">Drop into any backend.</tspan>
</text>

</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 540" width="1100" height="540">
<rect width="1100" height="540" rx="20" fill="#0f172a" stroke="#334155" stroke-width="1"/>

<!-- Header -->
<g transform="translate(44,44) scale(1.2500)" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="6" r="3"/><path d="M18 9v3a6 6 0 0 1-6 6h-3"/></g>
<text x="84" y="72" fill="#ffffff" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="26" font-weight="800" letter-spacing="-0.3">Architecture Rationale</text>
<text x="44" y="108" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="14.5">Why bypass managed services like OpenAI and Pinecone? Prototype economics rarely survive</text>
<text x="44" y="128" fill="#94a3b8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="14.5">production scale. We designed IntelliQA to maintain inference quality without compounding API costs.</text>

<!-- divider -->
<line x1="44" y1="152" x2="1056" y2="152" stroke="#1e293b" stroke-width="1"/>

<!-- 2 cards -->

<rect x="26.0" y="175" width="510" height="320" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1"/>

<text x="50.0" y="217" fill="#fca5a5" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5">THE MANAGED TRAP</text>
<circle cx="55.0" cy="255" r="2.5" fill="#fca5a5"/><text x="68.0" y="259" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Recurring Costs:</tspan><tspan fill="#cbd5e1"> Per-token embedding</tspan></text><text x="68.0" y="277" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">billing erodes margins at scale.</text><circle cx="55.0" cy="299" r="2.5" fill="#fca5a5"/><text x="68.0" y="303" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Data Privacy:</tspan><tspan fill="#cbd5e1"> Documents leave your</tspan></text><text x="68.0" y="321" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">environment for third-party APIs.</text><circle cx="55.0" cy="343" r="2.5" fill="#fca5a5"/><text x="68.0" y="347" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Rate Limits:</tspan><tspan fill="#cbd5e1"> Bulk ingestion hits</tspan></text><text x="68.0" y="365" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">throttling caps instantly.</text><circle cx="55.0" cy="387" r="2.5" fill="#fca5a5"/><text x="68.0" y="391" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Vendor Lock-in:</tspan><tspan fill="#cbd5e1"> Vector store tightly</tspan></text><text x="68.0" y="409" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">coupled to one provider's model.</text>


<rect x="564.0" y="175" width="510" height="320" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>

<rect x="964.0" y="163" width="92" height="22" rx="11" fill="#38bdf8"/>
<text x="1010.0" y="178" text-anchor="middle" fill="#0f172a" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="10" font-weight="800" letter-spacing="1">OUR STACK</text>

<text x="588.0" y="217" fill="#38bdf8" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5">THE OPEN REALITY</text>
<circle cx="593.0" cy="255" r="2.5" fill="#38bdf8"/><text x="606.0" y="259" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Zero-Cost Embeddings:</tspan><tspan fill="#cbd5e1"> Local</tspan></text><text x="606.0" y="277" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">all-MiniLM-L6-v2 makes ingestion free.</text><circle cx="593.0" cy="299" r="2.5" fill="#38bdf8"/><text x="606.0" y="303" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Sub-Second Inference:</tspan><tspan fill="#cbd5e1"> Groq</tspan></text><text x="606.0" y="321" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">LPU latency rivals managed-LLM APIs.</text><circle cx="593.0" cy="343" r="2.5" fill="#38bdf8"/><text x="606.0" y="347" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Data Sovereignty:</tspan><tspan fill="#cbd5e1"> ChromaDB on-disk;</tspan></text><text x="606.0" y="365" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">vectors never leave your environment.</text><circle cx="593.0" cy="387" r="2.5" fill="#38bdf8"/><text x="606.0" y="391" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13"><tspan fill="#ffffff" font-weight="700">Portable Wheel:</tspan><tspan fill="#cbd5e1"> Entire stack</tspan></text><text x="606.0" y="409" fill="#cbd5e1" font-family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif" font-size="13">ships in one Python package.</text>

</svg>

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