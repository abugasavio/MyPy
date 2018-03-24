import pika
import time


def pdf_process_function(msg):
    print(" PDF processing")
    print(" Received %r" % msg)    
    time.sleep(5)
    print(" PDF processing finished")
    return


url = ''
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='pdfprocess')


def callback(ch, method, properties, body):
    pdf_process_function(body)


channel.basic_consume(callback, queue='pdfprocess', no_ack=True)

channel.start_consuming()

connection.close()
