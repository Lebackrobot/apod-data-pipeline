import redis
from os import getenv

CACHE_PASSWORD = getenv('CACHE_PASSWORD')
CACHE_USERNAME = getenv('CACHE_USERNAME')
CACHE_HOST = getenv('CACHE_HOST')
CACHE_PORT = getenv('CACHE_PORT')

cache_connection = redis.Redis(
    host=CACHE_HOST,
    password=CACHE_PASSWORD,
    username=CACHE_USERNAME,
    port=CACHE_PORT,
    db=0, 
    ssl = True 
)
