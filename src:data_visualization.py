import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Load Data from SQLite
DATABASE_URL = "sqlite:///data/stocks_data.db"
engine = create_engine(DATABASE_URL)
df = pd.read_sql("SELECT * FROM stocks", con=engine)

# Convert timestamp to datetime for better visualization
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp')

# Set Seaborn Style
sns.set(style="whitegrid")

# Plot 1: Stock Price Trend Over Time
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['close'], label='Closing Price', color='b')
plt.xlabel("Timestamp")
plt.ylabel("Stock Price ($)")
plt.title("Stock Price Trend Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# Plot 2: Stock Volume Distribution
plt.figure(figsize=(10, 5))
sns.barplot(x=df['timestamp'][:10], y=df['volume'][:10], palette="viridis")
plt.xlabel("Timestamp")
plt.ylabel("Trading Volume")
plt.title("Stock Trading Volume Distribution (Top 10)")
plt.xticks(rotation=45)
plt.show()

# Plot 3: Moving Average of Closing Price
df["Moving_Avg"] = df["close"].rolling(window=5).mean()

plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["close"], label="Closing Price", color="blue")
plt.plot(df["timestamp"], df["Moving_Avg"], label="5-period Moving Avg", color="red")
plt.xlabel("Timestamp")
plt.ylabel("Stock Price ($)")
plt.title("Stock Price with Moving Average")
plt.legend()
plt.grid()
plt.show()

# Plot 4: Top Stocks by Volume (Pie Chart)
top_stocks = df.nlargest(5, 'volume')

plt.figure(figsize=(8, 8))
plt.pie(top_stocks["volume"], labels=top_stocks["timestamp"], autopct="%1.1f%%", colors=sns.color_palette("coolwarm"))
plt.title("Top 5 Stocks by Volume")
plt.show()
