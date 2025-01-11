# Week 6 Github Analysis : Earthquakes

## 1st Commit

- Extracted dataset from https://www.kaggle.com/datasets/bakiturhan/earthquake-dataset

- Initialized app, templates, README.md, requirements.txt, data.py, index.html

- Created initial code in data.py to load the csv into a html format prior to cleaning.

## 2nd Commit

- Added the @app.route('/') to visualize head(10) to understand what data to clean

- Filtered to remove "latitude", "longitude",  "magType", "nst", "gap", "dmin", "rms", "net", "id", "updated", "type", "horizontalError", "depthError", "magError", "magNst", "status", "locationSource", "magSource", "Alert", "place"

- This leaves the "time", "depth", "mag", "place" attributes

- Formatted the "time" attribute to show only the year

- Created ap.route('/plot') to show the relationship between the time of yearly occurences and varying magnitudes.

- Line chart is messy and aggregated data is not visually clean. Fix in 3rd commit.

## 3rd Commit

## 4th Commit

## 5th Commit