# Heart Disease Prediction

A compact, reproducible machine learning project predicting heart disease from tabular clinical features. This repository is organized for research and demonstration: it contains exploratory data analysis, model training and evaluation code, a lightweight FastAPI inference app, and Docker support for deployment.

Project highlights
- **Dataset:** `Heart_Disease_Prediction.csv` (included in repo root)
- **Model:** scikit-learn pipeline saved to `models/model.joblib`
- **API:** FastAPI app at `src/app/main.py` for inference
- **Reproducibility:** training scripts in `src/models/` and EDA in `src/eda/`

Quick start
1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

2. Train the model (optional  repo includes a saved model):

```bash
python src/models/train.py
```

3. Run the API locally:

```bash
uvicorn src.app.main:app --host 0.0.0.0 --port 8000
```

4. Docker (build & run):

```bash
docker build -t heart-disease-app .
docker run -p 8000:80 heart-disease-app
```

Repository structure
- `Heart_Disease_Prediction.csv`  dataset (CSV)
- `src/eda/eda.py`  exploratory data analysis and summary
- `src/models/train.py`  training pipeline and model export
- `src/models/predict.py`  prediction helpers
- `src/app/main.py`  FastAPI application and inference endpoint
- `models/model.joblib`  trained model artifact (included)
- `reports/eda_summary.txt`  EDA notes and findings

Reproducibility & evaluation
- Training outputs (metrics, model artifacts) are produced by `src/models/train.py`.
- Check `reports/` for EDA findings and notes useful for reproducible research.

Good practices for research profile
- Add an explicit `results/` folder for experiment outputs and notebooks.
- Add a `Model Card` (short document describing dataset, training, evaluation, limitations).

Contributing
- Use branches for changes and open a PR with a clear description of experiments, hyperparameters and expected outcomes.

Contact & citation
- Author: sentongo-web
- If you use this work in a paper or portfolio, cite the repository and include dataset provenance.

License
- Add a license file (e.g., MIT) if you wish to make the code reusable for others.

For detailed instructions see the code in `src/` and the EDA notes in `reports/`.
