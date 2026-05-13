# 🧠 GenAI Portfolio

> A curated collection of production-oriented Generative AI projects spanning **RAG**, **LLM fine-tuning**, **conversational AI**, and **agentic systems**.

Each project lives in its own folder with a dedicated README covering architecture, implementation choices, and trade-offs. The main goals across this portfolio: production deployment, hybrid (deterministic + LLM) design, and honest documentation of what worked and what didn’t.

<p align="center">
  <img 
    src="https://github-readme-stats-sigma-five.vercel.app/api?username=abhijitdeshpande83&show_icons=true&hide_border=true&border_radius=12&bg_color=050a14&title_color=38bdf8&icon_color=38bdf8&text_color=ffffff&count_private=true" 
    alt="Abhijit's GitHub Stats" 
    height="171" 
    style="vertical-align: middle;"
  />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img 
    src="https://github-readme-streak-stats-eight.vercel.app/?user=abhijitdeshpande83&hide_border=true&border_radius=12&background=050a14&stroke=1e293b&ring=38bdf8&fire=ff6600&currStreakLabel=ffffff&sideLabels=ffffff&dates=94a3b8&currStreakNum=ffffff&sideNums=ffffff" 
    alt="GitHub Streak" 
    height="170" 
    style="vertical-align: middle;"
  />
</p>

---

## 🚀 Featured Projects

### 🤖 Agentic AI

#### 🛡️ AURA: Hybrid Conversational AI Support System
A production-oriented customer support system that combines a deterministic ML intent router (DeBERTa) with LangGraph-orchestrated workflows and bounded LLM reasoning (Groq). Designed to solve a real production tension: balancing LLM flexibility with deterministic control.

**Highlights**
- **Hybrid architecture:** DeBERTa for intent routing, Groq LLM scoped to bounded reasoning only (Inquiry Agent), LangGraph for traceable workflow execution
- Three execution paths: Inquiry Agent (LLM + tools), Complaint Workflow (ticket creation), Retention Workflow (churn mitigation)
- **89% intent classification accuracy, sub-800ms p95 latency**
- Documented design decision: explicitly rejected a pure-LLM orchestration approach after observing tool-selection loops and inconsistent workflow behavior
- Deployed via AWS Lambda + API Gateway + ECR (containerized)

<p>
  <img src="https://img.shields.io/badge/LangGraph-4B0082?logo=graphql&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq%20LLM-00C7B7?logo=lightning&logoColor=white" />
  <img src="https://img.shields.io/badge/DeBERTa-0A66C2?logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?logo=awslambda&logoColor=white" />
  <img src="https://img.shields.io/badge/API%20Gateway-232F3E?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/ECR-FF9900?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
</p>

📂 [Full Documentation](./Agentic%20User%20Resolution%20Assistant%20(AURA)/README.md)

---

#### 🌍 ATLAS: Agentic Tool-Enabled Web Assistant
A LangGraph-powered autonomous agent that performs real-time web research using Groq LLM and Tavily Search, with session-based memory. *(Named after Atlas the Titan: holding up a world of real-time information.)*

**Highlights**
- Dynamic tool orchestration: the agent decides when to respond directly vs invoke external tools
- Session memory via LangGraph `MemorySaver` for contextual multi-turn conversations
- Modular separation of agent definition from execution via a `run_agent` interface
- Deployed serverlessly on AWS Lambda + API Gateway, with CORS handled by routing requests through a Django backend proxy
- Containerized with Docker

<p>
  <img src="https://img.shields.io/badge/LangGraph-000000?logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq%20LLM-F55036?logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/Tavily%20Search-1E90FF?logo=googlechrome&logoColor=white" />
  <img src="https://img.shields.io/badge/MemorySaver-000000?logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?logo=awslambda&logoColor=white" />
  <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
</p>

📂 [Full Documentation](./Agentic%20Tool-Enabled%20Web%20Assistant%20(ATLAS)/README.md)

---

### 🎯 LLM Fine-Tuning

#### 🧠 INTELLA: Intent Classification with LoRA-Fine-Tuned Language Assistant
A two-phase fine-tuning project for multi-domain conversational AI, demonstrating end-to-end LLM customization from intent classification through natural response generation.

**Phase I: Intent Classification Foundation**
- Fine-tuned **RoBERTa-large with LoRA** to classify ~150 user intents across multiple domains
- Built scalable training and deployment pipelines on **AWS SageMaker + Hugging Face Trainer**

**Phase II: Natural Language Generation for Core Intents**
- Reduced 150 raw intents → 20 core intents via a custom label-mapping wrapper
- Fine-tuned **FLAN-T5** to generate natural responses for 10 core intents
- Cost-efficient serverless inference via **AWS Lambda + API Gateway**

