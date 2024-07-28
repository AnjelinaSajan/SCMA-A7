import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate sample data
def generate_sample_data():
    np.random.seed(42)  # For reproducibility
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Category': np.random.choice(['Food', 'Entertainment', 'Bills', 'Travel', 'Other'], 100),
        'Amount': np.random.uniform(10, 100, 100)
    })
    return data

# Generate sample data
data = generate_sample_data()

# Title of the dashboard
st.title('Personal Finance Dashboard')

# Dashboard description
st.write("""
This dashboard allows you to track and visualize your personal finances, 
including expenses, savings, investments, and debts. Navigate through the different sections 
using the sidebar to gain insights into your financial health.
""")

# Sidebar for navigation
st.sidebar.header('Navigation')
section = st.sidebar.selectbox('Select Section', [
    'Home', 'Expense Breakdown', 'Savings Tracker', 'Investment Analysis', 'Debt Management'])

if section == 'Home':
    st.header('Welcome to Your Personal Finance Dashboard')
    st.write("""
    Use this dashboard to get a comprehensive overview of your finances. 
    Track your spending, monitor your savings, analyze your investments, and manage your debts effectively.
    """)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyUWeEQFZEgkldDWfNB4NpgAx8N8EA53jvGA&s", caption='Finance Dashboard')

elif section == 'Expense Breakdown':
    st.subheader('Expense Breakdown')
    st.write("Track how you spend your money across different categories.")
    category_expense = data.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots()
    category_expense.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

elif section == 'Savings Tracker':
    st.subheader('Savings Tracker')
    st.write("Monitor your savings over time to ensure you're meeting your financial goals.")
    savings_data = pd.DataFrame({
        'Month': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'Savings': np.random.uniform(200, 1000, 12)
    })
    fig, ax = plt.subplots()
    sns.lineplot(x='Month', y='Savings', data=savings_data, ax=ax)
    ax.set_title('Savings Over Time')
    st.pyplot(fig)

elif section == 'Investment Analysis':
    st.subheader('Investment Portfolio Analysis')
    st.write("Analyze the distribution of your investment portfolio.")
    investment_data = pd.DataFrame({
        'Asset': ['Stocks', 'Bonds', 'Real Estate', 'Commodities'],
        'Value': [5000, 3000, 2000, 1000]
    })
    fig, ax = plt.subplots()
    sns.barplot(x='Asset', y='Value', data=investment_data, ax=ax)
    ax.set_title('Investment Portfolio Distribution')
    st.pyplot(fig)

elif section == 'Debt Management':
    st.subheader('Debt Management')
    st.write("Manage your debts and keep track of outstanding amounts.")
    debt_data = pd.DataFrame({
        'Debt Type': ['Credit Card', 'Student Loan', 'Mortgage', 'Auto Loan'],
        'Amount': [2000, 15000, 30000, 10000]
    })
    fig, ax = plt.subplots()
    sns.barplot(x='Debt Type', y='Amount', data=debt_data, ax=ax)
    ax.set_title('Debt Distribution')
    st.pyplot(fig)
