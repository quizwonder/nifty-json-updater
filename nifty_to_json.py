from flask import Flask, jsonify
import requests
import threading
import time
import json

app = Flask(__name__)

data = {}

def fetch_nifty_data():
    global data
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"
    while True:
        try:
            response = requests.get(url)
            result = response.json()
            price = result["chart"]["result"][0]["meta"]["regularMarketPrice"]
            data = {
                "symbol": "NIFTY 50",
                "price": price
            }
            with open("nifty.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Updated:", data)
        except Exception as e:
            print("Error:", e)
        time.sleep(30)  # safer interval (30 seconds)
        

@app.route("/nifty.json")
def get_json():
    return jsonify(data)


@app.route("/")
def home():
    return "<h3>Nifty JSON API Running ✅</h3><p>Visit /nifty.json for data.</p>"


if __name__ == "__main__":
    threading.Thread(target=fetch_nifty_data, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)