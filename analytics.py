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

# Function to generate Plotly pie chart HTML for web display
# Takes a dictionary of category totals and returns HTML for embedding
def generate_pie_chart_html(spending_summary):
    if not spending_summary:
        return "<p>No data available for chart</p>"

    # Extract categories and amounts from the summary
    categories = list(spending_summary.keys())
    amounts = list(spending_summary.values())

    # Create HTML for a simple CSS-based pie chart
    total = sum(amounts)
    chart_html = '<div class="pie-chart-container">'
    chart_html += '<div class="pie-chart">'

    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', '#FF6384', '#C9CBCF']
    current_angle = 0

    for i, (category, amount) in enumerate(zip(categories, amounts)):
        percentage = (amount / total) * 100
        angle = (amount / total) * 360
        color = colors[i % len(colors)]

        if percentage > 0:
            chart_html += f'<div class="pie-slice" style="--angle: {angle}deg; --color: {color}; --start-angle: {current_angle}deg;"></div>'
            current_angle += angle

    chart_html += '</div>'
    chart_html += '<div class="pie-legend">'

    for i, (category, amount) in enumerate(zip(categories, amounts)):
        percentage = (amount / total) * 100
        color = colors[i % len(colors)]
        chart_html += f'<div class="legend-item">'
        chart_html += f'<span class="legend-color" style="background-color: {color};"></span>'
        chart_html += f'<span class="legend-text">{category}: ${amount:.2f} ({percentage:.1f}%)</span>'
        chart_html += f'</div>'

    chart_html += '</div></div>'

    # Add CSS styles
    css = '''
    <style>
    .pie-chart-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }
    .pie-chart {
        position: relative;
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: conic-gradient(from 0deg, #f3f4f6 0deg);
    }
    .pie-slice {
        position: absolute;
        width: 100%;
        height: 100%;
        clip-path: polygon(50% 50%, 50% 0%, var(--end-x, 100%) 0%, var(--end-x, 100%) var(--end-y, 0%), 50% 50%);
        background: var(--color);
        transform: rotate(var(--start-angle, 0deg));
    }
    .pie-legend {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .legend-color {
        width: 16px;
        height: 16px;
        border-radius: 2px;
    }
    .legend-text {
        font-size: 14px;
        color: #374151;
    }
    </style>
    '''

    return css + chart_html