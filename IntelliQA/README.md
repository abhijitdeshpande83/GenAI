# IntelliQA

**IntelliQA** is a Retrieval Augmented Generation (RAG) based document question answering system.

## Key Features
* **Multi-format document ingestion**: Parses PDF, DOCX, TXT, HTML through a unified extraction layer powered by Apache Tika.
* **Content deduplication**: Detects and skips duplicate documents and repeated chunks so the vector store stays clean.
* **Grounded answers**: Responses are generated only from retrieved context.

## Design Decisions
* **Apache Tika over format-specific parsers**: A single extraction layer handles dozens of file types, removing the need to maintain separate parsing logic per format.
* **Deduplication at ingestion**: Indexing the same content twice inflates the vector store and skews retrieval toward repeated chunks.

## Project Structure

```text
IntelliQA/
├── IntelliQA.ipynb         # Main notebook: runs the end-to-end RAG demo
├── rag_pipeline/           # Core RAG package
│   ├── __init__.py
│   ├── query_engine.py     # Query embedding, retrieval, and answer generation
│   ├── vector_store.py     # Chroma vector store setup and indexing
│   └── utils.py            # Document parsing and chunking helpers
├── requirements.txt        # Python dependencies
├── setup.py                # Package installation config
└── README.md
