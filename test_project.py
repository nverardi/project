import pytest
import pandas as pd
from project import fetch_transactions, analyze_spending, suggest_budget_adjustments

def test_fetch_transactions():
    transactions = fetch_transactions(user_id=1, date_range=30)
    assert isinstance(transactions, pd.DataFrame)
    assert not transactions.empty
    assert all(col in transactions.columns for col in ['date', 'category', 'amount'])

def test_analyze_spending():
    transactions = fetch_transactions(user_id=1, date_range=30)
    category = transactions['category'].iloc[0]  # Select a valid category
    spending_summary = analyze_spending(category)
    assert isinstance(spending_summary, pd.Series)
    assert not spending_summary.empty

def test_suggest_budget_adjustments():
    result = suggest_budget_adjustments(5000, 4500)
    assert "You're saving" in result
    
    result = suggest_budget_adjustments(4000, 4500)
    assert "You're overspending" in result
