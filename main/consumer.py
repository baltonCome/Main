import os
import django
import json
from django import db
import pika

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
# Rest of your code
from dotenv import load_dotenv
load_dotenv()

queue_url = os.getenv("RABBIT_MQ_URL")

from product_user.models import Product

params = pika.URLParameters(queue_url)

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
            product.save()
            print('Product Created')

        elif properties.content_type == 'product_updated':
            product = Product.objects.get(pk=data['data'])
            product.title = data['title']
            product.image = data['image']
            product.save()
            print('Product Updated')
        
        elif properties.content_type == 'product_deleted':
            product = Product.objects.get(pk=data['data'])
            product.delete()
            print('Product Deleted')
    

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
else :
    print('Failed to consume')