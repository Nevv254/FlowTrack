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