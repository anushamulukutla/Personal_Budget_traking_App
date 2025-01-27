import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt

'''fucntion to get the values entered for Money In Frame 
it returns a tuple month and Total income '''
def Money_In_Frame():
    try:
        Total_sal = float(Total_sal_entry.get())
        Additional_income = float(Additional_income_entry.get())
        Total_income = Total_sal + Additional_income
        month = month_income_var.get()
        if not month or not Total_sal or not Additional_income:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return None
        return month, Total_income #it returns tuple
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for salary and income")
        return None

''' Funcitons write the date to a month specified  csv file eg:jan.csv writes the data    '''

def write_money_in_csv():
    Money_In_data = Money_In_Frame()
    if Money_In_data:
        month, Total_income = Money_In_data#unpacking tuple
        filename = f"{month}.csv"
        with open(filename, "a", newline='') as Money_infile:
            writer = csv.writer(Money_infile)
            writer.writerow([month, Total_income])
        messagebox.showinfo("Success", "MONTHLY INCOME RECORDED SUCCESSFULLY!!!")

"""Function is created ti return category, date and expenditure for Money_out_Frame        """

def Money_out_frame(): #expenses
    category = category_var.get()
    date = entry_date.get()
    month = month_ex_var.get()
    expenditure = entry_expenditure.get()
    if not (category and date and month and expenditure):
        messagebox.showwarning("Input Error", "PLEASE FILL IN ALL FIELDS")
        return None
    try:
        expenditure = float(expenditure)
        return category, date, month, expenditure #it returns a tuple
    except ValueError:
        messagebox.showerror("Input Error", "Expenditure should be a numeric value")
        return None

'''Function writes the data expenses.csv file for Money_out_Frame     '''
def write_money_out_csv():
    Money_out_data = Money_out_frame()
    if Money_out_data:
        category, date, month, expenditure = Money_out_data
        filename = f"{month}_expenses.csv"
        with open(filename, "a", newline='') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow([date, month, category, expenditure])
        messagebox.showinfo("Success", "EXPENSES RECORDED SUCCESSFULLY!!!")

'''Function is created to clear all the entries fro all the Frames i.e Money_In_Frame ,Money_outFrame , Budget Frame       '''

def clear_function():
    Total_sal_entry.delete(0, tk.END)
    Additional_income_entry.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_date.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
    entry_expenditure.delete(0, tk.END)
    category_var.set("")
    month_var.set(" ")
    month_income_var.set(" ")
    month_budget_var.set(" ")
    category_budget_var.set(" ")
    budget_entry.delete(0, tk.END)


'''  Function is created for Budget Frame .In this function it gets the values 
         entered by user in the GUI and Stores to  category_budgets.csv  i.e month,category and Budget_amount, added some
         validation for Budget_Amount if the user enters the wrong value , A window will popup will error message window...'''
