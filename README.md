# 🤖 AI Quiz Generator

An AI-powered Quiz Generator built with **FastAPI**, **Streamlit**, and **Google Gemini AI**. The application generates quizzes dynamically based on the topic, difficulty level, question count, and question type selected by the user.

---

## 🚀 Features

- 🤖 AI-powered quiz generation using Google Gemini
- 📚 Topic-based quiz creation
- 🎯 Difficulty selection (Easy, Medium, Hard)
- 🔢 Custom number of questions
- ❓ Multiple question types (MCQ, True/False)
- ⚡ FastAPI REST API
- 🖥️ Streamlit frontend
- 📄 Structured JSON responses
- ❤️ Health Check API
- 📝 Logging support
- 🔐 Environment variable configuration

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend |
| Google Gemini API | AI Quiz Generation |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |

---

## 📂 Project Structure

```text
AI-Quiz-Generator/
│
├── BACKEND/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   └── run.py
│
├── FRONTEND/
│   ├── app.py
│   └── utils.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Quiz-Generator.git
```

Go to the project folder

```bash
cd AI-Quiz-Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the **BACKEND** folder.

```env
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL_NAME=gemini-2.5-flash
APP_NAME=AI Quiz Generator
APP_VERSION=1.0.0
```

---

## ▶️ Run Backend

```bash
cd BACKEND
python run.py
```

---

## ▶️ Run Frontend

```bash
cd FRONTEND
streamlit run app.py
```

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome API |
| GET | `/health` | Health Check |
| POST | `/generate-quiz` | Generate AI Quiz |

---


## 🔮 Future Improvements

- User Authentication
- Quiz Score Tracking
- Quiz History
- Database Integration
- Export Quiz as PDF
- Timer-based Quiz
- Leaderboard

---

## 👨‍💻 Author

**Bittu Sharma**

---

⭐ If you found this project useful, consider giving it a star on GitHub.
