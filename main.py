# Import necessary libraries
from flask import Flask, render_template
import plotly.express as px
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Define route for the dashboard
@app.route('/')
def dashboard():
    # Create a scatter plot using Plotly
    fig = px.scatter(df, x='Age', y='Salary', color='Name', title='Salary vs Age')

    # Convert Plotly figure to JSON
    graphJSON = fig.to_json()

    # Render the dashboard template with the Plotly figure JSON
    return render_template('dashboard.html', graphJSON=graphJSON)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
