from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form input
        parameter = request.form['parameter']

        # Assuming you have a function that reads data and creates charts
        chart = create_chart(parameter)

        # Convert chart image to base64 to embed in HTML
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        # Render the HTML template with chart
        return render_template('index.html', plot_url=plot_url)

    # Render default form
    return render_template('index.html')

def create_chart(parameter):
    # Example function to read data and create a chart (replace with your logic)
    # Example code to read data (replace with your data reading logic)
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11]
    })

    # Example chart creation using matplotlib (replace with your charting logic)
    plt.figure(figsize=(8, 6))
    plt.plot(data['x'], data['y'], marker='o')
    plt.title('Example Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)

    return plt

if __name__ == '__main__':
    app.run(debug=True)
