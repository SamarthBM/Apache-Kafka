from kafka import KafkaProducer

TOPIC_NAME = 'kafkaInPython'
KAFKA_SERVER = ['localhost:9092']

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Hello myself samarth, today has been a great day')
producer.flush()