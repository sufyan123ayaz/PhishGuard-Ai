🛡️ PhishGuard-AI — AI-Driven Phishing Detection System

PhishGuard-AI is an AI-driven cybersecurity project designed to detect phishing attempts in URLs and email content using machine learning and rule-based security checks.
The system is built with FastAPI and provides an interactive Swagger UI for testing and integration.

This project is ideal for students, researchers, and cybersecurity professionals who want to understand how AI can be used in real-world phishing detection systems.

🚀 Features

✅ AI-Driven phishing detection

✅ URL phishing analysis

✅ Email/text phishing detection

✅ Confidence score with result

✅ Reason-based output (why it is phishing or safe)

✅ REST API using FastAPI

✅ Interactive Swagger UI (/docs)

✅ Easy to integrate with other systems

✅ Modular and extendable architecture

🧠 How It Works (AI-Driven Detection)

PhishGuard-AI uses a hybrid approach:

🔹 Machine Learning Model

Trained on phishing & legitimate samples

Predicts probability of phishing

Loaded using joblib

🔹 Rule-Based Checks

Suspicious keywords

URL patterns

Domain anomalies

🔹 Final Decision

AI prediction + rules are combined to generate:

✔ Safe

⚠ Suspicious

❌ Phishing

🏗️ Tech Stack

Backend: FastAPI

Language: Python 3.10+

AI/ML: Scikit-learn, Joblib

API Docs: Swagger UI (OpenAPI)

Testing: Postman / Browser

Deployment Ready: Docker / Cloud supported

📂 Project Structure
PhishGuard-AI/
│
├── app.py / main.py        # FastAPI main server
├── model/
│   └── phishing_model.pkl # Trained ML model
├── detector/
│   ├── ai_engine.py       # ML prediction logic
│   └── rules.py           # Rule-based checks
├── utils/
│   └── preprocess.py      # Text & URL cleaning
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/PhishGuard-AI.git
cd PhishGuard-AI

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Server
uvicorn app:app --reload

🌐 Swagger UI (API Testing)

After running server, open in browser:

http://127.0.0.1:8000/docs


Here you can:

Test URL phishing detection

Test email/text phishing detection

See API request & response format

🔍 Sample API Endpoints
✅ URL Check
POST /check-url


Input:

{
  "url": "http://secure-login-update.com"
}


Output:

{
  "result": "Phishing",
  "confidence": 0.94,
  "reason": "Suspicious domain pattern"
}

✅ Email/Text Check
POST /check-text


Input:

{
  "text": "Your account is suspended. Click here to verify."
}


Output:

{
  "result": "Suspicious",
  "confidence": 0.78,
  "reason": "Urgent language and malicious keywords detected"
}

🎯 Use Cases

🔐 Security awareness training

🧪 Cybersecurity labs

🤖 AI + Security research

🛡️ SOC automation testing

📚 Academic projects

🔮 Future Improvements

📊 Admin dashboard (Streamlit / React)

🗂️ Detection history logging

🌍 GeoIP scoring

📩 Email & Telegram alerts

🧠 Deep learning models

🧩 Browser extension integration

⚠️ Disclaimer

This project is for educational and research purposes only.
It should not be used as the only security layer in production environments.

👨‍💻 Author (Muhammad Sufyan Ayaz)

Developed as part of a cybersecurity and AI learning project
focused on AI-Driven Threat Detection Systems.