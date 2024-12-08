from src.configs.rabbit_connect import rabbitConnection

class RabbitService:
    @staticmethod
    def send(message):
        rabbitConnection.basic_publish(
            exchange='',
            routing_key='subscriptions',
            body=message    
        )