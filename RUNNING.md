# How to run and test the Heart Disease Predictor

This document explains how to run the app locally and with Docker, and how to test it. Use the Docker instructions for the easiest way to share the app with others.

## Requirements
- Docker (recommended)
- Python 3.10+ and `pip` (optional, for local run)

## Run with Docker (recommended)

1. Build the image (run from repository root):

```powershell
docker build -t heart-disease-prediction:latest -f Dockerfile .
```

2. Start the container mapping host port `8080` to the container port the app listens on (`80`):

```powershell
docker run -d --name hdp_app -p 8080:80 heart-disease-prediction:latest
```

3. Open the UI in your browser:

```
http://localhost:8080/
```

4. View logs:

```powershell
docker logs -f hdp_app
```

5. Stop and remove the container:

```powershell
docker rm -f hdp_app
```

Notes:
- The app inside the container listens on port `80`. Map host ports accordingly (e.g., `-p 8080:80`).

## Run locally without Docker

1. Create and activate a virtual environment:

Windows (PowerShell):
```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app with Uvicorn (from repository root):

```bash
python -m uvicorn src.app.main:app --host 0.0.0.0 --port 8080 --reload
```

4. Open `http://localhost:8080/` in your browser.

## API endpoints (use these for automated testing)

- GET `/` — returns the UI (index.html) or a status message.
- POST `/predict` — accepts JSON matching the model features and returns a prediction.

### Sample `POST /predict` request (curl)

```bash
curl -s -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{
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
    "Thallium": 7
  }'
```

Response example:

```json
{"prediction": 1, "probability": [0.12, 0.88]}
```

## Share and push to GitHub

If you want to publish this `RUNNING.md` file to GitHub, run:

```powershell
git add RUNNING.md
git commit -m "Add RUNNING.md with run and test instructions"
git push origin main
```

If your repository uses a different branch, replace `main` with your branch name.

---
If you want, I can commit and push this file for you now (I will create the commit and push to `origin main`).
