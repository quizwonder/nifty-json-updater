import yfinance as yf

# Nifty 50 company list
nifty_50_symbols = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "SBIN.NS", "BHARTIARTL.NS", "ITC.NS", "KOTAKBANK.NS"
]

# Fetch live data
data = yf.download(nifty_50_symbols, period="1d", interval="1m", group_by='ticker')

# Generate HTML
html = """
<html>
<head>
<title>Nifty 50 Live Prices</title>
<style>
body { font-family: Arial; background: #f8f9fa; }
table { border-collapse: collapse; width: 70%; margin: 30px auto; background: white; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
th, td { padding: 10px 15px; text-align: left; border-bottom: 1px solid #ddd; }
th { background-color: #04AA6D; color: white; }
</style>
</head>
<body>
<h2 style='text-align:center;'>Nifty 50 Live Prices</h2>
<table>
<tr><th>Company</th><th>Current Price (₹)</th></tr>
"""

for symbol in nifty_50_symbols:
    try:
        price = data[symbol]['Close'].iloc[-1]
        html += f"<tr><td>{symbol}</td><td>{price:.2f}</td></tr>"
    except:
        html += f"<tr><td>{symbol}</td><td>--</td></tr>"

html += """
</table>
</body>
</html>
"""

# Save HTML file
with open("nifty50.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML file 'nifty50.html' created successfully!")