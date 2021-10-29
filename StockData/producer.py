import csv
import requests
import os
from kafka import KafkaProducer
from json import dumps

from dotenv import load_dotenv
load_dotenv('.env')

TOPIC_NAME = os.getenv('TOPIC_NAME')
producer = KafkaProducer(value_serializer=lambda K:dumps(K).encode('utf-8'))

key = os.getenv('API_KEY','BOOTSTRAP_SERVER')

CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey= key'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        producer.send(TOPIC_NAME,row)
