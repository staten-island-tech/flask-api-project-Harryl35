from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Fetch all Digimons
def fetch_all_digimons():
    try:
        response = requests.get('https://digimon-api.vercel.app/api/digimon')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Digimons: {e}")
        return []

# Fetch Digimon by name
def fetch_digimon_by_name(name):
    try:
        response = requests.get(f'https://digimon-api.vercel.app/api/digimon/name/{name}')
        response.raise_for_status()
        data = response.json()
        return data[0] if data else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {name}: {e}")
        return None

@app.route('/')
def index():
    digimons = fetch_all_digimons()
    return render_template('index.html', digimons=digimons)

@app.route('/digimon/<name>')
def digimon(name):
    digimon_data = fetch_digimon_by_name(name)
    if digimon_data:
        return render_template('digimon.html', digimon=digimon_data)
    else:
        return f"Digimon '{name}' not found.", 404

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        digimon_data = fetch_digimon_by_name(name)
        if digimon_data:
            return render_template('digimon.html', digimon=digimon_data)
        else:
            return f"Digimon '{name}' not found.", 404
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
