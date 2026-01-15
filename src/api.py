# src/api.py
import os
import joblib
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="PhishGuard AI", version="1.0.0")


class EmailIn(BaseModel):
    text: str


# Project root (phishguard-ai/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.joblib")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)
templates.env.auto_reload = True
templates.env.cache = {}


@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at: {MODEL_PATH}. Run training to create models/phishing_model.joblib"
        )
    model = joblib.load(MODEL_PATH)
    print("✅ Model loaded:", MODEL_PATH)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "host": "127.0.0.1:8000"},
    )


@app.post("/predict")
def predict(payload: EmailIn):
    text = payload.text.strip()

    pred = int(model.predict([text])[0])

    proba = None
    if hasattr(model, "predict_proba"):
        proba = float(model.predict_proba([text])[0][1])

    return {"is_phishing": bool(pred), "phishing_probability": proba}
