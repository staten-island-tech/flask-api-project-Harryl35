from flask import Flask, render_template, request
import requests

app = Flask(__name__)
<<<<<<< HEAD

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
=======
DIGIMON_API_URL = "https://digimon-api.vercel.app/api/digimon"

@app.route('/')
def home():
    response = requests.get(DIGIMON_API_URL)
    digimon_list = response.json()
    return render_template("index.html", digimon_list=digimon_list)

@app.route('/digimon/<name>')
def digimon_info(name):
    response = requests.get(f"{DIGIMON_API_URL}/name/{name}")
    digimon_data = response.json()
    return render_template("digimon.html", digimon=digimon_data[0] if digimon_data else None)
>>>>>>> 3cb05c081cf0c865418560a0d4a7dd1b2be5687b

if __name__ == '__main__':
    app.run(debug=True)
