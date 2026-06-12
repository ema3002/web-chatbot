# 🤖 Baymax — AI Web Chatbot

> An intelligent web-based chatbot powered by **Groq API** and **Flask**, featuring RAG (Retrieval-Augmented Generation), voice transcription, flashcard generation, resume analysis, and multi-agent research.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?style=for-the-badge&logo=render)](https://web-chatbot-unx8.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge)](https://groq.com)

---

## ✨ Features

- 💬 **AI Chat** — Conversational chatbot powered by Groq's ultra-fast LLM inference
- 📄 **PDF RAG** — Upload a PDF and ask questions based on its content
- 🎙️ **Voice Transcription** — Speech-to-text via Groq Whisper
- 🃏 **Flashcard Generator** — Auto-generate study flashcards from any topic or document
- 📝 **Resume Analyzer** — Upload your resume and get instant AI feedback
- 🔍 **Multi-Agent Research Tool** — Decompose complex queries into sub-tasks and aggregate results

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| LLM Provider | Groq API (Llama 3) |
| Speech-to-Text | Groq Whisper |
| PDF Processing | PyPDF2 |
| Server (Production) | Gunicorn |
| Deployment | Render |
| Config | python-dotenv |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ema3002/web-chatbot.git
cd web-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
python app.py
```

App will be live at `http://localhost:5000`

---

## 📁 Project Structure
<img width="378" height="185" alt="image" src="https://github.com/user-attachments/assets/48cc128a-63a9-4890-a429-027998f697a9" />


## ⚙️ Deployment (Render)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your `ema3002/web-chatbot` repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable: `GROQ_API_KEY`
6. Deploy 🚀

---

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key (required) |

> ⚠️ Never commit your `.env` file. It's listed in `.gitignore`.

---

## 👩‍💻 Author

**Ema** — BSc CSE @ Dhaka International University

[![Portfolio](https://img.shields.io/badge/Portfolio-miskatul.netlify.app-00c8ff?style=flat-square)](https://miskatul.netlify.app)
[![GitHub](https://img.shields.io/badge/GitHub-ema3002-181717?style=flat-square&logo=github)](https://github.com/ema3002)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
