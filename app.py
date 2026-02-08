from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# REPLACE THIS URL:
# Go to your Google Sheet -> File -> Share -> Publish to Web
# Select "Link" and "Comma-separated values (.csv)"
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/YOUR_LONG_ID_HERE/pub?output=csv"

@app.route('/')
def index():
    try:
        # We read the CSV directly from the web
        # Use storage_options to avoid potential header issues
        df = pd.read_csv(SHEET_CSV_URL)

        # We convert the rows into a list of dictionaries for the HTML
        links = df.to_dict('records')
    except Exception as e:
        print(f"Error: {e}")
        links = []

    return render_template('index.html', links=links)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
