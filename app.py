import streamlit as st
import pandas as pd
from src.auth import login
def main():
    st.title('Personal Finance Predictor (Student Edition)')

    # Login
    username, password = login()

    if username and password:
        # Load data and display
        df = pd.read_csv('data/sample_expenses.csv')
        st.dataframe(df)

        # Add more app functionalities here

if __name__ == '__main__':
    main()