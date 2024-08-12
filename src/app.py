import streamlit as st
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

#Load the pre-trained model
model = joblib.load('logistic_model.pk1')


#Define the input fields
def user_input_features():
    st.sidebar.header('User Input Features')
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', ['Yes', 'No'])
    tenure = st.sidebar.slider('Tenure (months)', 0, 72, 12)
    MonthlyCharges = st.sidebar.slider('Monthly Charges ($)', 20.0 150.0, 70.0)
    TotalCharges = st.sidebar.slider('Total Charges ($)', 0.0, 8000.0, 500.0)
    Contract = st.sidebar.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
    PaymentMethod = st.sidebar.selectionbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'])


    data = {
        'Gender': gender,
        'Senior Citizen': SeniorCitizen,
        'Tenure': tenure,
        'Monthly Charges': MonthlyCharges,
        'Total Charges': TotalCharges,
        'Contract Type': Contract,
        'Payment Method': PaymentMethod,
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()


#Make prediction
predicition = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.write(f"Prediction:  {'Churn' if prediction[0] else 'No Churn'}")
st.write(f"Prediction Probability:  {prediction_proba[0]}")



if __name__ == "__main__":
    main()