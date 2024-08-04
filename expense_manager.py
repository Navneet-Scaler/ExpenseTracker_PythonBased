import json
import os

DATA_FILE = 'data/expenses.json'

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

def add_expense(expense):
    with open(DATA_FILE, 'r+') as file:
        data = json.load(file)
        data.append(expense)
        file.seek(0)
        json.dump(data, file, indent=4)

def view_expenses():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        if not data:
            print("No expenses recorded.")
        else:
            for expense in data:
                print(expense)

def delete_expense(index):
    with open(DATA_FILE, 'r+') as file:
        data = json.load(file)
        if 0 <= index < len(data):
            data.pop(index)
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)
            print("Expense deleted successfully.")
        else:
            print("Invalid index.")