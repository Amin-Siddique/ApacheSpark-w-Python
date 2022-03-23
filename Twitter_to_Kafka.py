import tweepy


from kafka import KafkaProducer # pip install kafka-python
import numpy as np              # pip install numpy
from sys import argv, exit
from time import  time,sleep
import datetime
import json

dateformat='%Y-%m-%d %I:%M:%S'
now_time = datetime.datetime.now()
time_format = datetime.datetime.strftime(now_time,dateformat)

#Provide the Keys
consumer_key=" "
consumer_secret=" "
access_token=" "
access_token_secret=" "

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):

    def on_data(self,data):

        try:
            json_data = json.loads(data)
            tweet = json_data["text"]
            output = f'{time_format} ---> {tweet} + "\n"'
            print(output)
            producer.send('awesome',bytes(output,encoding='utf8'))


            self.producer.produce(bytes(json.dumps(tweet),"utf-8"))
        except (KeyError,UnicodeEncodeError,AttributeError) as e:
            pass			
            #print("Error on data: %s" % str(e) )
        

        return True	
        

# Initialize instance of the subclass
printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret
)




while True:
	
	# Filter realtime Tweets by keyword

	msg = f'{time()},{printer.filter(track=["IPL"])}'

	# send to Kafka
	#producer.send('topic: awesome', bytes(msg, encoding='utf8'))    ##sends to topic weather
	#print(f'sending data to kafka, #{count}')
	sleep(10)
