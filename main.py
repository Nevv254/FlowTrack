# Import the database module for database operations
import database

# Import the expense module for Expense class
import expense

# Import the analytics module for charts and summaries
import analytics

# Function to display the main menu
# Shows options for the user to choose from
def display_menu():
    # Print the menu header
    print("\n=== FlowTrack Expense Tracker ===")
    # Print menu options
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. Set Monthly Budget")
    print("5. View Spending Chart")
    print("6. Exit")
    # Prompt for choice
    choice = input("Choose an option (1-6): ")
    # Return the user's choice
    return choice

# Function to add a new expense
# Prompts user for expense details and validates input
def add_expense():
    # Prompt for amount
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a positive number.")
    
    # Prompt for category
    category = input("Enter expense category (e.g., food, transport): ").strip()
    if not category:
        category = "misc"
    
    # Prompt for date
    while True:
        date = input("Enter expense date (YYYY-MM-DD): ").strip()
        try:
            from datetime import datetime
            datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Create Expense object
    exp = expense.Expense(amount, category, date)
    
    # Insert into database
    database.insert_expense(amount, category, date)
    
    # Confirm addition
    print(f"Expense added: {exp}")

# Function to view all expenses in a formatted list
# Retrieves and displays all expenses from the database
def view_all_expenses():
    # Retrieve all expenses from database
    expenses = database.get_all_expenses()
    
    # Check if there are any expenses
    if not expenses:
        print("No expenses found.")
        return
    
    # Print header
    print("\nAll Expenses:")
    print("-" * 50)
    print(f"{'ID':<5} {'Amount':<10} {'Category':<15} {'Date':<12}")
    print("-" * 50)
    
    # Print each expense
    for exp in expenses:
        exp_id, amount, category, date = exp
        print(f"{exp_id:<5} ${amount:<9.2f} {category:<15} {date:<12}")
    
    # Print total
    total = sum(exp[1] for exp in expenses)
    print("-" * 50)
    print(f"Total: ${total:.2f}")

# Function to view expenses filtered by category
# Prompts user for category and displays matching expenses
def view_expenses_by_category():
    # Prompt for category
    category = input("Enter category to filter by: ").strip()
    
    # Retrieve all expenses
    expenses = database.get_all_expenses()
    
    # Filter expenses by category
    filtered_expenses = [exp for exp in expenses if exp[2].lower() == category.lower()]
    
    # Check if there are any matching expenses
    if not filtered_expenses:
        print(f"No expenses found for category '{category}'.")
        return
    
    # Print header
    print(f"\nExpenses in category '{category}':")
    print("-" * 50)
    print(f"{'ID':<5} {'Amount':<10} {'Date':<12}")
    print("-" * 50)
    
    # Print each filtered expense
    for exp in filtered_expenses:
        exp_id, amount, _, date = exp
        print(f"{exp_id:<5} ${amount:<9.2f} {date:<12}")
    
    # Print total for category
    total = sum(exp[1] for exp in filtered_expenses)
    print("-" * 50)
    print(f"Total for '{category}': ${total:.2f}")