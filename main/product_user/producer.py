import json
import pika
import os
from dotenv import load_dotenv
load_dotenv()

queue_url = os.getenv("RABBIT_MQ_URL")

params = pika.URLParameters(queue_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

if channel.is_open:
    def publish(method, body):
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties = properties)
else:
    print('Check your configuration')