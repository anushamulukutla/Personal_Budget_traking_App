
Personal Budget Tracker
Overview
The Personal Budget Tracker is a Python application that allows users to track their income, expenses, and budget for each month. It provides functionality to record and save monthly incomes, expenses, and budgets, as well as visualize the data through graphs and pie charts.

Features
Record monthly income and additional income.
Track monthly expenses across various categories.
Set and save monthly budgets for different categories.
Generate bar graphs to compare actual expenditure vs. budget.
Generate pie charts to analyze spending by category.
Clear entries and reset the input fields.
User-friendly GUI using Tkinter.
Save data to CSV files for persistent storage.
Prerequisites
Python 3.x
Required Python libraries: tkinter, pandas, matplotlib
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/personal-budget-tracker.git
cd personal-budget-tracker
Install required Python libraries:

sh
Copy code
pip install pandas matplotlib
Usage
Run the application:

sh
Copy code
python personal_budget_tracker.py
Enter your income:

Input total salary and additional income.
Select the month.
Click on Submit Income.
Record your expenses:

Enter the date, month, category, and expense amount.
Click on Submit Expenses.
Set your budget:

Select the month and category.
Enter the budget amount.
Click on Submit Budget.
Visualize your spending:

Select the month.
Click on Actual vs Budget to see a bar graph comparison.
Click on Spending Analysis to see a pie chart of your spending.
Clear entries:

Click on Clear Entry to reset all input fields.
Exit the application:

Click on Exit to close the application.
File Structure
personal_budget_tracker.py: Main application script.
category_budgets.csv: CSV file storing the budget data.
{month}_expenses.csv: CSV files storing the expense data for each month.

Contributing
Fork the repository.
Create a new branch: git checkout -b feature-branch
Make your changes and commit them: git commit -m 'Add feature'
Push to the branch: git push origin feature-branch
Open a pull request.

Acknowledgements
Tkinter for the GUI framework.
Pandas for data manipulation.
Matplotlib for data visualization.