#BugetFrame
def write_category_budget_to_csv():
    month = month_budget_var.get()
    category = category_budget_var.get()
    budget_amount = budget_entry.get()
    if not (month and category and budget_amount):
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return None
    try:
        budget_amount = float(budget_amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the budget")
        return None
    #calling the function to check weather selected month and cat exist
    if check_month_category_budget_exists(month, category):
        messagebox.showinfo("Info", f"The Budget for {category} in Month {month} is Already Set!!")
        return None
    filebudget = "category_budgets.csv"
    with open(filebudget, "a", newline='') as budgetfile:
        writer = csv.writer(budgetfile)
        writer.writerow([month, category, budget_amount])
    messagebox.showinfo("Success", "Monthly budget for category successfully set!")


'''Function is created to check if the user is adding budget for same month again and again i
  if the user the select same month and category it throws an error window saying YOU HAVE ALREADY RECORDED BUDGET FOR THIS MONTH'''

def check_month_category_budget_exists(month, category):
    try:
        with open("category_budgets.csv", "r", newline='') as budgetfile:
            reader = csv.reader(budgetfile)
            for row in reader:
                if len(row) < 2:
                    continue  #here it skips the rows which don't have atleast 2 col
                if row[0] == month and row[1] == category:
                    return True
    except FileNotFoundError:
        with open("category_budgets.csv", "w", newline='') as budgetfile:
            writer = csv.writer(budgetfile)
            writer.writerow(["Month", "Category", "Budget"]) #giving headers if file not found
        return False#so here the function returns false indicating that no entry was found
    return False#If the loop completes without finding a match,
    # the function returns False, indicating that no entry for the
    # specified month and category exists.

def generate_graph_actual_budget(month):
    try:
        # reading csv file into data frames by giving manual header for df_budget and df_expenses
        df_budget = pd.read_csv('category_budgets.csv', names=['Month', 'Category', 'Budget'], header=None)
        df_expenses = pd.read_csv(f'{month}_expenses.csv', names=['Date', 'Month', 'Category', 'Amount'], header=None)

        #filtering data for specidied month .Where Month col mateches the specified month
        df_budget_month = df_budget[df_budget['Month'].str.strip().str.capitalize() == month.capitalize()]
        df_expenses_month = df_expenses[df_expenses['Month'].str.strip().str.capitalize() == month.capitalize()]

        #merging the two data frames it merges the category and add suffix for Month_spent and Month_budget
        #outer: Includes all categories from both dataframes. If a category is present in only one dataframe, the missing values for that category will be filled with NaN.
        df_merged = pd.merge(df_budget_month, df_expenses_month, on='Category', suffixes=('_Budget', '_Spent'), how='outer').fillna(0)
        # Set index to 'Category' for better plotting control
        df_merged.set_index('Category', inplace=True)

        #plotting for bar graph for side by side bars to compare Actual vs Buget
        ax = df_merged[['Budget', 'Amount']].plot(kind='bar', color=['skyblue', 'orange'], width=0.8, position=0.5)
        plt.title(f'Budget vs Actual Expenditure for {month}')
        plt.xlabel('Category')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.legend(["Budget", "Spent"])
        plt.tight_layout()
        plt.show()

    except FileNotFoundError as e:
        messagebox.showinfo("Error", f"Data file missing: {str(e)}")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")

def generate_pie_chart(month):
    try:
        #reading csv file into data frames by giving manual header for df_budget and df_expenses
        df_budget = pd.read_csv('category_budgets.csv', names=['Month', 'Category', 'Budget'], header=None)
        df_expenses = pd.read_csv(f'{month}_expenses.csv', names=['Date', 'Month', 'Category', 'Amount'], header=None)

        # filtering data for specidied month .Where Month col mateches the specified month
        df_budget_month = df_budget[df_budget['Month'].str.strip().str.capitalize() == month.capitalize()]
        df_expenses_month = df_expenses[df_expenses['Month'].str.strip().str.capitalize() == month.capitalize()]

        # Merge the budget and expenses data on Category
        df_merged = pd.merge(df_budget_month, df_expenses_month, on='Category', suffixes=('_Budget', '_Spent'), how='outer').fillna(0)

        #Cal on spending
        df_merged['Difference'] = df_merged['Amount'] - df_merged['Budget']
        df_merged['Difference'] = df_merged['Difference'].abs()  #take the absolute value

        # Prepare data for the pie chart
        labels = df_merged['Category']
        sizes = df_merged['Difference']
        colors = ['red' if x > df_merged['Budget'][i] else 'green' for i, x in enumerate(df_merged['Amount'])]

        # Plotting the pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(f' {month} Expenses Summary') #March Expense Summary
        plt.show()

    except FileNotFoundError as e:
        messagebox.showinfo("Error", f"Data file missing: {str(e)}")
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")
#Function helps User to Exit from the application
def exit_application():
    window.quit()

'''CREATING THE MAIN WINDOW !!!!'''
window = tk.Tk()
window.title("PERSONAL BUDGET TRACKER")
window.geometry("900x800")
window.configure(background="blue")
# Create a style object and configure styles for TFrame and TButton
style = ttk.Style()
style.configure("TFrame", background="Black")
style.configure("TButton", background="Red", font=('Arial', 10))
#Grid configuration
window.grid_columnconfigure(1, weight=1)
""" LABELING THE WINDOW   """
label_top = ttk.Label(window, text="PERSONAL BUDGET_Final", font=("Arial", 16, 'bold'))
label_top.grid(row=0, column=0, columnspan=2, sticky='ew', pady=20)
#Money_in_Frame
money_in_frame = ttk.Frame(window,style='TFrame', padding="10", relief="sunken", borderwidth=2)
money_in_frame.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)
money_in_label=ttk.Label(money_in_frame,text="Income",font=("Arial", 16, 'bold'))
money_in_label.grid(row=0,column=0,columnspan=2,sticky='w',pady=0)
#Money_outFrame
money_out_frame = ttk.Frame(window, padding="10", relief="sunken", borderwidth=2)
money_out_frame.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)
money_out_label=ttk.Label(money_out_frame,text="Expenses",font=("Arial", 16, 'bold'))
money_out_label.grid(row=0,column=0,columnspan=2,sticky='w',pady=0)
#BugetFrame
budget_frame = ttk.Frame(window, padding="10", relief="sunken", borderwidth=2)
budget_frame.grid(row=2, column=0, sticky='nsew', padx=20, pady=20)
budget_label=ttk.Label(budget_frame,text="Budget",font=("Arial", 16, 'bold'))
budget_label.grid(row=0,column=0,columnspan=2,sticky='w',pady=0)
# Graph Frame setup
graph_frame = ttk.Frame(window, padding="10", relief="sunken", borderwidth=2)
graph_frame.grid(row=2, column=1, sticky='nsew', padx=20, pady=20)
graph_label = ttk.Label(graph_frame, text="Spending Analysis", font=("Arial", 16, 'bold'))
graph_label.grid(row=0, column=0, columnspan=2, sticky='w', pady=0)


