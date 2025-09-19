# Expense class to represent individual expense records
class Expense:
    # Initialize an Expense object with amount, category, and date
    def __init__(self, amount, category, date):
        # Store the expense amount as a float
        self.amount = amount
        # Store the expense category as a string
        self.category = category
        # Store the expense date as a string
        self.date = date

    # Validate the expense amount
    # Ensures amount is a positive number
    def validate_amount(self):
        # Check if amount is a number and greater than zero
        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            raise ValueError("Amount must be a positive number")

    # Validate the expense category
    # Ensures category is a non-empty string
    def validate_category(self):
        # Check if category is a string and not empty
        if not isinstance(self.category, str) or not self.category.strip():
            raise ValueError("Category must be a non-empty string")

    # Validate the expense date
    # Ensures date is in YYYY-MM-DD format
    def validate_date(self):
        # Check if date matches the expected format
        from datetime import datetime
        try:
            datetime.strptime(self.date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    # String representation of the Expense object
    # Returns a formatted string showing expense details
    def __str__(self):
        # Format the expense information for display
        return f"Expense: ${self.amount:.2f} on {self.date} in category '{self.category}'"