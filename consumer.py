from kafka import KafkaConsumer
from json import loads
from s3fs import S3FileSystem
import json

consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['localhost:9092'],  # change IP here if needed
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open(
        "s3://kafka-stockflow-project/stock_market_{}.json".format(count),
        'w'
    ) as file:
        json.dump(i.value, file)