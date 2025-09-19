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

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            category = request.form['category'].strip()
            date = request.form['date'].strip()

            # Validate inputs
            if amount <= 0:
                flash('Amount must be a positive number', 'error')
                return redirect(url_for('add_expense'))

            if not category:
                category = 'misc'

            # Validate date format
            from datetime import datetime
            datetime.strptime(date, '%Y-%m-%d')

            # Create expense object and validate
            exp = expense.Expense(amount, category, date)

            # Insert into database
            database.insert_expense(amount, category, date)

            flash(f'Expense added successfully: {exp}', 'success')
            return redirect(url_for('index'))

        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'error')
            return redirect(url_for('add_expense'))
        except Exception as e:
            flash(f'Error adding expense: {str(e)}', 'error')
            return redirect(url_for('add_expense'))

    return render_template('add_expense.html')

@app.route('/view_expenses')
def view_expenses():
    expenses = database.get_all_expenses()

    # Calculate total
    total = sum(exp[1] for exp in expenses) if expenses else 0

    return render_template('view_expenses.html', expenses=expenses, total=total)

@app.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            month = request.form['month'].strip()
            year = int(request.form['year'])

            if amount <= 0:
                flash('Budget amount must be positive', 'error')
                return redirect(url_for('budget'))

            if not month:
                flash('Month is required', 'error')
                return redirect(url_for('budget'))

            database.insert_budget(amount, month, year)
            flash(f'Budget set: ${amount:.2f} for {month} {year}', 'success')
            return redirect(url_for('budget'))

        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'error')
            return redirect(url_for('budget'))

    # Get current budget status
    budgets = database.get_all_budgets()
    budget_status = None

    if budgets:
        latest_budget = budgets[-1]
        budget_id, budget_amount, budget_month, budget_year = latest_budget

        # Calculate spent for this budget period
        expenses = database.get_all_expenses()
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
            'warning': warning,
            'month': budget_month,
            'year': budget_year
        }

    return render_template('budget.html', budget_status=budget_status)

@app.route('/charts')
def charts():
    # Get all expenses
    expenses = database.get_all_expenses()

    # Calculate spending by category
    spending_summary = analytics.calculate_spending_by_category(expenses)

    # Generate chart HTML
    chart_html = analytics.generate_pie_chart_html(spending_summary)

    return render_template('charts.html', chart_html=chart_html, spending_summary=spending_summary)

if __name__ == '__main__':
    app.run(debug=True)