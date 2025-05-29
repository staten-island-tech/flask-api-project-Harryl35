from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search', '').lower()
    url = 'https://digimon-api.vercel.app/api/digimon'
    response = requests.get(url)
    digimons = response.json()

    if search_query:
        digimons = [digimon for digimon in digimons if search_query in digimon['name'].lower()]

    return render_template('search.html', digimons=digimons)

@app.route('/digimon/<name>')
def digimon(name):
    response = requests.get(f'https://digimon-api.vercel.app/api/digimon/{name}')
    digimon = response.json()
    return render_template('digimon.html', digimon=digimon)

if __name__ == '__main__':
    app.run(debug=True)