#widgets for Money_In
#Total salary -Inputfield
Total_sal_label = ttk.Label(money_in_frame, text="Total Salary:")
Total_sal_label.grid(row=1, column=0, sticky='w', padx=5, pady=2)
Total_sal_entry = ttk.Entry(money_in_frame)
Total_sal_entry.grid(row=1, column=1, padx=5, pady=2)
#Additional Income -Inputfield
Additional_income_label = ttk.Label(money_in_frame, text="Additional Income:")
Additional_income_label.grid(row=2, column=0, sticky='w', padx=5, pady=2)
Additional_income_entry = ttk.Entry(money_in_frame)
Additional_income_entry.grid(row=2, column=1, padx=5, pady=2)
#Select Month Input field
month_dropdown_options=[
    " ","January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
month_label = ttk.Label(money_in_frame, text="Month:")
month_label.grid(row=3, column=0, sticky='w', padx=5, pady=2)
month_income_var = tk.StringVar()
month_dropdown = ttk.Combobox(money_in_frame, textvariable= month_income_var, values=month_dropdown_options, state="readonly")
month_dropdown.grid(row=3, column=1, padx=5, pady=2)
month_dropdown.current(0)
#submit Button for MoneyIn frame
submit_button = ttk.Button(money_in_frame, text="Submit Income", command=write_money_in_csv)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)
submit_button.configure(style='TButton')
# Money Out Frame Widgets
#date -inputfield
date_label = ttk.Label(money_out_frame, text="Date:")
date_label.grid(row=1, column=0, sticky='w', padx=5, pady=2)
entry_date = ttk.Entry(money_out_frame)
entry_date.grid(row=1, column=1, padx=5, pady=2)
entry_date.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
#month-Input field
month_ex_label = ttk.Label(money_out_frame, text="Month:")
month_ex_label.grid(row=2, column=0, sticky='w', padx=5, pady=2)
month_ex_var = tk.StringVar()
month_ex_dropdown = ttk.Combobox(money_out_frame, textvariable=month_ex_var, values=month_dropdown_options, state="readonly")
month_ex_dropdown.grid(row=2, column=1, padx=5, pady=2)
month_ex_dropdown.current(0)
#Category -input field
category_list_dropdown=[" ","RENT/EMI","Fuel","groceries","Food","Shopping","Creditcard bill",'hydro']
category_label = ttk.Label(money_out_frame, text="Category:")
category_label.grid(row=3, column=0, sticky='w', padx=5, pady=2)
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(money_out_frame, textvariable=category_var, values=category_list_dropdown, state="readonly")
category_dropdown.grid(row=3, column=1, padx=5, pady=2)
category_dropdown.current(0)
#Expenditure -input field
expenditure_label = ttk.Label(money_out_frame, text="Expense Amount:")
expenditure_label.grid(row=4, column=0, sticky='w', padx=5, pady=2)
entry_expenditure = ttk.Entry(money_out_frame)
entry_expenditure.grid(row=4, column=1, padx=5, pady=2)
#Submit -Button_money_out_frame
submit_button_out = ttk.Button(money_out_frame, text="Submit Expenses", command=write_money_out_csv)
submit_button_out.grid(row=5, column=0, columnspan=2, pady=10)
submit_button_out.configure(style='TButton')
#Budget Frame widget for category
#Month-Input field
Month_Budget_Label=ttk.Label(budget_frame,text="Month")
Month_Budget_Label.grid(row=1,column=0,sticky='w',padx=5,pady=2)
month_budget_var = tk.StringVar()
month_dropdown = ttk.Combobox(budget_frame, textvariable=month_budget_var, values=month_dropdown_options, state="readonly")
month_dropdown.grid(row=1, column=1, padx=5, pady=2)
month_dropdown.current(0)
#category -input field
category_list_dropdown=[" ","RENT/EMI","Fuel","groceries","Food","Shopping","Creditcard bill",'hydro']
category_label = ttk.Label(budget_frame, text="Category:")
category_label.grid(row=2, column=0, sticky='w', padx=5, pady=2)
category_budget_var = tk.StringVar()
category_dropdown = ttk.Combobox(budget_frame, textvariable=category_budget_var, values=category_list_dropdown, state="readonly")
category_dropdown.grid(row=2, column=1, padx=5, pady=2)
category_dropdown.current(0)

