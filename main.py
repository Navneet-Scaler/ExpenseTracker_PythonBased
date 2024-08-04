from expense_manager import add_expense, view_expenses, delete_expense
from report_generator import generate_monthly_report

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Monthly Report")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            expense = {"amount": amount, "category": category, "date": date, "description": description}
            add_expense(expense)
            print("Expense added successfully.")
            
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            generate_monthly_report()
        
        elif choice == '4':
            expense_id = input("Enter the ID of the expense to delete: ")
            delete_expense(expense_id)

        elif choice == "5":
            break;
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()