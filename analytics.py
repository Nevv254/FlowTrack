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

# Function to generate and display a pie chart of spending by category
# Takes a dictionary of category totals and displays a pie chart
def generate_pie_chart(spending_summary):
    # Extract categories and amounts from the summary
    categories = list(spending_summary.keys())
    amounts = list(spending_summary.values())
    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    # Add title
    plt.title('Spending by Category')
    # Ensure the pie is drawn as a circle
    plt.axis('equal')
    # Display the chart
    plt.show()