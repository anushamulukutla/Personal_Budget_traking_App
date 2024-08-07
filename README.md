# Personal Budget Tracker

## Overview

The Personal Budget Tracker is a Python application designed to help users manage their finances by tracking income, expenses, and budgets on a monthly basis. 
The application provides a graphical user interface (GUI) built with Tkinter, and it utilizes Matplotlib for visualizing financial data.

## Features

- **User Input Form:** Allows users to enter monthly income, additional income, and categorize expenses.
- **Income Tracking:** Records total monthly income from salary and additional sources.
- **Expense Tracking:** Tracks expenses across various categories like rent, fuel, groceries, etc.
- **Budget Management:** Enables users to set monthly budgets for different expense categories.
- **Data Storage:** Saves income, expenses, and budget details in CSV files for persistent storage.
- **Graphical Analysis:** Generates bar graphs and pie charts to compare actual expenses with the budget and analyze spending.
- **Data Validation:** Ensures all input fields are filled and contain valid data before saving.
- **Clear Entries:** Provides functionality to clear all input fields for new data entry.
- **Exit Application:** Allows users to exit the application safely.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pandas
- Matplotlib

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/personal-budget-tracker.git
    cd personal-budget-tracker
    ```

2. **Install the required packages:**
    ```sh
    pip install pandas matplotlib
    ```

## Usage

1. **Run the application:**
    ```sh
    python personal_budget_tracker.py
    ```

2. **Enter your income:**
    - Input total salary and additional income.
    - Select the month.
    - Click on `Submit Income`.

3. **Record your expenses:**
    - Enter the date, month, category, and expense amount.
    - Click on `Submit Expenses`.

4. **Set your budget:**
    - Select the month and category.
    - Enter the budget amount.
    - Click on `Submit Budget`.

5. **Visualize your spending:**
    - Select the month.
    - Click on `Actual vs Budget` to see a bar graph comparison.
    - Click on `Spending Analysis` to see a pie chart of your spending.

6. **Clear entries:**
    - Click on `Clear Entry` to reset all input fields.

7. **Exit the application:**
    - Click on `Exit` to close the application.

## File Structure

- **personal_budget_tracker.py:** The main Python script containing the application code.
- **category_budgets.csv:** CSV file storing the budget data.
- **{month}_expenses.csv:** CSV files storing the expense data for each month.

## Functions

- **Money_In_Frame():** Collects user input for income details.
- **write_money_in_csv():** Saves income data to a CSV file.
- **Money_out_frame():** Collects user input for expense details.
- **write_money_out_csv():** Saves expense data to a CSV file.
- **clear_function():** Clears all input fields.
- **write_category_budget_to_csv():** Saves budget data to a CSV file.
- **check_month_category_budget_exists(month, category):** Checks if budget for the month and category already exists.
- **generate_graph_actual_budget(month):** Generates a bar graph comparing actual expenses vs. budget.
- **generate_pie_chart(month):** Generates a pie chart of spending categories.
- **exit_application():** Exits the application.

## Screenshots

- **You can find the Screenshots of the project in ProjectReport_AnushaMulukutla .pdf
## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) for data visualization.
