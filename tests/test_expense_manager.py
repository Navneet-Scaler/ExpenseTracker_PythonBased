import unittest
import json
import os
from expense_manager import add_expense, view_expenses

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.test_file = 'data/test_expenses.json'
        with open(self.test_file, 'w') as file:
            json.dump([], file)
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_expense(self):
        expense = {'amount': 50, 'category': 'Food', 'date': '2024-08-01', 'description': 'Lunch'}
        add_expense(expense)
        with open(self.test_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], expense)
    
    def test_view_expenses(self):
        expense = {'amount': 50, 'category': 'Food', 'date': '2024-08-01', 'description': 'Lunch'}
        add_expense(expense)
        expenses = view_expenses()
        self.assertIn(expense, expenses)

if __name__ == "__main__":
    unittest.main()
