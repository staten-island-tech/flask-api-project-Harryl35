from flask import Flask, render_template
import requests

app = Flask(__name__)

import requests

url = 'https://digimon-api.vercel.app/api/digimon'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get(url, headers=headers)

if response.status_code('name'):
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

