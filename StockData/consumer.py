from kafka import KafkaConsumer
from pydoop import hdfs
import os
import json

TOPIC_NAME = os.getenv('TOPIC_NAME')

consumer = KafkaConsumer(TOPIC_NAME,auto_offset_reset = 'earliest',group_id = None,
                     value_deserializer=lambda x: json.loads(x.decode('utf-8')))
hdfs_path = 'hdfs://localhost:9000//LiveStockData/data1.txt'

for message in consumer:
    values = message.value
    with hdfs.open(hdfs_path, 'at') as f:
        f.write(f"{values}\n")
