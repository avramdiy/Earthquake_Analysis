from flask import Flask, jsonify
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Define the path to the CSV file
csv_path = r"C:\\Users\\Ev\\Desktop\\Earthquake_Analysis\\earthquakes.csv"

# Verify that the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"The file at {csv_path} does not exist.")

# Load the data into a Pandas DataFrame
data = pd.read_csv(csv_path)

# Create a Flask route to serve the data
@app.route('/api/earthquakes', methods=['GET'])
def get_earthquakes():
    # Convert DataFrame to a dictionary (list of records)
    earthquakes = data.to_dict(orient='records')
    return jsonify(earthquakes)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
