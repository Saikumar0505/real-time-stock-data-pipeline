import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db(db_url, input_file):
    engine = create_engine(db_url)
    df = pd.read_csv(input_file)
    df.to_sql("stocks", con=engine, if_exists="replace", index=False)
    print(f"Data loaded into database: {db_url}")

if __name__ == "__main__":
    load_data_to_db("sqlite:///data/stocks_data.db", "data/output/processed_stock_data.csv")
