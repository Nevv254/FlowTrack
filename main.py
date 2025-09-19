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