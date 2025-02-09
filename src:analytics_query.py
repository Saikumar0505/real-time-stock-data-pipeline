from sqlalchemy import create_engine

def get_top_stocks_by_volume(db_url):
    engine = create_engine(db_url)
    query = """
    SELECT timestamp, close, volume
    FROM stocks
    ORDER BY volume DESC
    LIMIT 5;
    """
    result = engine.execute(query)
    for row in result:
        print(row)

if __name__ == "__main__":
    DATABASE_URL = "sqlite:///data/stocks_data.db"
    get_top_stocks_by_volume(DATABASE_URL)
