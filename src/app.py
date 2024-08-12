import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#telecom_churn = pd.DataFrame()
df = pd.read_csv("/Users/jeff/Documents/assignments/churn_rates_and_root_causes/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

#Streamlit code to create the web app
st.title('Churn Rates and Root Causes')


if 'df' in locals():
    st.write('Data:')
    st.dataframe(df)


if __name__ == "__main__":
    main()