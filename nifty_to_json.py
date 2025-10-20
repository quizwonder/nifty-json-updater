from flask import Flask, jsonify
import yfinance as yf
import threading
import time
import json

app = Flask(__name__)

data = {}

def fetch_nifty_data():
    global data
    while True:
        ticker = yf.Ticker("^NSEI")  # Nifty 50 Index
        info = ticker.info
        data = {
            "symbol": "NIFTY 50",
            "price": info.get("regularMarketPrice"),
            "change": info.get("regularMarketChange"),
            "percent_change": info.get("regularMarketChangePercent")
        }
        with open("nifty.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Updated:", data)
        time.sleep(10)

@app.route("/nifty.json")
def get_json():
    return jsonify(data)

if __name__ == "__main__":
    threading.Thread(target=fetch_nifty_data, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)