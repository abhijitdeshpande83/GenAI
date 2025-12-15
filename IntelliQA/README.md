# IntelliQA

**IntelliQA** is a Retrieval Augmented Generation (RAG) based document question answering system. Upload documents in multiple formats, and ask natural language questions against their content. Answers are grounded in the source documents, with retrieval handling the knowledge and the LLM handling the reasoning and phrasing.

The project is built to demonstrate a production oriented RAG pipeline: robust multi format ingestion, content deduplication, session aware conversations, and a containerized, reusable package design.

## Overview

Large language models are powerful but have two well known limits: they do not know your private documents, and they hallucinate when asked about things outside their training data. RAG solves both. Instead of relying on the model's parametric memory, IntelliQA retrieves the most relevant chunks from your uploaded documents and passes them to the LLM as context. The model answers only from what was retrieved, and it can cite where the answer came from.

## Key Features

* **Multi format document ingestion**: Parses PDF, DOCX, TXT, HTML, and other formats through a unified extraction layer powered by Apache Tika.
* **Content deduplication**: Detects and skips duplicate documents and repeated chunks so the vector store stays clean and retrieval quality does not degrade.
* **Session management**: Maintains conversation context per session, so follow up questions ("what about the second point?") resolve correctly against earlier turns.
* **Grounded answers**: Responses are generated only from retrieved context, reducing hallucination and keeping answers traceable to source documents.
* **Dockerized**: Fully containerized via the included `dockerfile` for consistent, reproducible environments.
<!-- If deployed to AWS, add a line here, e.g.: * Cloud deployed: Hosted on AWS <service> -->
* **Reusable package**: Core RAG logic lives in the `rag_pipeline` package, separated from the demo notebook.

## Architecture

IntelliQA follows a standard two phase RAG design: an ingestion phase that indexes documents, and a query phase that answers questions.

![IntelliQA RAG Flow](./RAG%20Flow.png)

### Ingestion Phase

1. **Document upload**: User uploads one or more files.
2. **Text extraction**: Apache Tika parses each file and extracts raw text, supporting PDF, DOCX, HTML, TXT, and other formats.
3. **Deduplication check**: Documents and chunks already present in the index are detected and skipped.
4. **Text chunking**: Extracted text is split into overlapping segments.
5. **Embedding**: Each chunk is converted into a dense vector by the embedding model.
6. **Indexing**: Vectors are stored in the vector store for similarity search.

### Query Phase

1. **Question input**: User submits a natural language question.
2. **Query embedding**: The question is converted into a vector using the same embedding model.
3. **Similarity search**: The system retrieves the top K chunks whose vectors are closest to the question vector.
4. **Prompt assembly**: The question, retrieved context, and session history are combined into a single prompt.
5. **Generation**: The LLM produces an answer grounded in the retrieved context.
6. **Response**: The answer is returned to the user along with its source context.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.x |
| Orchestration | LangChain |
| Document parsing | Apache Tika |
| Embeddings | <!-- e.g., OpenAI text-embedding-3-small, or sentence-transformers all-MiniLM-L6-v2 --> |
| Vector store | Chroma (persisted locally in `chroma_db/`) |
| LLM | <!-- e.g., OpenAI GPT-4o-mini, or AWS Bedrock model --> |
| Core package | `rag_pipeline` (custom RAG modules) |
| Interface | Jupyter Notebook (`IntelliQA.ipynb`) |
| Packaging | `setup.py` (pip installable) |
| Containerization | Docker |

## How RAG Works in IntelliQA

1. **Chunking**: Documents are split into overlapping segments so that no single retrieval unit is too large for the model context, while overlap preserves meaning across boundaries.
2. **Embedding**: Each chunk is converted into a dense vector that captures its semantic meaning.
3. **Retrieval**: The user question is embedded the same way, then the system finds the top K chunks whose vectors are closest to the question vector.
4. **Generation**: The retrieved chunks, the question, and the session history are assembled into a single prompt. The LLM answers using only this grounded context.

