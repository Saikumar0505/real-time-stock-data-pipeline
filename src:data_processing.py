import pandas as pd
import json

def process_stock_data(input_file, output_file):
    with open(input_file, "r") as f:
        raw_data = json.load(f)

    time_series = raw_data["Time Series (1min)"]
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })
    df.index.name = "timestamp"
    df.reset_index(inplace=True)
    df.to_csv(output_file, index=False)
    print(f"Data processed and saved to {output_file}")

if __name__ == "__main__":
    process_stock_data("data/output/stock_data.json", "data/output/processed_stock_data.csv")
