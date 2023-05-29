import json
import pika

params = pika.URLParameters('amqps://waezmnsx:5ATtwcDKyZKVkAqxbGbW3mvrXcbfSlyv@goose.rmq2.cloudamqp.com/waezmnsx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

if channel.is_open:
    def publish(method, body):
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties = properties)
else:
    print('Check your configuration')