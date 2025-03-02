# Budget Tracker & Expense Analyzer

The **Budget Tracker & Expense Analyzer** is a Streamlit-based web application designed to help users monitor their spending habits, analyze trends, and receive recommendations for better financial management. Users can log transactions, categorize expenses, and get insights into their monthly savings or overspending. The tool is built using Python and incorporates Pandas for data handling, Streamlit for the user interface, and Pytest for testing functionalities.

## Features
- **User Authentication**: Requires users to enter a username and password to access their financial records.
- **Transaction Logging**: Users can manually enter transactions with a date, category, and amount.
- **Spending Analysis**: A bar chart visualization helps users see their spending distribution across categories.
- **Budget Adjustment Recommendations**: Based on income and expenses, the app provides insights into financial well-being and suggests adjustments.
- **Data Persistence**: Transactions persist during the session, allowing continuous tracking without data loss.

## File Structure
### `project.py`
This is the core file that contains the main logic of the application. It includes:
1. **`fetch_transactions(user_id, date_range)`**: Simulates fetching financial transactions based on a given time range.
2. **`analyze_spending(category, time_period)`**: Computes total spending per category over a given period and returns a summary.
3. **`suggest_budget_adjustments(income, expenses)`**: Evaluates user income versus expenses and provides recommendations on savings or spending reductions.
4. **`main()`**: Implements the Streamlit user interface, handling user inputs, transactions, visualizations, and budget suggestions.

### `test_project.py`
This file contains Pytest-based unit tests to ensure the reliability of core functionalities:
- `test_fetch_transactions()`: Verifies that the function returns a non-empty DataFrame with correct columns.
- `test_analyze_spending()`: Ensures spending analysis correctly summarizes expenses per category.
- `test_suggest_budget_adjustments()`: Confirms that budget recommendations vary correctly depending on income and spending levels.

### `requirements.txt`
Lists all dependencies required to run the project:
- **streamlit**: Provides the UI framework.
- **pandas**: Handles transaction data storage and analysis.
- **pytest**: Enables unit testing.
- **pyarrow**: Facilitates DataFrame operations in Streamlit.

## Design Considerations
### User Authentication
A basic authentication system was implemented requiring a username and password before accessing the app. While it doesn’t store user credentials persistently, it serves as a minimal security barrier to ensure session uniqueness.

### Transaction Entry and Persistence
To allow users to log transactions dynamically, we used **Streamlit’s session state** to maintain user-entered transactions. This prevents data loss when interacting with the interface.

### Budget Analysis and Visualization
For intuitive insights, a **bar chart visualization** was included to help users quickly understand their expense distribution. 

## AI Usage and Academic Integrity
For this final project, AI-based tools such as ChatGPT, GitHub Copilot, CS50 duck, and Bing Chat were used as **assistive tools** to improve productivity. However, the **core implementation, structure, and logic of this project remain the user’s own work**. AI tools were utilized for:
- Generating function structures and documentation.
- Debugging issues related to Pandas and Streamlit.
- Refining code efficiency and readability.

All AI-assisted code has been reviewed and integrated in accordance with academic integrity guidelines. 

## Future Enhancements
While the project provides core budgeting functionalities, potential improvements include:
- **Database Integration**: Implementing SQLite or Firebase for persistent transaction storage.
- **User Authentication with Sessions**: Enabling secure, user-specific accounts.
- **Expense Forecasting**: Using predictive analytics to suggest future budgets based on past transactions.

## Running the Project
To run this project locally, follow these steps:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run project.py
   ```

## Conclusion
The **Budget Tracker & Expense Analyzer** is a user-friendly financial tracking application that offers real-time transaction logging, analysis, and budgeting recommendations. It serves as an effective tool for individuals looking to improve their financial habits while also demonstrating the power of Python, Streamlit, and Pandas in building interactive applications. The project is structured to allow future expansion, making it a great starting point for more advanced personal finance management solutions.

