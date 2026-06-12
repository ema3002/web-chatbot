---

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
