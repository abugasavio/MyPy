import os
import pika
import time
import logging

url = ''
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='pdfprocess')

for i in range(10000):
    channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information ' + str(i))
    time.sleep(1)

print("[x] Message sent to consumer")
connection.close()
