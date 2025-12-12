# RAG QnA & Summarization Chatbot

A Streamlit-based application that performs Retrieval-Augmented Generation (RAG) to answer questions based on uploaded documents. It also provides document summarization capabilities.

## Features

- **Document Ingestion**: Upload text-based documents (PDF, TXT, MD, HTML, DOCX).
- **Automatic Summarization**: Instantly generates a summary of the uploaded document using `MarkItDown` and GenAI.
- **RAG Chatbot**: Ask questions about the uploaded content. The app uses ChromaDB for vector storage and retrieval to provide accurate, context-aware answers.
- **Persistent Storage**: Vector embeddings are stored locally in `chroma_db` for persistent retrieval across sessions.

## Architecture

- **Frontend**: Streamlit
- **Vector Database**: ChromaDB
- **LLM Integration**: OpenAI (via `tiktoken` for tokenization and standard API calls)
- **Document Processing**: `MarkItDown` for converting various file formats to text.

## Prerequisites

- Python 3.8+
- An OpenAI API Key

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abd-RAHEEM/RAGx.git
    cd RAGx
    ```

2.  **Create and activate a virtual environment:**

    *Windows:*
    ```bash
    create_venv.bat
    ```
    *Or manually:*
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

    *Linux/Mac:*
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory (copy from a template if available, excluding secrets from git):

    ```env
    MODEL_API_KEY=your_openai_api_key_here
    CHROMA_COLLECTION_NAME=your_collection_name
    ```

## Usage

1.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

2.  **Navigate to the App:**
    Open your browser at `http://localhost:8501`.

3.  **Ingest Documents:**
    - Go to the **Ingest** page.
    - Upload a file.
    - View the summary.
    - Click "Upload & Ingest to Chroma DB" to index the content.

4.  **Chat:**
    - Switch to the **Chatbot** page.
    - Ask questions related to the document you just uploaded.

## Directory Structure

```
RAGx/
├── .env                # Environment variables (not contained in repo)
├── .gitignore          # Git ignore file
├── activate.bat        # Helper script to activate venv
├── create_venv.bat     # Helper script to create venv
├── chroma_db/          # Persistent Vector DB storage
├── chroma_services.py  # ChromaDB interaction logic
├── data.txt            # Sample data file
├── genai_services.py   # AI/LLM service logic
├── main.py             # Entry point for Streamlit app
├── pages/              # Streamlit pages
│   ├── chatbot_page.py
│   └── ingest_page.py
└── requirements.txt    # Python dependencies
```

## Security Note

- **API Keys**: Ensure your `.env` file is never pushed to public repositories. This project is configured with a `.gitignore` that excludes `.env` and the `chroma_db` directory.
