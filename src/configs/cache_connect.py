import redis

cache_connection = redis.Redis(
    host='localhost',
    password='password',
    port=6379, 
    db=0, 
    protocol=3
)