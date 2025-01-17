from flask import Flask, jsonify, render_template, send_file
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Initialize Flask app
app = Flask(__name__, template_folder=r"C:\\Users\\Ev\\Desktop\\Earthquake_Analysis\\templates")

# Define the path to the CSV file
csv_path = r"C:\\Users\\Ev\\Desktop\\Earthquake_Analysis\\earthquakes.csv"

# Verify that the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"The file at {csv_path} does not exist.")

# Load the data into a Pandas DataFrame
data = pd.read_csv(csv_path)

columns_to_remove = [
    "latitude", "place", "longitude", "magType", "nst", "gap", "dmin", "rms", 
    "net", "id", "updated", "type", "horizontalError", "depthError", 
    "magError", "magNst", "status", "locationSource", "magSource", "Alert"
]
data = data.drop(columns=columns_to_remove, errors='ignore')

# Keep the original time column intact and format it to show only the year
if 'time' in data.columns:
    data['time'] = pd.to_datetime(data['time'], errors='coerce').dt.year

@app.route('/')
def show_head():
    table_html = data.head(10).to_html(index=False)
    return render_template('index.html', table=table_html)

# Create a Flask route to serve the data
@app.route('/api/earthquakes', methods=['GET'])
def get_earthquakes():
    # Convert DataFrame to a dictionary (list of records)
    earthquakes = data.to_dict(orient='records')
    return jsonify(earthquakes)
    
@app.route('/boxplot', methods=['GET'])
def plot_boxplot():
    # Ensure that both 'time' and 'mag' columns are present
    if 'time' in data.columns and 'mag' in data.columns:
        # Create the box plot
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='time', y='mag', data=data, palette='coolwarm')
        plt.title('Distribution of Earthquake Magnitudes by Year')
        plt.xlabel('Time')
        plt.ylabel('Magnitude')
        plt.xticks(rotation=45)
        plt.grid(True)

        # Save the plot to a BytesIO object
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        # Return the plot as a response
        return send_file(img, mimetype='image/png')
    else:
        return "Columns 'time' or 'mag' are missing from the data.", 400
    
@app.route('/stats', methods=['GET'])
def get_statistics():
    if 'time' in data.columns and 'mag' in data.columns:
        stats = data.groupby('time')['mag'].agg(['count', 'mean', 'median', 'std', 'min', 'max']).reset_index()
        return stats.to_html(index=False)
    else:
        return "Columns 'time' or 'mag' are missing from the data.", 400
    
@app.route('/interactive-scatter', methods=['GET'])
def interactive_scatter():
    import plotly.express as px
    if 'time' in data.columns and 'mag' in data.columns:
        fig = px.scatter(data, x='mag', y='time', title='Interactive Scatter Plot of Earthquakes',
                         labels={'mag': 'Magnitude', 'time': 'Time'}, color='mag', 
                         hover_data=['time'])
        fig.update_layout(xaxis_title='Magnitude', yaxis_title='Time')
        
        # Save plot to HTML
        html_path = 'templates/interactive_scatter.html'
        fig.write_html(html_path)
        return render_template('interactive_scatter.html')
    else:
        return "Columns 'year' or 'mag' are missing from the data.", 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