#Budget_Amount -input field
Budet_Amount_label = ttk.Label(budget_frame, text="Expense Amount:")
Budet_Amount_label.grid(row=3, column=0, sticky='w', padx=5, pady=2)
budget_entry = ttk.Entry(budget_frame)
budget_entry.grid(row=3, column=1, padx=5, pady=2)
#submit button for Budget Frame
Submit_Budget = ttk.Button(budget_frame, text="Submit Budget", command=write_category_budget_to_csv)
Submit_Budget.grid(row=4, column=0, columnspan=2, pady=10)
Submit_Budget.configure(style='TButton')

#Graph Frame Weidgets
#Date-Label--- Inputfield
date_label = ttk.Label(graph_frame, text="Date:")
date_label.grid(row=1, column=0, sticky='w', padx=5, pady=2)
entry_date = ttk.Entry(graph_frame)
entry_date.grid(row=1, column=1, padx =5, pady=2)
entry_date.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))

#month Label- input field
month_label = ttk.Label(graph_frame, text="Month:")
month_label.grid(row=3, column=0, sticky='w', padx=5, pady=2)
month_var = tk.StringVar()
month_dropdown = ttk.Combobox(graph_frame, textvariable=month_var, values=month_dropdown_options, state="readonly")
month_dropdown.grid(row=3, column=1, padx=5, pady=2)
month_dropdown.current(0)

#show graph button for
show_graph = ttk.Button(graph_frame, text="Actual vs Budget", command=lambda: generate_graph_actual_budget(month_var.get()))
show_graph.grid(row=4, column=0, columnspan=2, pady=10)
show_graph.configure(style='TButton')

show_pie_chart = ttk.Button(graph_frame, text="Spending Analysis", command=lambda: generate_pie_chart(month_var.get()))
show_pie_chart.grid(row=5, column=0, columnspan=2, pady=10)
show_pie_chart.configure(style='TButton')
# Clear button for Main frame
clear_button = ttk.Button(window, text="Clear Entry", command=clear_function, style='My.TButton')
clear_button.grid(row=4, column=0, columnspan=2, pady=10)
clear_button.configure(style='TButton')

#Exit button to exit yhr application

exit_button = ttk.Button(window, text="Exit", command=exit_application)
exit_button.grid(row=6, column=0, columnspan=2, pady=10)
exit_button.configure(style='TButton')
window.mainloop()