> **Honest limitation surfaced:** FLAN-T5 handles single-turn queries fluently but does not reliably manage structured multi-turn dialogues requiring slot filling. This motivated the Rasa project below.

<p>
  <img src="https://img.shields.io/badge/RoBERTa-701516?logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/FLAN--T5-0F0F0F?logo=huggingface&logoColor=white" />
  <img src="https://img.shields.io/badge/LoRA-FFD21E?logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/SageMaker-FF9900?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?logo=awslambda&logoColor=white" />
  <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
</p>

📂 [Full Documentation](./Intent%20Classification%20with%20LoRA-Fine-Tuned%20Language%20Assistant(INTELLA)/README.md)

---

### 📚 Retrieval-Augmented Generation

#### 🔍 IntelliQA: RAG-based Document Q&A
A conversational Q&A system over uploaded documents (PDF, DOCX, TXT, and more) built on a containerized, production-deployed RAG pipeline.

**Highlights**
- Document parsing and embedding via **LangChain + Apache Tika**
- Multi-format support: PDF, DOCX, TXT, and additional file types
- Operational guardrails: duplicate detection on upload, 5-file session cap, daily cleanup cron for storage hygiene
- Modular Dockerized deployment package
- Deployed on AWS for production usage

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-00A6FF?logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Apache%20Tika-ED8B00?logo=apache&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?logo=amazonaws&logoColor=white" />
</p>

📂 [Project Folder](./IntelliQA/) *(detailed README in progress)*

---

### 💬 Dialogue Management

#### 🎬 Rasa: Movie Booking Chatbot
A deterministic, slot-filling chatbot for end-to-end movie booking, directly addressing the multi-turn dialogue limitation identified in INTELLA Phase II.

**Highlights**
- Multi-turn dialogue collecting ZIP code, movie, showtime, theater, and seat selection
- Form validation and business-rule enforcement (e.g. one seat per show, no past or ongoing dates)
- **Gracenote API** integration for real-time movie listings, theaters, and showtimes
- Automated HTML email confirmations via Python’s `smtplib`
- Docker-based training and deployment, handling MacOS → Linux model compatibility issues

<p>
  <img src="https://img.shields.io/badge/Rasa-FF3B30?logo=rasa&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Gracenote%20API-8A2BE2?logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
</p>

📂 [Full Documentation](./rasa/README.md)

---

### 📝 Additional Projects

#### ✂️ TextSummarization
NLP-based text summarization project. *(Documentation in progress.)*

📂 [Project Folder](./TextSummarization/)

---

## 🗂 Repository Structure

```
GenAI/
├── Agentic Tool-Enabled Web Assistant (ATLAS)/      # LangGraph + Groq + Tavily research agent
├── Agentic User Resolution Assistant (AURA)/        # Hybrid production support system
├── Intent Classification with LoRA-Fine-Tuned       # RoBERTa + LoRA + FLAN-T5 fine-tuning
│   Language Assistant(INTELLA)/
├── IntelliQA/                                       # RAG-based document Q&A
├── TextSummarization/                               # NLP text summarization (WIP)
├── rasa/                                            # Deterministic dialogue management
└── README.md                                        # You are here
```

---

## 🧰 Skills Demonstrated

| **Area** | **Tools & Techniques** |
| --- | --- |
| **LLMs & Fine-Tuning** | RoBERTa, DeBERTa, FLAN-T5, LoRA / PEFT, Hugging Face Transformers |
| **Agentic Systems** | LangGraph, LangChain, Groq LLM, Tavily Search, MemorySaver checkpointing |
| **RAG** | LangChain, Apache Tika, vector retrieval, multi-format document parsing |
| **Dialogue Management** | Rasa (slot filling, form validation, business-rule enforcement) |
| **Cloud & Deployment** | AWS SageMaker, Lambda, API Gateway, ECR, Docker, serverless inference |
| **Backend & Data** | Python, Django, Supabase |
| **System Design** | Hybrid ML + LLM architectures, deterministic-first routing, graph-based orchestration |

---

## 👤 About

I build practical GenAI systems with a focus on production deployment, hybrid architectures (deterministic + LLM), and transparent trade-off documentation. This portfolio reflects a progression from foundational RAG and fine-tuning toward agentic and hybrid system design.

📫 **Connect:** [LinkedIn](https://www.linkedin.com/in/abhijit-deshpande/) • [Website](https://www.theanalyticmind.com/) • [GitHub](https://github.com/abhijitdeshpande83)
