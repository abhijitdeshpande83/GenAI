# IntelliQA

**IntelliQA** is a Retrieval-Augmented Generation (RAG) based document question-answering system. Upload documents in multiple formats and ask natural language questions about their content. Answers are grounded in the source documents, with retrieval handling knowledge access and the LLM handling reasoning and response generation.

The project demonstrates a production-oriented RAG pipeline featuring robust multi-format document ingestion, content deduplication, session-aware conversations, and a containerized, reusable package design.

---

## Overview

Large Language Models (LLMs) are powerful but have two well-known limitations:

1. They do not have access to your private documents by default.
2. They may hallucinate when answering questions outside their training data.

Retrieval-Augmented Generation (RAG) addresses both challenges. Instead of relying solely on the model's parametric memory, IntelliQA retrieves the most relevant document chunks and provides them as context to the LLM. The model then generates answers based only on the retrieved information, enabling more accurate and traceable responses.

---

## Key Features

* **Multi-format document ingestion**: Parses PDF, DOCX, TXT, HTML, and other document formats through a unified extraction layer powered by Apache Tika.
* **Content deduplication**: Detects and skips duplicate documents and repeated chunks to maintain vector store quality and improve retrieval performance.
* **Session management**: Preserves conversational context across user sessions, enabling accurate follow-up questions.
* **Grounded answers**: Generates responses exclusively from retrieved context, reducing hallucinations and improving traceability.
* **Dockerized deployment**: Fully containerized using Docker for consistent and reproducible environments.
* **Reusable package design**: Core RAG functionality is encapsulated within the `rag_pipeline` package, separated from the demonstration notebook.

---

## Architecture

IntelliQA follows a standard two-phase RAG architecture:

1. **Ingestion Phase** – Processes and indexes uploaded documents.
2. **Query Phase** – Retrieves relevant content and generates answers.

![IntelliQA RAG Flow](./RAG%20Flow.png)

### Ingestion Phase

1. **Document Upload** – Users upload one or more files.
2. **Text Extraction** – Apache Tika extracts raw text from documents.
3. **Deduplication Check** – Existing documents and chunks are identified and skipped.
4. **Text Chunking** – Content is split into overlapping segments.
5. **Embedding Generation** – Chunks are converted into dense vector embeddings.
6. **Indexing** – Embeddings are stored in the vector database for similarity search.

### Query Phase

1. **Question Input** – User submits a natural language query.
2. **Query Embedding** – The question is converted into an embedding vector.
3. **Similarity Search** – The top-k most relevant chunks are retrieved.
4. **Prompt Assembly** – Retrieved context and conversation history are combined.
5. **Answer Generation** – The LLM generates a context-grounded response.
6. **Response Delivery** – The answer and source context are returned to the user.

---

## Tech Stack

| Layer            | Technology                                 |
| ---------------- | ------------------------------------------ |
| Language         | Python 3.x                                 |
| Orchestration    | LangChain / LangGraph                      |
| Document Parsing | Apache Tika                                |
| Embeddings       | HuggingFace Embeddings / OpenAI Embeddings |
| Vector Store     | Chroma (persisted locally in `chroma_db/`) |
| LLM              | OpenAI GPT Models                          |
| Core Package     | `rag_pipeline`                             |
| Interface        | Jupyter Notebook (`IntelliQA.ipynb`)       |
| Packaging        | `setup.py`                                 |
| Containerization | Docker                                     |

---

## How RAG Works in IntelliQA

### 1. Chunking

Documents are split into overlapping segments so that each retrieval unit remains within the model's context window.

### 2. Embedding

Each chunk is transformed into a dense vector representation that captures semantic meaning.

### 3. Retrieval

User queries are embedded using the same embedding model, and the most relevant chunks are retrieved through similarity search.

### 4. Generation

Retrieved chunks, user questions, and conversation history are combined into a prompt for the LLM to generate a grounded answer.

---

## Project Structure

```text
IntelliQA/
├── IntelliQA.ipynb         # End-to-end RAG demonstration notebook
├── rag_pipeline/
│   ├── __init__.py
│   ├── query_engine.py     # Query embedding, retrieval, and answer generation
│   ├── vector_store.py     # Chroma setup and indexing
│   └── utils.py            # Parsing, chunking, and deduplication utilities
├── chroma_db/              # Persistent Chroma vector database
├── RAG Flow.png            # Architecture diagram
├── dockerfile              # Docker configuration
├── requirements.txt        # Project dependencies
├── setup.py                # Package installation configuration
└── README.md
```

---

## Getting Started

### Prerequisites

* Python 3.9+
* Docker (optional)
* OpenAI API Key

### Clone the Repository

```bash
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install the Package

```bash
pip install -e .
```

---

## Environment Variables

Set your OpenAI API key before running the application.

**Linux/macOS**

```bash
export OPENAI_API_KEY="your-api-key"
```

**Windows (PowerShell)**

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

---

## Running IntelliQA

Launch the notebook:

```bash
jupyter notebook IntelliQA.ipynb
```

---

## Docker Usage

### Build the Docker Image

```bash
docker build -t intelliqa -f dockerfile .
```

### Run the Container

```bash
docker run -p 8888:8888 \
  -e OPENAI_API_KEY="your-api-key" \
  intelliqa
```

---

## Future Enhancements

* Support for additional vector databases (FAISS, Pinecone, Weaviate).
* Metadata-based filtering during retrieval.
* Streaming responses.
* Source citation and highlighting in generated answers.
* Web-based UI using Streamlit or FastAPI.
* Hybrid search combining semantic and keyword retrieval.


---

## Example Usage

After uploading documents, users can ask questions such as:

* "Summarize the key findings in this report."
* "What recommendations are mentioned in the document?"
* "Compare information across the uploaded files."
* "What risks or limitations are discussed?"
* "Explain the second section in simple terms."

---

## Why IntelliQA?

* Reduces hallucinations by grounding responses in retrieved documents.
* Supports multiple document formats through a unified ingestion pipeline.
* Preserves conversational context for follow-up questions.
* Eliminates duplicate content to improve retrieval quality.
* Provides a modular and reusable RAG architecture for experimentation and production use.

---
