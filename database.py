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