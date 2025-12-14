# Model Card — Heart Disease Prediction

## Model Details
- **Name:** Heart Disease Classifier
- **Version:** v1
- **Authors / Provider:** sentongo-web
- **Model type:** scikit-learn classification pipeline
- **File:** `models/model.joblib`

## Intended use
- **Primary use case:** Assistive screening for heart disease risk from structured clinical attributes (tabular CSV). Intended for research, demonstration and educational purposes.
- **Users:** Researchers, students, demonstrators.
- **Out-of-scope:** Clinical diagnosis, treatment decisions. Not to be used as a sole basis for medical decisions.

## Data
- **Training data:** `Heart_Disease_Prediction.csv` included in repository root.
- **Features:** clinical attributes included in the CSV (see `src/eda/eda.py` for preprocessing and feature engineering).
- **Labels:** binary heart disease presence/absence (as prepared in training script).

## Evaluation
- **Evaluation script:** `src/models/train.py` produces metrics when run.
- **Recommended metrics to report:** accuracy, precision, recall, F1, ROC AUC, confusion matrix.

## Ethical considerations & Limitations
- The dataset may not represent global populations — performance can degrade on underrepresented groups.
- Model may encode biases present in training data (e.g., age, sex, ethnicity distributions). Evaluate fairness before deployment.
- No clinical validation performed; intended for research only.

## Maintenance & reproducibility
- Retrain using `python src/models/train.py` and record hyperparameters and random seeds in `results/`.
- Save experiment outputs and evaluation artifacts under `results/` for reproducibility.

## Contact
- For questions about the model and experiments contact repository owner: sentongo-web
