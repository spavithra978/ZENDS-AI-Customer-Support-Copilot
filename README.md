# ZENDS-AI-Customer-Support-Copilot

An AI-powered telecom customer support assistant built using NLP, HuggingFace Transformers, RAG, and Streamlit.

---

## Project Overview

This project simulates an AI customer support copilot for a virtual telecom company called **ZENDS Communications**.

The system can:

* Detect **customer intent**
* Analyze **customer sentiment**
* Retrieve relevant **company policies**
* Generate **recommended responses for support agents**

---

## Technologies Used

* Python
* HuggingFace Transformers
* DistilBERT
* SentenceTransformers
* FAISS Vector Search
* Streamlit
* Scikit-learn
* Pandas

---

## Project Architecture

User Query
↓
Intent Classification (DistilBERT)
↓
Sentiment Analysis
↓
RAG Retrieval (SentenceTransformer + FAISS)
↓
Policy Context
↓
AI Recommended Response
↓
Streamlit Dashboard

---

## Dataset

A synthetic dataset of **20,000 customer queries** was generated for training.

Columns:

* text
* intent
* sentiment

Intents included:

* Billing
* Refund
* Technical
* Complaint
* Product Inquiry
* Other

---

## Features

* Real-time query analysis
* Intent classification
* Sentiment detection
* Policy retrieval using embeddings
* AI-generated recommended responses
* Interactive dashboard using Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/zends-ai-copilot.git
cd zends-ai-copilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## Example Query

```
Why was I charged twice for my internet plan?
```

Output:

* Intent: Billing
* Sentiment: Angry
* Retrieved Policy
* AI Recommended Response

---

## Future Improvements

* Deploy using cloud platforms
* Add LLM response generation
* Expand company policy database
* Integrate with real customer support APIs

---

