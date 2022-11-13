from pathlib import Path
import numpy as np
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent

model = pickle.load(open(BASE_DIR/"disease_prediction/prediction_model.pkl", "rb"))


def predict(id):
    return model.predict(np.array([id], dtype='object'))

