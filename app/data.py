from flask import Flask, jsonify, render_template, send_file
import pandas as pd
import os
import matplotlib.pyplot as plt
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

# New route to plot time vs magnitude
@app.route('/plot', methods=['GET'])
def plot_time_magnitude():
    # Ensure that both 'time' and 'magnitude' columns are present
    if 'time' in data.columns and 'mag' in data.columns:
        # Create a plot
        plt.figure(figsize=(10, 6))
        plt.plot(data['time'], data['mag'], marker='o', linestyle='-', color='b')
        plt.title('Earthquake Magnitude Over Time')
        plt.xlabel('Year')
        plt.ylabel('Magnitude')
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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
