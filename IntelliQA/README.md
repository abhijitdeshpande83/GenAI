# IntelliQA

**IntelliQA** is a Retrieval Augmented Generation (RAG) based document question answering system.

## Key Features
* **Multi-format document ingestion**: Powered by Apache Tika.
* **Content deduplication**: Skips duplicate chunks.
* **Session management**: Maintains conversation context per session, so follow-up questions resolve correctly.
* **Dockerized**: Fully containerized setup.

## Future Improvements
* Add a reranking step (cross-encoder) after retrieval.
* Return inline citations linking back to source chunks.
* Add hybrid search (keyword plus vector).

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
