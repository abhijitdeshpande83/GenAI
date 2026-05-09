# AURA: Hybrid Conversational AI Support System

## System Overview

AURA is a **production-oriented hybrid GenAI system** designed for automated customer support using a combination of:

- deterministic intent routing (ML classifier)
- graph-based orchestration
- LLM-based tool-augmented reasoning

The system is built to explore a key production challenge in modern GenAI systems:

> How to balance **deterministic control** with **LLM flexibility** without sacrificing reliability.

---

## Problem Statement

Most customer support systems today fail in production due to:

- over-reliance on static FAQ systems  
- uncontrolled LLM behavior (hallucination + inconsistency)  
- lack of intent-aware routing  
- poor separation between retrieval, reasoning, and workflow execution  

This leads to:
- incorrect responses  
- inefficient escalation pipelines  
- poor customer retention handling  

AURA is designed to address these issues using a **controlled hybrid architecture**.

---

## 🧠 System Design Philosophy

AURA follows a **control-first GenAI architecture**:

### 1. Deterministic First Principle
All user inputs are first routed through a **DeBERTa-based intent classifier**, ensuring predictable system behavior before any LLM is invoked.

### 2. LLMs as Scoped Executors
LLMs are used only inside bounded contexts (Inquiry Agent), not for global orchestration decisions.

### 3. Graph-Based Execution Control
All workflows are executed using a **LangGraph state machine**, ensuring structured and traceable execution paths.

---

## 🏗️ High-Level Architecture

The system follows a **three-layer design pattern**:

### 1. Control Layer (Routing)
- Intent classification using DeBERTa  
- Routes request into predefined system paths  

### 2. Execution Layer (Workflows)
- Complaint handling (ticket generation)  
- Retention handling (churn mitigation logic)  

### 3. Reasoning Layer (LLM Agent)
- Inquiry agent powered by Groq LLM  
- Tool-based dynamic information retrieval  

---

## 🔄 Core Execution Flow

1. User sends input via chat interface  
2. Intent classifier (DeBERTa) determines category:
   - Query  
   - Complaint  
   - Churn Risk  
3. LangGraph routes request to appropriate node:
   - Inquiry Agent → LLM + tools  
   - Complaint Workflow → ticket creation  
   - Retention Workflow → churn mitigation logic  
4. Response is generated and returned to user  

---

## 🧠 Design Decision: Why Hybrid Instead of Pure LLM

A fully LLM-driven orchestration approach was initially tested but failed due to:

### Failure Modes Observed:
- inconsistent tool selection  
- execution loops between tools  
- non-deterministic workflow behavior  
- poor production stability  

### Final Decision:
A **hybrid architecture was introduced**:

- ML model handles routing (DeBERTa)  
- LLM is restricted to bounded reasoning (Inquiry only)  
- workflows are deterministic and traceable  

This improved:
- reliability  
- latency stability  
- production predictability  

---

## 🧩 System Components

### 🔹 Intent Router
Model: DeBERTa  
Function: classifies user intent into structured categories  

---

### 🔹 Orchestration Engine
Framework: LangGraph  
Function: manages state transitions across workflows  

---

### 🔹 LLM Layer
Model: Groq LLM  
Function: tool-augmented reasoning for inquiry handling  

---

### 🔹 Infrastructure Layer
- AWS Lambda  
- API Gateway  
- ECR  
- Docker  

---

## 🛠 Tech Stack  

<table>
  <tr>
    <td><strong>LLM & Agent Frameworks</strong></td>
    <td>
      <img src="https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white" alt="LangChain">
      <img src="https://img.shields.io/badge/LangGraph-4B0082?logo=graphql&logoColor=white" alt="LangGraph">
    </td>
  </tr>
  <tr>
    <td><strong>Large Language Models</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Groq%20LLM-00C7B7?logo=lightning&logoColor=white" alt="Groq LLM">
    </td>
  </tr>
  <tr>
    <td><strong>Machine Learning</strong></td>
    <td>
      <img src="https://img.shields.io/badge/DeBERTa%20Intent%20Classification-0A66C2?logo=scikitlearn&logoColor=white" alt="DeBERTa">
      <img src="https://img.shields.io/badge/Churn%20Prediction-701516?logo=pytorch&logoColor=white" alt="Churn Prediction">
    </td>
  </tr>
  <tr>
    <td><strong>Deployment</strong></td>
    <td>
      <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?logo=amazonaws&logoColor=white" alt="Lambda">
      <img src="https://img.shields.io/badge/API%20Gateway-232F3E?logo=amazonaws&logoColor=white" alt="API Gateway">
      <img src="https://img.shields.io/badge/ECR-FF9900?logo=amazonaws&logoColor=white" alt="ECR">
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

---

## 📊 Key System Characteristics

- Hybrid architecture (deterministic + LLM reasoning)  
- Intent-first routing before LLM invocation  
- Graph-based execution model (LangGraph)  
- Tool-augmented LLM reasoning (bounded scope)  
- Production-oriented design with latency constraints  

---

## 📈 Performance Highlights

- 89% accuracy (3-class intent classification)  
- Sub-800ms p95 latency  
- Reduced LLM routing failures via deterministic control layer  
- Eliminated tool-selection loops from initial LLM-only design  

---

## 🧪 Workflow Visualization

### Visual Representation
<p align="center"><img src="docs/Multi‑Agent%20Customer%20Support%20System%20using%20LangGraph%20and%20LLM%20Orchestrationgraphvisual%20naraction.png" alt="Visual Narration" width="400" height="450"></p>

### Execution Graph
<p align="center"><img src="docs/Multi‑Agent%20Customer%20Support%20System%20using%20LangGraph%20and%20LLM%20Orchestrationgraph%20workflow.png" alt="Workflow Diagram" width="400" height="650"></p>


---

## 🚧 Current Status

- Core routing system complete  
- Intent classifier integrated  
- Inquiry agent tool system in progress  
- Retention + complaint workflows under refinement  

---

## 🚀 Future Improvements

- Feedback loop for intent classifier improvement  
- LLM evaluation framework (hallucination + correctness)  
- Multi-channel deployment (voice, email, chat)  
- Observability layer for agent decisions  
- Human-in-the-loop escalation system  

---

## 💡 System Value

AURA demonstrates how modern GenAI systems can be designed using:

- structured control flow  
- selective LLM usage  
- graph-based orchestration  
- ML-driven routing  

It reflects real-world production constraints where **reliability matters more than full autonomy**.

---

> This project focuses on **production-grade GenAI system design, not just model experimentation.**