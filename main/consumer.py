import os
import django
import json
from django import db
import pika

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
# Rest of your code

from product_user.models import Product

params = pika.URLParameters('amqps://waezmnsx:5ATtwcDKyZKVkAqxbGbW3mvrXcbfSlyv@goose.rmq2.cloudamqp.com/waezmnsx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

if channel.is_open:

    channel.queue_declare(queue='main')

    def callback(ch, method, properties, body):
        print('Received in main')
        data = json.loads(body)
        print(data)

        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            # db.session.add(product)
            # db.session.commit()
            product.save()
            print('Product Created')

        elif properties.content_type == 'product_updated':
            # product = Product.query.get(data['data'])
            product = Product.objects.get(pk=data['data'])
            product.title = data['title']
            product.image = data['image']
            #db.session.commit()
            product.save()
            print('Product Updated')
        
        elif properties.content_type == 'product_deleted':
            # product = Product.query.get(data['data'])
            product = Product.objects.get(pk=data['data'])
            # db.session.delete(product)
            # db.session.commit()
            product.delete()
            print('Product Deleted')
    

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
else :
    print('Failed to consume')