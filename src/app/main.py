import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd


app = FastAPI(title="Heart Disease Predictor")

# Allow requests from local UI / other origins during testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL_FILE = os.path.join(os.getcwd(), 'models', 'model.joblib')
model = None
if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)


# Pydantic model with aliases that match CSV column headers exactly
class InputFeatures(BaseModel):
    Age: int
    Sex: int
    chest_pain_type: int = Field(..., alias="Chest pain type")
    BP: float
    Cholesterol: float
    FBS_over_120: int = Field(..., alias="FBS over 120")
    EKG_results: int = Field(..., alias="EKG results")
    Max_HR: float = Field(..., alias="Max HR")
    Exercise_angina: int = Field(..., alias="Exercise angina")
    ST_depression: float = Field(..., alias="ST depression")
    Slope_of_ST: int = Field(..., alias="Slope of ST")
    Number_of_vessels_fluro: int = Field(..., alias="Number of vessels fluro")
    Thallium: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "Age": 63,
                "Sex": 1,
                "Chest pain type": 4,
                "BP": 150,
                "Cholesterol": 407,
                "FBS over 120": 0,
                "EKG results": 2,
                "Max HR": 154,
                "Exercise angina": 0,
                "ST depression": 4.0,
                "Slope of ST": 2,
                "Number of vessels fluro": 3,
                "Thallium": 7,
            }
        }


@app.get('/', response_class=HTMLResponse)
def root():
    # Serve the simple static UI if present
    index_path = os.path.join(os.getcwd(), 'src', 'app', 'static', 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            return HTMLResponse(f.read())
    return {"status": "ok", "message": "Send POST /predict with JSON matching model features"}


@app.post('/predict')
def predict(features: InputFeatures):
    global model
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available. Train the model first.")
    try:
        # Use aliases so DataFrame columns match training CSV headers
        data = features.dict(by_alias=True)
        df = pd.DataFrame([data])
        pred = int(model.predict(df)[0])
        proba = model.predict_proba(df)[0].tolist() if hasattr(model, 'predict_proba') else None
        return {"prediction": pred, "probability": proba}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Mount static files for the UI
static_dir = os.path.join(os.getcwd(), 'src', 'app', 'static')
if os.path.isdir(static_dir):
    app.mount('/static', StaticFiles(directory=static_dir), name='static')
