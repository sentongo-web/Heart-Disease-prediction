import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib


def main(csv_path=None, out_dir="models"):
    if csv_path is None:
        csv_path = os.path.join(os.getcwd(), "Heart_Disease_Prediction.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at {csv_path}")

    df = pd.read_csv(csv_path)
    # detect target column (allow variants like 'Heart Disease')
    target_col = None
    for cand in ['HeartDisease', 'Heart Disease', 'Heart_Disease', 'target', 'Target']:
        if cand in df.columns:
            target_col = cand
            break
    if target_col is None:
        raise ValueError("Target column not found in dataset. Expected one of: HeartDisease, 'Heart Disease', Heart_Disease, target")

    X = df.drop(target_col, axis=1)
    y = df[target_col]

    # normalize target values to 0/1
    if y.dtype == object or y.dtype.name == 'category':
        y_str = y.astype(str).str.strip().str.lower()
        if set(y_str.unique()) <= { 'presence', 'absence' }:
            y = y_str.map({'presence': 1, 'absence': 0})
        else:
            # try numeric strings
            try:
                y = y_str.astype(int)
            except Exception:
                raise ValueError(f"Unexpected categorical target values: {y_str.unique()}")

    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
    ])

    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)

    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'model.joblib')
    joblib.dump(model, out_path)
    print(f"Model trained and saved to {out_path}")


if __name__ == '__main__':
    main()
