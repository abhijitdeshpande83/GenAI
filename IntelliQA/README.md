<h1 align="center">🤖 IntelliQA</h1>

<p align="center">
  <b>Ask any document. Get grounded answers.</b><br/>
  <sub>A production oriented Retrieval Augmented Generation (RAG) system that turns your PDFs, Word docs, HTML files, and more into a private, conversational knowledge base.</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Build-rag__pipeline_v3.0-blue?style=flat-square" alt="Build"/>
  <img src="https://img.shields.io/badge/Status-Stable-success?style=flat-square" alt="Status"/>
  <img src="https://img.shields.io/badge/Deployed-AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white" alt="Deployed"/>
</p>

---

## 📖 Overview

Large language models are powerful but they do not know your private documents and they hallucinate on topics outside their training data. **IntelliQA solves both** by retrieving the most relevant chunks from your uploaded documents and passing them to the LLM as grounded context. The model answers only from what was retrieved, making the system reliable for enterprise document Q&A.

> 💡 Core RAG logic is packaged in the `rag_pipeline` Python package and shipped as a **prebuilt wheel**, so anyone can install it with a single `pip install` and start asking questions.

---

## ✨ Key Features

<table align="center">
<tr>
<td align="center" width="33%">
  <h3>🗂️</h3>
  <h4>Multi Format Ingestion</h4>
  <p>Parse <b>PDF, DOCX, HTML, TXT, RTF, ODT</b> and dozens more through a single extraction layer.</p>
  <sub><i>Apache Tika</i></sub>
</td>
<td align="center" width="33%">
  <h3>🔁</h3>
  <h4>Smart Deduplication</h4>
  <p>Detects and skips already indexed content to keep the vector store clean and retrieval precise.</p>
  <sub><i>Custom dedup pipeline</i></sub>
</td>
<td align="center" width="33%">
  <h3>💬</h3>
  <h4>Session Aware Q&A</h4>
  <p>Maintains conversation state so follow up questions resolve correctly against earlier turns.</p>
  <sub><i>LangChain memory</i></sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
  <h3>🎯</h3>
  <h4>Grounded Answers</h4>
  <p>Runs at <code>temperature=0</code> and answers only from retrieved context to minimize hallucination.</p>
  <sub><i>Deterministic output</i></sub>
</td>
<td align="center" width="33%">
  <h3>⚡</h3>
  <h4>Lightning Fast LLM</h4>
  <p>Sub second responses powered by Groq's LPU serving of <b>Llama 3.3 70B Versatile</b>.</p>
  <sub><i>Groq + Meta Llama</i></sub>
</td>
<td align="center" width="33%">
  <h3>📦</h3>
  <h4>Pip Installable</h4>
  <p>Core logic shipped as a <b>prebuilt wheel</b> in <code>dist/</code> for instant installation anywhere.</p>
  <sub><i>rag_pipeline v3.0</i></sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
  <h3>🐳</h3>
  <h4>Containerized</h4>
  <p>Fully Dockerized for consistent, reproducible runs across local machines and cloud.</p>
  <sub><i>Docker</i></sub>
</td>
<td align="center" width="33%">
  <h3>☁️</h3>
  <h4>Cloud Deployed</h4>
  <p>Live on AWS EC2, demonstrating real cloud deployment beyond a local laptop.</p>
  <sub><i>AWS EC2</i></sub>
</td>
<td align="center" width="33%">
  <h3>🆓</h3>
  <h4>Open Weight Stack</h4>
  <p>No LLM vendor lock in. Built on open weight models and open source infrastructure.</p>
  <sub><i>Meta Llama + HF</i></sub>
</td>
</tr>
</table>

---

## 🏗️ Architecture

<p align="center">
  <img src="./RAG%20Flow.png" alt="IntelliQA RAG Flow"/>
</p>

IntelliQA follows a clean two phase RAG design.

<details open>
<summary><b>📥 Phase 1: Ingestion</b> (run once per document set)</summary>

1. **Upload** documents in any supported format.
2. **Parse** with Apache Tika to extract clean text.
3. **Deduplicate** already indexed content.
4. **Chunk** the text into overlapping segments.
5. **Embed** each chunk into a 384 dimensional vector using `all-MiniLM-L6-v2`.
6. **Index** vectors into ChromaDB, persisted in `chroma_db/`.

</details>

<details open>
<summary><b>🔎 Phase 2: Query</b> (runs per question)</summary>

1. **Embed** the user question with the same embedding model.
2. **Retrieve** the top K nearest chunks via cosine similarity.
3. **Assemble** a prompt combining the question, retrieved context, and session history.
4. **Generate** the answer with Llama 3.3 70B at `temperature=0`.
5. **Return** the response while preserving session state for follow ups.

