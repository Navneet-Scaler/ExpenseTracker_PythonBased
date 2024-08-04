import json
from datetime import datetime

DATA_FILE = 'data/expenses.json'

def generate_monthly_report():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    
    expenses_by_month = {}
    for expense in data:
        month = datetime.strptime(expense['date'], '%Y-%m-%d').strftime('%B %Y')
        if month not in expenses_by_month:
            expenses_by_month[month] = 0
        expenses_by_month[month] += expense['amount']
    
    for month, total in expenses_by_month.items():
        print(f"{month}: ${total:.2f}")
