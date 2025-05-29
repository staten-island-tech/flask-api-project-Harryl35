from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch Digimon data from the API
    response = requests.get('https://digimon-api.vercel.app/api/digimon')
    digimons = response.json()
    return render_template('index.html', digimons=digimons)

@app.route('/digimon/<name>')
def digimon(name):
    # Fetch detailed data for a specific Digimon
    response = requests.get(f'https://digimon-api.vercel.app/api/digimon/{name}')
    digimon = response.json()
    return render_template('digimon.html', digimon=digimon)

if __name__ == '__main__':
    app.run(debug=True)
