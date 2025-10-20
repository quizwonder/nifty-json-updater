def fetch_nifty_data():
    global data
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"
    while True:
        try:
            response = requests.get(url, timeout=10)
            result = response.json()
            # Check if the response is valid
            chart = result.get("chart", {})
            if chart.get("result"):
                price = chart["result"][0]["meta"]["regularMarketPrice"]
                data = {
                    "symbol": "NIFTY 50",
                    "price": price
                }
                # Save JSON locally (optional)
                with open("nifty.json", "w") as f:
                    json.dump(data, f, indent=4)
                print("Updated:", data)
            else:
                print("No data yet, waiting...")
        except Exception as e:
            print("Error fetching data:", e)
        time.sleep(30)  # fetch every 30 seconds