# IntelliQA

**IntelliQA** is a Retrieval-Augmented Generation (RAG) based document question-answering system.

## Overview
Large language models are powerful but have two well-known limits: they do not know your private documents, and they hallucinate when asked about things outside their training data. RAG solves both. Instead of relying on the model's parametric memory, IntelliQA retrieves the most relevant chunks from your uploaded documents and passes them to the LLM as context.

## Project Structure

```text
IntelliQA/
├── IntelliQA.ipynb         # Main notebook: runs the end-to-end RAG demo
├── rag_pipeline/           # Core RAG package placeholder
├── requirements.txt        # Python dependencies
└── README.md