from flask import Flask, render_template, request, redirect, url_for, flash
import database
import expense
import analytics
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'flowtrack_secret_key_2023'

# Initialize database tables
database.create_expenses_table()
database.create_budgets_table()

@app.route('/')
def index():
    # Get dashboard data
    expenses = database.get_all_expenses()
    budgets = database.get_all_budgets()

    # Calculate totals
    total_expenses = sum(exp[1] for exp in expenses) if expenses else 0

    # Calculate monthly total (current month)
    current_month = datetime.now().strftime('%Y-%m')
    monthly_total = sum(exp[1] for exp in expenses if exp[3].startswith(current_month)) if expenses else 0

    # Get category count
    categories = set(exp[2] for exp in expenses) if expenses else set()
    category_count = len(categories)

    # Get recent expenses (last 5)
    recent_expenses = expenses[-5:] if expenses else []

    # Get budget status
    budget_status = None
    if budgets:
        latest_budget = budgets[-1]
        budget_id, budget_amount, budget_month, budget_year = latest_budget

        # Calculate spent for this budget period
        spent = 0
        for exp in expenses:
            exp_date = exp[3]
            exp_year, exp_month, _ = exp_date.split('-')
            if int(exp_year) == budget_year and exp_month.lower() == budget_month.lower():
                spent += exp[1]

        remaining = budget_amount - spent
        warning = None

        if spent > budget_amount:
            warning = "⚠️ You have exceeded your budget!"
        elif spent > budget_amount * 0.8:
            warning = "⚠️ You are close to your budget limit."

        budget_status = {
            'budget': budget_amount,
            'spent': spent,
            'remaining': remaining,
            'warning': warning
        }

    return render_template('index.html',
                         total_expenses=total_expenses,
                         monthly_total=monthly_total,
                         category_count=category_count,
                         recent_expenses=recent_expenses,
                         budget_status=budget_status)

if __name__ == '__main__':
    app.run(debug=True)