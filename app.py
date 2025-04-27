from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_iocs():
    response = requests.get("https://otx.alienvault.com/api/v1/indicators/malware")
    if response.status_code == 200:
        return response.json()
    else:
        return []

@app.route('/')
def index():
    iocs = fetch_iocs()
    return render_template('index.html', iocs=iocs)

if __name__ == "__main__":
    app.run(debug=True)
