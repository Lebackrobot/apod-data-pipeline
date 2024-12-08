import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
rabbitConnection = connection.channel()

