from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# REPLACE THIS URL:
# Go to your Google Sheet -> File -> Share -> Publish to Web
# Select "Link" and "Comma-separated values (.csv)"
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ0yR4gNYKqNsZYVhtncB5lYaM4QEB3TL5QlaTlydbniXL5xnHDW2aMp_syjb9IEIoe8yqU5YCtCCpy/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    try:
        df = pd.read_csv(SHEET_CSV_URL)

        # Now we check both file_name and folder_path for duplicates
        df_clean = df.drop_duplicates(subset=['file_name', 'folder_path'], keep='last')

        links = df_clean.to_dict('records')
    except Exception as e:
        print(f"Error: {e}")
        links = []
    return render_template('index.html', links=links)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
