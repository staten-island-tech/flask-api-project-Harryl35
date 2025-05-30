from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

DIGIMON_API_URL = "https://digimon-api.vercel.app/api/digimon"

@app.route('/')
def home():
    response = requests.get(DIGIMON_API_URL)
    digimon_list = response.json()
    return render_template("search.html", digimon_list=digimon_list)

@app.route('/search_digimon')
def search_digimon():
    level_query = request.args.get('level', '').capitalize()

    if level_query:  # If a level is entered, filter by level
        response = requests.get(f"{DIGIMON_API_URL}/level/{level_query}")
        digimon_data = response.json()
        return jsonify(digimon_data if digimon_data else {"error": "No Digimon found for this level"})
    
    # If no level is entered, return all Digimon
    response = requests.get(DIGIMON_API_URL)
    digimon_data = response.json()
    return jsonify(digimon_data)

if __name__ == '__main__':
    app.run(debug=True)
