import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Title of the app
st.title('Machine Learning Analysis App')

# Option to upload a file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data.head())

    # Simple Linear Regression Model
    if st.button('Run Analysis'):
        if 'feature1' in data.columns and 'feature2' in data.columns and 'target' in data.columns:
            X = data[['feature1', 'feature2']]
            y = data['target']
            model = LinearRegression()
            model.fit(X, y)
            predictions = model.predict(X)
            data['Predictions'] = predictions
            st.write("Analysis Results:")
            st.write(data[['feature1', 'feature2', 'target', 'Predictions']])
        else:
            st.error("Columns 'feature1', 'feature2', and 'target' are required.")

# Option to enter data manually
st.subheader("Enter Data Manually")
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
target = st.number_input("Target", value=0.0)

if st.button('Submit Data'):
    input_data = pd.DataFrame([[feature1, feature2, target]], columns=['feature1', 'feature2', 'target'])
    st.write("Manual Data Submitted:")
    st.write(input_data)
