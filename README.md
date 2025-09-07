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

**Tech Stack**  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-00A6FF?style=for-the-badge&logo=langchain&logoColor=white) ![Apache Tika](https://img.shields.io/badge/Apache_Tika-ED8B00?style=for-the-badge&logo=apache&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)

---

## 2. SupportIQ: Conversational AI Platform

**Description**  
SupportIQ is a Conversational AI platform that assists users with multi-domain queries, automating tasks like bookings, status updates, and transactions. The project has been a learning journey, progressing from Transformer model fine-tuning and deployment to using Rasa for structured dialogue management, with plans to evolve into an agentic AI system. Each phase has contributed to building a scalable, efficient, and user-friendly support chatbot.

**Tech Stack** 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Hugging Face](https://img.shields.io/badge/HuggingFace-FF6F61?style=for-the-badge&logo=huggingface&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-00A6FF?style=for-the-badge&logo=langchain&logoColor=white) ![Rasa](https://img.shields.io/badge/Rasa-FF4433?style=for-the-badge&logo=rasa&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)

---

### Phase I: Intent Classification Foundation

**Scope:** Create a reliable intent classification model capable of understanding a large variety of user intents (~150 raw intents) to support multi-domain conversational AI.

**Implementation:**  
- Fine-tuned **RoBERTa-large** with **LoRA** for efficient, domain-specific intent classification.  
- Developed scalable training and deployment pipelines using **AWS SageMaker** and **Hugging Face Trainer**.  
- Delivered an initial MVP that accurately classified intents across domains.

**Outcome:** A robust intent classifier capable of generalizing across domains, ready to be extended with response generation.

---

### Phase II: Natural Language Generation for Core Intents

**Scope:** Generate natural, fluent responses for a subset of core intents to enhance user interaction.

**Implementation:**  
- Reduced raw intents from 150 to 20 core intents using a label mapping wrapper for simplified response generation.  
- Fine-tuned and deployed **FLAN-T5** to generate responses for 10 core intents.  
- Implemented cost-efficient serverless inference with **API Gateway** and **AWS Lambda**.

**Challenges:**  
- FLAN-T5 generated fluent responses for straightforward queries but lacked the ability to reliably manage structured, multi-turn dialogues that require collecting and validating specific user inputs (slot filling) or handling complex form-like interactions. 

**Outcome:** Enhanced user engagement via natural responses, but highlighted limitations in handling complex transactional conversations.

---

### Note: 
Phases I and II are parts of the same project and were developed sequentially. They were divided into separate phases to improve efficiency in managing and tracking the development process, not because they represent completely separate projects.

---

### Phase III: Rasa for Dialogue Management and Slot Filling

**Scope:** Enable structured, multi-turn conversations that collect necessary user inputs (e.g., account number, movie choice) to support transactional workflows like bookings, transfers, and calendar events. This enables triggering backend actions based on the gathered information.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Rasa](https://img.shields.io/badge/Rasa-FF4433?style=for-the-badge&logo=rasa&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 
![Gracenote API](https://img.shields.io/badge/Gracenote_API-FF66CC?style=for-the-badge&logo=api&logoColor=ffffff)


**Highlights:**  
- Collects user inputs for movie, showtime, theater, and seat selection.  
- Validates inputs and enforces booking rules.  
- Sends booking confirmation emails automatically.  

[See Detailed Documentation & Diagrams →](rasa/README.md)
---

### Phase IV: Future Plans: Agentic AI for Dynamic Multi-Agent Orchestration

**Scope:**  Develop a system with dynamic orchestration of multiple AI agents, reasoning abilities, and autonomous action execution.

**Implementation:**  
- Planning to explore agentic AI architectures for multi-agent collaboration and advanced task planning.

---
