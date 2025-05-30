from flask import Flask, render_template, request
import requests

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)