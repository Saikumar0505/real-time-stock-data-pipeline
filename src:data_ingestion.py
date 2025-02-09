import requests
import yaml
import time

def fetch_stock_data(symbol, api_key, output_file):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        with open(output_file, "w") as f:
            f.write(str(data))
        print(f"Data for {symbol} fetched and saved.")
    else:
        print("Failed to fetch data:", response.status_code, response.text)

if __name__ == "__main__":
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    API_KEY = config["api"]["api_key"]
    fetch_stock_data("AAPL", API_KEY, "data/output/stock_data.json")
