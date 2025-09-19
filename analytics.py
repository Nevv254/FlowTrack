# Import matplotlib for plotting charts
import matplotlib.pyplot as plt

# Import pandas for data manipulation and analysis
import pandas as pd

# Function to calculate spending summaries by category
# Takes a list of expense tuples and returns a dictionary of category totals
def calculate_spending_by_category(expenses):
    # Create a DataFrame from the expenses list
    df = pd.DataFrame(expenses, columns=['id', 'amount', 'category', 'date'])
    # Group by category and sum the amounts
    summary = df.groupby('category')['amount'].sum().to_dict()
    # Return the summary dictionary
    return summary