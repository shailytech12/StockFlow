import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # change IP here if needed
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

df = pd.read_csv("indexProcessed.csv")

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    print("Record Sent")
    sleep(1)

producer.flush()
