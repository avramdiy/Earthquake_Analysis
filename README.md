# Week 6 Github Analysis : Earthquakes

## 1st Commit | 1/9/25

- Extracted dataset from https://www.kaggle.com/datasets/bakiturhan/earthquake-dataset

- Initialized app, templates, README.md, requirements.txt, data.py, index.html

- Created initial code in data.py to load the csv into a html format prior to cleaning.

## 2nd Commit | 1/10/25

- Added the @app.route('/') to visualize head(10) to understand what data to clean

- Filtered to remove "latitude", "longitude",  "magType", "nst", "gap", "dmin", "rms", "net", "id", "updated", "type", "horizontalError", "depthError", "magError", "magNst", "status", "locationSource", "magSource", "Alert", "place"

- This leaves the "time", "depth", "mag", "place" attributes

- Formatted the "time" attribute to show only the year

- Created ap.route('/plot') to show the relationship between the time of yearly occurences and varying magnitudes.

- Line chart is messy and aggregated data is not visually clean. Fix in 3rd commit.

## 3rd Commit | 1/11/25

- Adjusted the line plot code to be a scatterplot instead.

- Removed /heatmap & /plot code. Used a /boxplot to demonstrate outliers and visualize the aggregated magnitude per year.

- Added /stats to retrieve the mean, median, and standard deviation of magnitudes, count of earthquakes per year, and the minimum & maximum magnitudes.

## 4th Commit | 1/12/25

- Created /interactive-scatter route & interactive-scatter.html for users to specifically focus on certain sections of the magnitudes and timeframes.

- Customized ('/') route to show a dashboard with individual buttons to load the webpages for /stats /boxplot /interactive-scatter routes

## 5th Commit | 1/13/25