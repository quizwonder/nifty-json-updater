from flask import Flask, jsonify
import yfinance as yf
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Nifty 50 symbols (add more if needed)
nifty_50_symbols = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS"
]

# Dictionary to store live data
nifty_data = {}

# Background thread to update prices every 10 seconds
def update_nifty():
    global nifty_data
    while True:
        for symbol in nifty_50_symbols:
            ticker = yf.Ticker(symbol)
            info = ticker.history(period="1d", interval="1m")
            if not info.empty:
                price = round(float(info['Close'].iloc[-1]), 2)
                nifty_data[symbol] = {
                    "price": price,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                nifty_data[symbol] = {"price": None, "timestamp": None}
        time.sleep(10)

# Start background thread
threading.Thread(target=update_nifty, daemon=True).start()

# Serve JSON via URL
@app.route("/nifty50.json")
def get_nifty():
    return jsonify(nifty_data)

# Start Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)