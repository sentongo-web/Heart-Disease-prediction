import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join(os.getcwd(), 'models', 'model.joblib')


def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}. Run training first.")
    return joblib.load(path)


def predict_from_dict(input_dict):
    model = load_model()
    df = pd.DataFrame([input_dict])
    proba = model.predict_proba(df)[0].tolist() if hasattr(model, 'predict_proba') else None
    pred = int(model.predict(df)[0])
    return {"prediction": pred, "probability": proba}
