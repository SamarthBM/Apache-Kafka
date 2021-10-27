Steps to store real time stock data to hdfs using kafka and python:

Kafka version -- 2.8.0
Hadoop version -- 3.3.1

Step 1: Create a topic to store live data.

	bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic StockData


Step 2: Start all hadoop daemons and create a path in your hdfs to store the data:

	hadoop fs -toucz  /LiveStockData/data.txt


Step 3: Now create a producer.py to write producer code.


Step 4: Now create consumer.py file to write consumer code.


Step 5: In terminal command open directory where your producer.py and consumer.py file is present and execute your consumer.py file:

	Python3 consumer.py


Step 6: Now execute your producer.py code.


Step 7: Open localhost:9870 to check the data.


