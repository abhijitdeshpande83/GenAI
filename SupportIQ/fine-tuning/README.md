# Fine-Tuning Details

## Phase I: Intent Classification Foundation
**Scope:** Create a reliable intent classification model capable of understanding a large variety of user intents (~150 raw intents) to support multi-domain conversational AI.

## 🛠 Tech Stack  

<table>
  <tr>
    <td><strong>ML Models</strong></td>
    <td>
      <img src="https://img.shields.io/badge/RoBERTa-701516?logo=pytorch&logoColor=white" alt="RoBERTa">
      <img src="https://img.shields.io/badge/FLAN--T5-0F0F0F?logo=huggingface&logoColor=white" alt="FLAN-T5">
    </td>
  </tr>
  <tr>
    <td><strong>Cloud / Deployment</strong></td>
    <td>
      <img src="https://img.shields.io/badge/SageMaker-FF9900?logo=amazonaws&logoColor=white" alt="SageMaker">
      <img src="https://img.shields.io/badge/Lambda-FF9900?logo=awslambda&logoColor=white" alt="Lambda">
      <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white" alt="API Gateway">
      <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker">
    </td>
  </tr>
  <tr>
    <td><strong>Programming Language</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
    </td>
  </tr>
</table>


**Implementation:**
- Fine-tuned RoBERTa-large with LoRA for efficient, domain-specific intent classification.
- Developed scalable training and deployment pipelines using AWS SageMaker and Hugging Face Trainer.
- Delivered an initial MVP that accurately classified intents across domains.

**Outcome:**  
A robust intent classifier capable of generalizing across domains, ready to be extended with response generation.

---

## Phase II: Natural Language Generation for Core Intents
**Scope:** Generate natural, fluent responses for a subset of core intents to enhance user interaction.

**Implementation:**
- Reduced raw intents from 150 to 20 core intents using a label mapping wrapper for simplified response generation.
- Fine-tuned and deployed FLAN-T5 to generate responses for 10 core intents.
- Implemented cost-efficient serverless inference with API Gateway and AWS Lambda.

**Challenges:**
- FLAN-T5 generated fluent responses for straightforward queries but lacked the ability to reliably manage structured, multi-turn dialogues requiring slot filling or complex form-like interactions.

**Outcome:**  
Enhanced user engagement via natural responses, but highlighted limitations in handling complex transactional conversations.

---

**Note:**  
Phases I and II are parts of the same project and were developed sequentially. They were divided into separate phases to improve efficiency in managing and tracking the development process, not because they represent completely separate projects.
