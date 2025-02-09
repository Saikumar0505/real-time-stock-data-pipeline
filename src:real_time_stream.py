from kafka import KafkaProducer
import json
import time

def stream_data(file_path, broker, topic):
    producer = KafkaProducer(
        bootstrap_servers=broker,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
    with open(file_path, "r") as f:
        data = json.load(f)
    
    for timestamp, record in data["Time Series (1min)"].items():
        producer.send(topic, value={timestamp: record})
        print(f"Sent data for {timestamp}")
        time.sleep(1)

if __name__ == "__main__":
    stream_data("data/output/stock_data.json", "localhost:9092", "stock_data")
