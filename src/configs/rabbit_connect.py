import pika
import ssl

from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)

RABBITMQ_URI = getenv('RABBIT_URI')

context = ssl.create_default_context()

parameters = pika.URLParameters(RABBITMQ_URI)
parameters.ssl_options = pika.SSLOptions(context)

connection = pika.BlockingConnection(parameters)
rabbitConnection = connection.channel()

