# 🎤 AI Interview Partner

An AI-powered mock interview platform that conducts personalized interviews based on the candidate's role, experience, and resume. The application provides real-time interview questions, evaluates responses using AI, generates detailed performance reports, and stores interview results in a PostgreSQL database.

---

## 🚀 Features

- 📄 Resume Upload and Parsing
- 🤖 AI-Powered Interview Questions
- 💬 Interactive Interview Session
- 📊 AI Evaluation Report
- 📈 Technical, Communication, Problem Solving & Confidence Scores
- 📜 Interview History
- 🗄 PostgreSQL Database Integration (Neon)
- 🎨 Modern Streamlit User Interface

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI
- Groq API
- Llama 3.3 70B Versatile

### Database
- PostgreSQL (Neon)

### Libraries
- psycopg2
- python-dotenv
- PyPDF2
- Streamlit

---

## 📁 Project Structure

```
AI-Interview-Partner
│
├── app.py
├── interview_agent.py
├── llm.py
├── memory.py
├── prompts.py
├── resume_parser.py
├── session.py
├── models.py
│
├── database/
│   ├── db.py
│   ├── interview_repository.py
│   └── create_tables.py
│
├── ui/
│   ├── hero.py
│   ├── home.py
│   ├── interview.py
│   ├── evaluation.py
│   ├── history.py
│   └── styles.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Interview-Partner.git
```

Navigate to the project

```bash
cd AI-Interview-Partner
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

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

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

DATABASE_URL=YOUR_NEON_DATABASE_URL
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🗄 Database

The project uses **Neon PostgreSQL**.

Create tables using

```bash
python create_tables.py
```

---

## 📊 AI Evaluation

After every interview the system generates

- Overall Score
- Technical Knowledge
- Communication Skills
- Problem Solving Ability
- Confidence Score
- Strengths
- Weaknesses
- Suggestions
- Final Recommendation

Interview reports are stored inside PostgreSQL.

---

## 🔮 Future Enhancements

- Voice Interview
- PDF Report Download
- Dashboard Analytics
- Resume Matching Score
- Coding Interview Module
- HR Interview Module
- Interview Replay

---

## 👩‍💻 Author

**Kuna Varshitha**

B.Tech Computer Science Engineering

AI Interview Partner — AI Powered Mock Interview Platform