</details>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|:------|:-----------|:--------|
| **Language** | ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat-square&logo=python&logoColor=white) | Core implementation |
| **Notebook** | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) | Interactive demo and development |
| **RAG Framework** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) | Ingestion and retrieval orchestration |
| **Vector Store** | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logoColor=white) | Persistent similarity search |
| **LLM** | ![Llama](https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white) | Answer generation |
| **LLM Serving** | ![Groq](https://img.shields.io/badge/Groq_LPU-F55036?style=flat-square&logoColor=white) | Low latency inference |
| **Embeddings** | ![HuggingFace](https://img.shields.io/badge/all--MiniLM--L6--v2-FFD21E?style=flat-square&logo=huggingface&logoColor=black) | 384 dim semantic vectors |
| **Document Parsing** | ![Apache Tika](https://img.shields.io/badge/Apache_Tika-D22128?style=flat-square&logo=apache&logoColor=white) | Unified multi format extraction |
| **Packaging** | ![Wheel](https://img.shields.io/badge/setup.py_%2B_wheel-3776AB?style=flat-square&logo=pypi&logoColor=white) | Distributable Python package |
| **Containerization** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | Reproducible runtime |
| **Deployment** | ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) | Cloud hosting |

---

## 📁 Project Structure

```
IntelliQA/
├── 📓 IntelliQA.ipynb                          # Main notebook: end-to-end RAG demo
├── 📦 rag_pipeline/                            # Core RAG package source
│   ├── __init__.py
│   ├── query_engine.py                         # Query embedding, retrieval, generation
│   ├── vector_store.py                         # Chroma vector store setup and indexing
│   └── utils.py                                # Parsing, chunking, deduplication helpers
├── 📂 dist/
│   └── rag_pipeline-3.0-py3-none-any.whl       # Prebuilt installable package
├── 🗃️  chroma_db/                              # Persisted Chroma vector store
├── 🖼️  RAG Flow.png                            # Architecture diagram
├── 🐳 dockerfile                               # Container definition
├── 📜 requirements.txt                         # Python dependencies
├── ⚙️  setup.py                                # Package build configuration
└── 📘 README.md
```

---

## 🚀 Installation & Usage

> 🎯 Three paths, each for a different goal. Pick what fits your use case.

<br/>

### ⚡ Option 1: Install the Prebuilt Wheel <sub><i>(fastest, recommended)</i></sub>

Install the `rag_pipeline` package directly from the prebuilt wheel shipped in `dist/`. Cleanest path if you want to use IntelliQA as a library in your own code.

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Install the prebuilt wheel
pip install dist/rag_pipeline-3.0-py3-none-any.whl

# Set your Groq API key
export GROQ_API_KEY="your-key-here"
```

Use it anywhere in your code:

```python
from rag_pipeline import vector_store, query_engine, utils

# See IntelliQA.ipynb for full usage examples
```

<br/>

### 🛠️ Option 2: Install from Source <sub><i>(for development)</i></sub>

Use this path if you want to modify the RAG logic, contribute, or run the demo notebook end to end.

```bash
# Clone the repository
git clone https://github.com/abhijitdeshpande83/GenAI.git
cd GenAI/IntelliQA

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate              # Windows: venv\Scripts\activate

# Install dependencies and the package in editable mode
pip install -r requirements.txt
pip install -e .

# Set your Groq API key
export GROQ_API_KEY="your-key-here"

# Launch the notebook
jupyter notebook IntelliQA.ipynb
```

<br/>

### 🐳 Option 3: Run with Docker <sub><i>(fully isolated)</i></sub>

Use this path for a fully isolated, reproducible runtime.

```bash
# Build the image
docker build -t intelliqa -f dockerfile .

# Run the container
docker run -p 8888:8888 \
  -e GROQ_API_KEY="your-key-here" \
  intelliqa
```

The container exposes Jupyter on port `8888`. Open the printed URL in your browser to interact with `IntelliQA.ipynb`.

---

## 🧠 Design Decisions

> The choices a hiring manager or senior engineer is most likely to ask about.

| 🔑 Decision | 💡 Rationale |
|:--|:--|
| **Groq + Llama 3.3 70B** | Sub second inference via LPU serving, with open weight flexibility and no LLM vendor lock in |
| **`temperature=0`** | Deterministic, repeatable answers, which is critical for document Q&A where the same question should return the same response |
| **`all-MiniLM-L6-v2` embeddings** | 384 dimensional vectors, fast on CPU, no API cost, strong quality for general semantic search |
| **ChromaDB (local persistence)** | Simple to operate, no separate infrastructure to manage, supports metadata filtering and persistence out of the box |
| **Apache Tika for parsing** | One extraction layer across dozens of formats, eliminating format specific parser maintenance |
| **Deduplication at ingestion** | Prevents the vector store from being polluted with repeated content, which would skew similarity scores |
| **Reusable `rag_pipeline` package** | Core logic decoupled from the notebook and shipped as a wheel, so it can be imported into a future API or web app without rewrites |

---

## 👤 About the Author

**Abhijit Deshpande**
Business Systems Analyst (AI/ML Systems) at Charter Communications. Actively transitioning into Data Science, ML, and AI Engineering roles. M.S. Industrial Engineering, University of Texas at Arlington (GPA 3.9 / 4.0).

<p align="left">
  <a href="https://theanalyticmind.com"><img src="https://img.shields.io/badge/Portfolio-theanalyticmind.com-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>
  <a href="https://linkedin.com/in/abhijit-deshpande/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/abhijitdeshpande83"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

---

## 📄 License

This project is open source under the **MIT License**. See [LICENSE](./LICENSE) for details.

<p align="center">
  <sub>Built with ❤️ as part of the <a href="https://github.com/abhijitdeshpande83/GenAI">GenAI portfolio</a>.</sub>
</p>