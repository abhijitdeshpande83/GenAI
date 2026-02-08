# NLP & GenAI Projects

<table>
  <tr>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username=abhijitdeshpande83&show_icons=true&theme=tokyonight&count_private=true" />
    </td>
    <td>
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=abhijitdeshpande83&theme=tokyonight" />
    </td>
  </tr>
</table>



Welcome to my **NLP & Generative AI** portfolio repository, showcasing cutting-edge projects ranging from **Retrieval-Augmented Generation (RAG)** systems to advanced **conversational AI platforms** leveraging fine-tuned LLMs and orchestrated dialogue management.

---

## 📂 Project Overview

---
## 1. IntelliQA: RAG-based Document Q&A

**Description**  
A Retrieval-Augmented Generation system enabling conversational Q&A over diverse uploaded documents.

**Key Features**  
- Document parsing & embedding using **LangChain** + **Apache Tika**  
- Detects duplicate files during upload to prevent redundant processing
- Limits users to uploading a maximum of 5 files per session for system efficiency
- Implements a daily cleanup cron job that removes all files uploaded within the past day to save storage space
- Multi-format support (PDF, DOCX, TXT, etc.)  
- Dockerized modular deployment package  
- Deployed on AWS for production-grade usage

## 🛠 Tech Stack  

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white" alt="Django" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/LangChain-00A6FF?logo=langchain&logoColor=white" alt="LangChain" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Apache_Tika-ED8B00?logo=apache&logoColor=white" alt="Apache Tika" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/AWS-232F3E?logo=amazonaws&logoColor=white" alt="AWS" />
</p>

---

## 2. SupportIQ: Conversational AI Platform

## LLM Fine-Tuning Project Overview

This repository includes fine-tuning efforts to build robust conversational AI capabilities, covering:

- **Phase I: Intent Classification** - Fine-tuned RoBERTa-large with LoRA to classify ~150 user intents across multiple domains.
- **Phase II: Response Generation** - Fine-tuned FLAN-T5 to generate natural responses for a subset of core intents and enable user-friendly conversational interactions.

## 🛠 Tech Stack  
<p>
  <img src="https://img.shields.io/badge/RoBERTa-701516?logo=pytorch&logoColor=white" alt="RoBERTa" />
  <img src="https://img.shields.io/badge/FLAN--T5-0F0F0F?logo=huggingface&logoColor=white" alt="FLAN-T5" />
  <img src="https://img.shields.io/badge/SageMaker-FF9900?logo=amazonaws&logoColor=white" alt="SageMaker" />
  <img src="https://img.shields.io/badge/Lambda-FF9900?logo=awslambda&logoColor=white" alt="Lambda" />
  <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white" alt="API Gateway" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
</p>

For detailed implementation, training, and deployment notes, see the dedicated [Fine-Tuning Details](SupportIQ/fine-tuning/README.md) file.

---

### Phase III: Rasa for Dialogue Management and Slot Filling

**Scope:** Enable structured, multi-turn conversations that collect necessary user inputs (e.g., account number, movie choice) to support transactional workflows like bookings, transfers, and calendar events. This enables triggering backend actions based on the gathered information.

## 🛠 Tech Stack  

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Rasa-FF4433?logo=rasa&logoColor=white" alt="Rasa" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?logo=supabase&logoColor=white" alt="Supabase" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker" style="margin-right:6px;" />
  <img src="https://img.shields.io/badge/Gracenote_API-FF66CC?logo=api&logoColor=white" alt="Gracenote API" />
</p>

**Highlights:**  
- Collects user inputs for movie, showtime, theater, and seat selection.  
- Validates inputs and enforces booking rules.  
- Sends booking confirmation emails automatically. 

[👉 See Detailed Documentation & Diagrams](SupportIQ/rasa/README.md)
---

### Phase IV: Future Plans: Agentic AI for Dynamic Multi-Agent Orchestration

**Scope:**  Develop a system with dynamic orchestration of multiple AI agents, reasoning abilities, and autonomous action execution.

**Implementation:**  
- Planning to explore agentic AI architectures for multi-agent collaboration and advanced task planning.

---
