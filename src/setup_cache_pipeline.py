from src.apis.apod_api import ApodApi
from src.configs.cache_connect import cache_connection

class SetupCachePipeline:
    @staticmethod
    def handle_apod_api_stage():
        return ApodApi.get()
        

    @staticmethod
    def handle_cache_data_stage(response_data):
        apod_date = response_data['date']
        apod_description = response_data['explanation']
        apod_url_image = response_data['url']
        apod_title = response_data['title']

        print('SET values to redis')

        cache_connection.set('apod_date', apod_date)
        cache_connection.set('apod_description', apod_description)
        cache_connection.set('apod_url_image', apod_url_image)
        cache_connection.set('apod_title', apod_title)


    @staticmethod
    def run():
        response = SetupCachePipeline.handle_apod_api_stage()
        SetupCachePipeline.handle_cache_data_stage(response)