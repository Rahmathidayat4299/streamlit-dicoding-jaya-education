import streamlit as st
import pandas as pd
import numpy as np
import joblib  # gunakan pickle jika model disimpan dengan pickle

st.write('Hi!')


# Load model
@st.cache_resource
def load_model():
    model = joblib.load('model/student_status_model.pkl')
    return model

model = load_model()

st.title("Akses Model Machine Learning")

st.write("Model berhasil dimuat!")
st.write(model)
