# ApacheSpark-w-Python

This project aims to consume the Iot weather data message from a python script through kafka broker and transform the data through ApacheSpark in a live streaming setup.

Flow:
Python Script --> Kafka --> ApacheSpark




## Deployment

To deploy this project run the following in order:

Make sure to 

1. zookeeper
```bash
  zookeeper-server-start.bat config\zookeeper.properties 
```

2. Kafka 
```bash
  kafka-server-start.bat config/server.properties 

```

3. Iot Data Python Script
```bash
  Python Iot_Data.py
```

4. Spark Script

```bash
  spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark_kafka.py localhost 9092     

```
## Authors

- [@AminSiddique](https://github.com/Amin-Siddique)

## 🚀 About Me
# Hi, I'm Amin! 👋

I am a passionate Data Engineer 

