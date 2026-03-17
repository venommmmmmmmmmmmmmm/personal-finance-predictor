# Full Streamlit Dashboard Code
import streamlit as st
import sqlite3

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect('data/personal_finance.db')
    return conn

# Input Tab
def input_tab():
    st.title('Input Your Financial Data')
    # Your input form here

# Dashboard Tab
def dashboard_tab():
    st.title('Dashboard')
    # Dashboard visualizations here

# Report Tab
def report_tab():
    st.title('Financial Report')
    # Generate report here

# Main function
def main():
    st.sidebar.title('Navigation')
    option = st.sidebar.radio('Select Tab:', ['Input', 'Dashboard', 'Report'])

    if option == 'Input':
        input_tab()
    elif option == 'Dashboard':
        dashboard_tab()
    elif option == 'Report':
        report_tab()

if __name__ == '__main__':
    main()