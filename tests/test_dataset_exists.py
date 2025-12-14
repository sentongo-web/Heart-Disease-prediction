import os


def test_dataset_present():
    assert os.path.exists(os.path.join(os.getcwd(), 'Heart_Disease_Prediction.csv'))
