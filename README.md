# 🎓 ITI Research Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** application that enables students and researchers to upload academic papers and interact with them using natural language queries.

This project was developed as part of the **ITI Advanced Generative AI Course**.

---

## 📌 Project Overview

The ITI Research Assistant helps users understand research papers by combining semantic search with Large Language Models (LLMs).

Instead of answering from general knowledge, the system retrieves relevant information directly from uploaded documents and generates grounded responses based only on document content.

---

## 📖 Project Explanation

The system follows a Retrieval-Augmented Generation (RAG) pipeline:

1. **Document Upload**
   - Users upload research papers in PDF or DOCX format.

2. **Text Extraction**
   - The system extracts textual content from documents.

3. **Chunking**
   - Documents are divided into smaller chunks for efficient processing.

4. **Embedding Generation**
   - Text chunks are converted into embeddings using HuggingFace models.

5. **Vector Database**
   - Embeddings are stored in a FAISS vector store.

6. **Semantic Retrieval**
   - Relevant document sections are retrieved based on user queries.

7. **LLM Response Generation**
   - Retrieved context is passed to a Groq-hosted LLaMA3 model to generate accurate answers.

---

## 🚀 Features

- Upload Research Papers (PDF / DOCX)
- Semantic Search using Vector Database
- Research Paper Question Answering
- Context-Grounded Responses
- Source Citation Display
- Academic Assistant Behavior
- Interactive Streamlit Interface
- Groq LLM Integration

---

## ⭐ Bonus Feature — Document Summarization

A dedicated summarization button allows automatic summarization of uploaded research papers including:

- Research Objective
- Methodology
- Key Findings
- Main Contributions

💬 How to Use

Upload a research paper.

Wait until document indexing finishes.

Ask questions related to the research paper.

View grounded answers with sources.

Click Summarize Uploaded Document to generate a summary.

✅ Functional Coverage

Document Ingestion

Chunking & Embedding

Vector Store Retrieval

LLM-based Question Answering

Document Summarization

🔮 Future Improvements

Multi-document comparison

Conversation memory

Section-based summarization

Cloud deployment

👨‍💻 Author

Ali Mostafa
AI Engineering Student
Faculty of Engineering – AI Department

LinkedIn:
https://www.linkedin.com/in/ali-developments/
GitHub:
https://github.com/Ali-Developments

---

## 🧠 System Workflow
