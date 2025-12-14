install:
	pip install -r requirements.txt

train:
	python src/models/train.py

run:
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000
