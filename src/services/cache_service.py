from src.configs.cache_connect import cache_connection

class CacheService:
    @staticmethod
    def set(key, value):
        cache_connection.set(key, value)
    
    @staticmethod
    def get(key):
        return cache_connection.get(key)