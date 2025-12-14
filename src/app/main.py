import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import joblib
import pandas as pd


app = FastAPI(title="Heart Disease Predictor")


MODEL_FILE = os.path.join(os.getcwd(), 'models', 'model.joblib')
model = None
if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)


class Features(BaseModel):
    data: Dict[str, Any]


@app.get('/')
def root():
    return {"status": "ok", "message": "Send POST /predict with JSON {\"data\": {...}}"}


@app.post('/predict')
def predict(request: Features):
    global model
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available. Train the model first.")
    try:
        df = pd.DataFrame([request.data])
        pred = int(model.predict(df)[0])
        proba = model.predict_proba(df)[0].tolist() if hasattr(model, 'predict_proba') else None
        return {"prediction": pred, "probability": proba}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
