import streamlit as st
import pandas as pd
import random

def fetch_transactions(user_id, date_range):
    """Fetches mock transactions for a user within a given date range."""
    categories = ['Food', 'Rent', 'Entertainment', 'Transport', 'Utilities']
    transactions = []
    
    for i in range(10):  
        transactions.append({
            'date': pd.Timestamp('2025-03-01') - pd.Timedelta(days=random.randint(0, 30)),
            'category': random.choice(categories),
            'amount': round(random.uniform(5, 100), 2)
        })
    
    return pd.DataFrame(transactions)

def analyze_spending(category=None, time_period=30):
    """Analyzes spending trends based on category and time period."""
    df = fetch_transactions(user_id=1, date_range=time_period)
    if category:
        df = df[df['category'] == category]
    return df.groupby('category')['amount'].sum()

def suggest_budget_adjustments(income, expenses):
    """Suggests budget adjustments based on income and expenses."""
    savings = income - expenses
    if savings < 0:
        return f"You're overspending by ${-savings:.2f}. Consider reducing expenses."
    return f"You're saving ${savings:.2f} per month. Keep it up!"

def main():
    st.title("Budget Tracker & Expense Analyzer")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if not username or not password:
        st.warning("Please enter your username and password to continue.")
        return
    
    st.subheader("Add a Transaction")
    transaction_date = st.date_input("Date")
    transaction_category = st.selectbox("Category", ['Food', 'Rent', 'Entertainment', 'Transport', 'Utilities'])
    transaction_amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    
    if st.button("Add Transaction"):
        new_transaction = pd.DataFrame({
            'date': [transaction_date],
            'category': [transaction_category],
            'amount': [transaction_amount]
        })
        st.session_state['transactions'] = pd.concat([st.session_state.get('transactions', fetch_transactions(1, 30)), new_transaction], ignore_index=True)
    
    st.subheader("Recent Transactions")
    transactions = st.session_state.get('transactions', fetch_transactions(1, 30))
    transactions['date'] = pd.to_datetime(transactions['date'])  # Convert to datetime64 before displaying
    st.dataframe(transactions)
    
    st.subheader("Spending Analysis")
    category = st.selectbox("Select a category to analyze", [None] + list(transactions['category'].unique()))
    spending_summary = analyze_spending(category)
    st.bar_chart(spending_summary)
    
    st.subheader("Budget Suggestions")
    income = st.number_input("Enter your monthly income", min_value=0.0, format="%.2f")
    total_expenses = transactions['amount'].sum()
    budget_suggestion = suggest_budget_adjustments(income, total_expenses)
    st.write(budget_suggestion)
    
if __name__ == "__main__":
    main()
