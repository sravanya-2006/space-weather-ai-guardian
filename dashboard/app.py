import streamlit as st
from prediction import predict_risk

st.set_page_config(
    page_title="Space Weather AI Guardian",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Space Weather AI Guardian")

st.markdown(
    "Predict Solar Flare Risk Levels using Machine Learning"
)

st.divider()

magnitude = st.number_input(
    "Magnitude",
    value=1.0
)

duration_minutes = st.number_input(
    "Duration Minutes",
    value=10.0
)

hour = st.slider(
    "Hour",
    0,
    23,
    12
)

day = st.slider(
    "Day",
    1,
    31,
    1
)

month = st.slider(
    "Month",
    1,
    12,
    1
)

year = st.number_input(
    "Year",
    value=2024
)

day_of_week = st.slider(
    "Day Of Week",
    0,
    6,
    0
)

flare_class_encoded = st.selectbox(
    "Flare Class",
    [0, 1, 2]
)

if st.button("Predict Risk"):

    prediction = predict_risk(
        magnitude,
        duration_minutes,
        hour,
        day,
        month,
        year,
        day_of_week,
        flare_class_encoded
    )

    risk_labels = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }

    st.success(
        f"Predicted Risk: {risk_labels[prediction]}"
    )