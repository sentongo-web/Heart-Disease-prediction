# Model Card — Heart Disease Prediction

## Model Details
- **Name:** Heart Disease Classifier
- **Version:** v1
- **Authors / Provider:** sentongo-web
- **Model type:** scikit-learn classification pipeline (preprocessing + LogisticRegression)
- **File:** `models/model.joblib`

## Intended use
- **Primary use case:** Assistive screening for heart disease risk from structured clinical attributes (tabular CSV). Intended for research, demonstration and educational purposes.
- **Users:** Researchers, students, demonstrators.
- **Out-of-scope:** Clinical diagnosis or treatment decisions. Not to be used as a sole basis for medical care.

## Data and Features (exact column names)
The model expects the following columns (exact names as headers in `Heart_Disease_Prediction.csv`):

- Age (numeric)
- Sex (numeric; 1 = male, 0 = female in this dataset)
- Chest pain type (numeric code)
- BP (blood pressure; numeric)
- Cholesterol (numeric)
- FBS over 120 (numeric; 1 = true, 0 = false)
- EKG results (numeric code)
- Max HR (numeric)
- Exercise angina (numeric; 1 = yes, 0 = no)
- ST depression (numeric)
- Slope of ST (numeric code)
- Number of vessels fluro (numeric)
- Thallium (numeric code)

The target column in the CSV is `Heart Disease` (values in the repository are `Presence` / `Absence` and are normalized to 1/0 during training).

## Sample input (JSON) and types
Example JSON payload representing a single patient (keys must match the column names exactly):

```json
{
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
}
```

## Quick example — load model and predict (Python)
```python
import pandas as pd
import joblib

# load trained pipeline
model = joblib.load('models/model.joblib')

# create a DataFrame with one row; column names must match exactly
sample = {
		'Age': 63,
		'Sex': 1,
		'Chest pain type': 4,
		'BP': 150,
		'Cholesterol': 407,
		'FBS over 120': 0,
		'EKG results': 2,
		'Max HR': 154,
		'Exercise angina': 0,
		'ST depression': 4.0,
		'Slope of ST': 2,
		'Number of vessels fluro': 3,
		'Thallium': 7
}
df = pd.DataFrame([sample])
pred = model.predict(df)
proba = model.predict_proba(df) if hasattr(model, 'predict_proba') else None
print('prediction (0=Absence,1=Presence):', pred[0])
if proba is not None:
		print('probabilities:', proba[0].tolist())
```

## Evaluation
- Use `python src/models/train.py` to reproduce training and evaluation metrics. Save outputs under `results/<experiment-id>/`.

## Ethical considerations & limitations
- Dataset coverage and demographic representation are limited; model performance can degrade on underrepresented subgroups.
- No clinical validation — do not use for real patient decision-making.

## Reproducibility
- Retrain with `python src/models/train.py` and store experimental metadata (seed, split, hyperparameters) in `results/`.

## Contact
- Repository owner: sentongo-web
