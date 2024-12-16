from src.configs.rabbit_connect import rabbitConnection
import pika

class RabbitService:
    @staticmethod
    def send(message):
        rabbitConnection.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=message,
        )
