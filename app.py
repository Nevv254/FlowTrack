from flask import Flask, render_template, request, redirect, url_for, flash
import database
import expense
import analytics

app = Flask(__name__)
app.secret_key = 'flowtrack_secret_key_2023'

# Initialize database tables
database.create_expenses_table()
database.create_budgets_table()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)