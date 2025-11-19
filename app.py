import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("expresso_churn_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📱 Expresso Customer Churn Prediction App")
st.write("Predict whether a customer will churn based on input features.")

# Input fields for all features (ensure these match the columns in X_train)
REGION = st.number_input("REGION", min_value=0, value=0)
TENURE = st.number_input("TENURE", min_value=0, value=7)
MONTANT = st.number_input("MONTANT", min_value=0.0, value=3000.0)
FREQUENCE_RECH = st.number_input("FREQUENCE_RECH", min_value=0.0, value=7.0)
REVENUE = st.number_input("REVENUE", min_value=0.0, value=3000.0)
ARPU_SEGMENT = st.number_input("ARPU_SEGMENT", min_value=0.0, value=1000.0)
FREQUENCE = st.number_input("FREQUENCE", min_value=0.0, value=9.0)
DATA_VOLUME = st.number_input("DATA_VOLUME", min_value=0.0, value=250.0)
ON_NET = st.number_input("ON_NET", min_value=0.0, value=27.0)
ORANGE = st.number_input("ORANGE", min_value=0.0, value=29.0)
TIGO = st.number_input("TIGO", min_value=0.0, value=6.0)
ZONE1 = st.number_input("ZONE1", min_value=0.0, value=1.0)
ZONE2 = st.number_input("ZONE2", min_value=0.0, value=2.0)
MRG = st.number_input("MRG", min_value=0, value=0)
REGULARITY = st.number_input("REGULARITY", min_value=0, value=24)
TOP_PACK = st.number_input("TOP_PACK", min_value=0, value=0)
FREQ_TOP_PACK = st.number_input("FREQ_TOP_PACK", min_value=0.0, value=5.0)

# Prepare input data with all features in the correct order
input_data = pd.DataFrame({
    'REGION': [REGION],
    'TENURE': [TENURE],
    'MONTANT': [MONTANT],
    'FREQUENCE_RECH': [FREQUENCE_RECH],
    'REVENUE': [REVENUE],
    'ARPU_SEGMENT': [ARPU_SEGMENT],
    'FREQUENCE': [FREQUENCE],
    'DATA_VOLUME': [DATA_VOLUME],
    'ON_NET': [ON_NET],
    'ORANGE': [ORANGE],
    'TIGO': [TIGO],
    'ZONE1': [ZONE1],
    'ZONE2': [ZONE2],
    'MRG': [MRG],
    'REGULARITY': [REGULARITY],
    'TOP_PACK': [TOP_PACK],
    'FREQ_TOP_PACK': [FREQ_TOP_PACK]
})

# Apply scaler
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is likely to stay.")
