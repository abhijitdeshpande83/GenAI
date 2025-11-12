# IntelliQA

**IntelliQA** is a Retrieval Augmented Generation (RAG) based document question answering system.

## Key Features
* **Multi-format document ingestion**: Parses documents through a unified extraction layer.
* **Grounded answers**: Responses are generated only from retrieved context, keeping answers traceable to source documents.

## Architecture
IntelliQA follows a standard two-phase RAG design:

### Ingestion Phase
1. **Document upload**: User points to files.
2. **Text extraction**: Document content parsing.
3. **Text chunking**: Text is split into overlapping segments.
4. **Embedding & Indexing**: Vectors are stored in the vector store.

### Query Phase
1. **Question input**: User submits a question.
2. **Similarity search**: Retrieves the top K chunks closest to the question vector.
3. **Generation**: The LLM produces an answer grounded in the context.