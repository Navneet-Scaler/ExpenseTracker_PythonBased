import tkinter as tk
from tkinter import messagebox
import datetime
import json

DATA_FILE = 'data/expenses.json'

class BudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")
        
        self.label = tk.Label(root, text="Personal Budget Tracker")
        self.label.pack()

        self.amount_label = tk.Label(root, text="Amount")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.category_label = tk.Label(root, text="Category")
        self.category_label.pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.description_label = tk.Label(root, text="Description")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.pack()

        self.report_button = tk.Button(root, text="Generate Report", command=self.generate_report)
        self.report_button.pack()

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()

        if not amount or not category or not date or not description:
            messagebox.showerror("Input Error", "All fields are required.")
            return
        
        expense = {"amount": float(amount), "category": category, "date": date, "description": description}

        with open(DATA_FILE, 'r+') as file:
            data = json.load(file)
            data.append(expense)
            file.seek(0)
            json.dump(data, file, indent=4)
        
        messagebox.showinfo("Success", "Expense added successfully.")

    def view_expenses(self):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        
        view_window = tk.Toplevel(self.root)
        view_window.title("View Expenses")
        
        for expense in data:
            expense_text = f"Amount: ${expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Description: {expense['description']}"
            tk.Label(view_window, text=expense_text).pack()

    def generate_report(self):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        
        expenses_by_month = {}
        for expense in data:
            month = datetime.strptime(expense['date'], '%Y-%m-%d').strftime('%B %Y')
            if month not in expenses_by_month:
                expenses_by_month[month] = 0
            expenses_by_month[month] += expense['amount']
        
        report_window = tk.Toplevel(self.root)
        report_window.title("Monthly Report")
        
        for month, total in expenses_by_month.items():
            tk.Label(report_window, text=f"{month}: ${total:.2f}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()
