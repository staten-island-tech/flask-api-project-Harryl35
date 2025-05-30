from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

DIGIMON_API_URL = "https://digimon-api.vercel.app/api/digimon"

@app.route('/')
def home():
    return render_template("search.html")

@app.route('/search_digimon')
def search_digimon():
    query = request.args.get('query', '').capitalize()  # Capitalizing for consistency
    response = requests.get(f"{DIGIMON_API_URL}/name/{query}")
    digimon_data = response.json()

    return jsonify(digimon_data[0] if digimon_data else {"error": "No Digimon found"})

if __name__ == '__main__':
    app.run(debug=True)