This design means the model's answer is bounded by the documents, which is exactly what makes RAG reliable for enterprise document Q&A.

## Project Structure

```
IntelliQA/
├── IntelliQA.ipynb         # Main notebook: runs the end-to-end RAG demo
├── rag_pipeline/           # Core RAG package
│   ├── __init__.py
│   ├── query_engine.py     # Query embedding, retrieval, and answer generation
│   ├── vector_store.py     # Chroma vector store setup and indexing
│   └── utils.py            # Document parsing, chunking, and deduplication helpers
├── chroma_db/              # Persisted Chroma vector store
├── RAG Flow.png            # Architecture / flow diagram
├── dockerfile              # Container definition
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation config
└── README.md
```

> Note: `venv/` and `dist/` appear in the working directory but should not be committed. Add them to `.gitignore` along with `__pycache__/` to keep the repository clean.

## Getting Started

### Prerequisites

* Python 3.x
* Docker (optional, for containerized runs)
* An API key for your chosen LLM and embedding provider

### Run Locally

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the rag_pipeline package in editable mode
pip install -e .

# Set environment variables
export OPENAI_API_KEY="your-key-here"   # or your provider's key

# Launch the notebook
jupyter notebook IntelliQA.ipynb
```

Run the notebook cells in order. The `rag_pipeline` modules handle ingestion, indexing, retrieval, and generation, while the notebook drives the end to end demo.

### Run with Docker

```bash
# Build the image
docker build -t intelliqa -f dockerfile .

# Run the container
docker run -p <host_port>:<container_port> \
  -e OPENAI_API_KEY="your-key-here" \
  intelliqa
```

## Usage

1. Open `IntelliQA.ipynb` in Jupyter.
2. Point the ingestion step at your document files (PDF, DOCX, TXT, HTML, and other formats).
3. Run the ingestion cells. Apache Tika extracts text, duplicates are skipped, and chunks are embedded into the Chroma store.
4. Use the query cells to ask natural language questions.
5. The query engine retrieves the most relevant chunks and returns a grounded answer.
6. Ask follow up questions in the same session to carry conversation context forward.

## Design Decisions

* **Apache Tika over format specific parsers**: A single extraction layer handles dozens of file types, which removes the need to maintain separate parsing logic per format.
* **Deduplication at ingestion**: Indexing the same content twice inflates the vector store and skews retrieval toward repeated chunks. Catching duplicates early keeps results clean.
* **Session scoped context**: Conversational Q&A only works if the system remembers the thread. Session management makes follow up questions resolve naturally.
* **Containerization first**: Docker guarantees the same behavior locally and on AWS, which removes "works on my machine" issues during deployment.

## Future Improvements

* Add a reranking step (cross encoder) after retrieval to improve the precision of the top K chunks
* Return inline citations that link each answer sentence back to its source chunk
* Add hybrid search (keyword plus vector) for better recall on exact term queries
* Add evaluation with RAG specific metrics: faithfulness, answer relevance, and context precision
* Support streaming responses for a faster perceived experience
* Add user authentication and per user document isolation

## Related Projects

IntelliQA is part of a broader Generative AI portfolio that also includes agentic assistants and fine tuned LLM systems. See the other folders in the [GenAI repository](https://github.com/abhijitdeshpande83/GenAI).

---

## Supported Document Formats

IntelliQA currently supports a variety of document formats through Apache Tika, including:

* PDF (`.pdf`)
* Microsoft Word (`.docx`)
* Plain Text (`.txt`)
* HTML (`.html`)
* Rich Text Format (`.rtf`)

Additional formats supported by Apache Tika can be integrated with minimal changes.

---

## Design Principles

The project is built around the following principles:

* **Accuracy** – Answers are grounded in retrieved document content.
* **Modularity** – Core RAG components are separated into reusable modules.
* **Scalability** – The architecture can be extended to larger document collections.
* **Maintainability** – Clear package structure and containerized deployment simplify development and operations.

---

