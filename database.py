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