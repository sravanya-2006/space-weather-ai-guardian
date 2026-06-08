import joblib
import numpy as np

model = joblib.load("models/risk_model.pkl")

def predict_risk(
    magnitude,
    duration_minutes,
    hour,
    day,
    month,
    year,
    day_of_week,
    flare_class_encoded
):

    data = np.array([
        [
            magnitude,
            duration_minutes,
            hour,
            day,
            month,
            year,
            day_of_week,
            flare_class_encoded
        ]
    ])

    prediction = model.predict(data)

    return prediction[0]