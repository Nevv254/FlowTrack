import sqlite3

# Database connection setup
# This function establishes a connection to the SQLite database
def get_connection():
    # Connect to the SQLite database file 'expenses.db'
    # If the file doesn't exist, it will be created
    return sqlite3.connect('expenses.db')

# Create expenses table schema
# This function creates the expenses table if it doesn't exist
def create_expenses_table():
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to create expenses table with id (primary key), amount (real), category (text), date (text)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Create budgets table schema
# This function creates the budgets table if it doesn't exist
def create_budgets_table():
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to create budgets table with id (primary key), amount (real), month (text), year (integer)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            month TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Insert expense into database
# This function inserts a new expense record into the expenses table
def insert_expense(amount, category, date):
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to insert expense data
    cursor.execute('INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)', (amount, category, date))
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Insert budget into database
# This function inserts a new budget record into the budgets table
def insert_budget(amount, month, year):
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to insert budget data
    cursor.execute('INSERT INTO budgets (amount, month, year) VALUES (?, ?, ?)', (amount, month, year))
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Retrieve all expenses from database
# This function fetches all expense records from the expenses table
def get_all_expenses():
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to select all expenses
    cursor.execute('SELECT id, amount, category, date FROM expenses')
    # Fetch all results
    expenses = cursor.fetchall()
    # Close the connection
    conn.close()
    # Return the list of expenses
    return expenses

# Retrieve all budgets from database
# This function fetches all budget records from the budgets table
def get_all_budgets():
    # Get database connection
    conn = get_connection()
    # Create cursor object
    cursor = conn.cursor()
    # SQL command to select all budgets
    cursor.execute('SELECT id, amount, month, year FROM budgets')
    # Fetch all results
    budgets = cursor.fetchall()
    # Close the connection
    conn.close()
    # Return the list of budgets
    return budgets