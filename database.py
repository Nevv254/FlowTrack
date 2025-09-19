import sqlite3

# Database connection setup
# This function establishes a connection to the SQLite database
def get_connection():
    # Connect to the SQLite database file 'expenses.db'
    # If the file doesn't exist, it will be created
    return sqlite3.connect('expenses.db')