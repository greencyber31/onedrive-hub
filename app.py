from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'links.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    links = load_data()
    return render_template('index.html', links=links)

@app.route('/update-link', methods=['POST'])
def update():
    data = request.json
    file_id = data.get('file_id')

    # Store the link using file_id as the unique key
    db = load_data()
    db[file_id] = {
        "name": data.get('file_name'),
        "url": data.get('new_link')
    }
    save_data(db)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Use the PORT environment variable if it exists (for Render), otherwise default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
