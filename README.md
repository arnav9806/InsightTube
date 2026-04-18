#  InsightTube

**InsightTube** is an AI-powered YouTube video intelligence system that transforms video content into structured insights using **LLMs + RAG (Retrieval-Augmented Generation)**.

It allows users to extract transcripts, generate summaries, ask contextual questions, create notes, and translate content—all from a single interface.

---

##  Features

###  Video Processing

* Extracts transcript from YouTube videos
* Processes and chunks content for AI understanding

---

###  Smart Summarization

* Short Summary
* Detailed Summary
* Key Takeaways

---

###  RAG-based Chatbot

* Ask questions about the video
* Answers strictly from transcript (no hallucination)
* Provides **timestamp references** for answers

---

###  Notes Generator

* Study Notes
* Revision Notes
* Quiz (MCQs)
* Flashcards

---

### 🌐 Translation

* Translate full transcript (Hindi → English)

---

###  Export

* Generate and download **PDF** of detailed summary

---

##  Architecture

InsightTube follows a **modular, production-ready architecture**:

```text
Frontend (Streamlit)
        ↓
FastAPI Backend (API Layer)
        ↓
Service Layer
        ↓
RAG Pipeline (Chunking + Embeddings + Retrieval)
        ↓
Vector Database (FAISS)
```

---

##  Tech Stack

| Layer      | Technology             |
| ---------- | ---------------------- |
| Frontend   | Streamlit              |
| Backend    | FastAPI                |
| LLM        | OpenAI / Local Models  |
| RAG        | Custom Pipeline        |
| Vector DB  | FAISS                  |
| Embeddings | Sentence Transformers  |
| PDF        | ReportLab              |
| Transcript | YouTube Transcript API |

---

## 📁 Project Structure

```bash
InsightTube/
│
├── frontend/
│   └── app.py
│
├── backend/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── rag/
│   ├── chains/
│   ├── utils/
│   ├── models/
│   └── storage/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

###  1. Create Virtual Environment

```bash
py -3.8 -m venv venv
venv\Scripts\activate
```

---

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ▶ 3. Run Backend

```bash
uvicorn backend.main:app --reload
```

---

###  4. Run Frontend

```bash
streamlit run frontend/app.py
```

---

##  Workflow

1. User inputs YouTube URL
2. Transcript is extracted
3. Text is chunked and stored in vector DB
4. User can:

   * Generate summaries
   * Ask questions (RAG chatbot)
   * Create notes
   * Translate transcript
5. Results are displayed and can be exported as PDF

---

## Future Improvements

* Multi-video support
* Streaming chatbot responses
* User authentication
* Cloud deployment (AWS/GCP)
* UI enhancements

---

##  Resume Highlight

> Built InsightTube, a full-stack AI system using RAG architecture with vector databases (FAISS) to enable transcript-based summarization, semantic search, contextual chatbot with timestamp grounding, and automated note generation from YouTube videos.

---

## 📌 Author

**Arnav Sokal**
GitHub: https://github.com/arnav9806

---

