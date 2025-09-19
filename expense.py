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