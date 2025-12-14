# Results

This folder is intended to store experiment outputs, trained-model snapshots, evaluation metrics, and notebooks that support reproducibility.

Suggested structure:

- `results/<experiment-id>/model.joblib` — model artifact for that run
- `results/<experiment-id>/metrics.json` — evaluation metrics
- `results/<experiment-id>/notes.md` — short summary of hyperparameters and observations

When running experiments, create a new `results/<timestamp-or-id>/` directory and save artifacts there. Commit only non-sensitive summaries; large artifacts can be tracked with Git LFS if needed.
