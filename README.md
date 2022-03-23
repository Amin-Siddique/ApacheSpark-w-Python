# ApacheSpark-w-Python

This project aims to consume tweets message from a python script through kafka broker and transform the data to get maximum tagged word through ApacheSpark Streaming.

Flow:
Python Script --> Kafka --> ApacheSpark




## Deployment

To deploy this project run the following in order:


1. zookeeper
```bash
  zookeeper-server-start.bat config\zookeeper.properties 
```

2. Kafka 
```bash
  kafka-server-start.bat config/server.properties 

```

3. Data Streaming from Twitter Python Script
```bash
  Python Twitter_to_Kafka.py
```

4. Spark Script

```bash
  spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.7 Spark_kafka_twitter_tags.py

```
## Authors

- [@AminSiddique](https://github.com/Amin-Siddique)

## 🚀 About Me
# Hi, I'm Amin! 👋

I am a passionate Data Engineer 

