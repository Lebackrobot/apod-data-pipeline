from src.apis.apod_api import ApodApi
from src.configs.cache_connect import cache_connection
from time import sleep

class SetupCachePipeline:
    @staticmethod
    def handle_apod_api_stage():
        try:
            return ApodApi.get()
    
        except Exception as error:
            print('APOD API endpoint error')
            sleep(60)

            SetupCachePipeline.handle_apod_api_stage()
        

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

        print('SET apod_date')
        print('SET apod_description')
        print('SET apod_url_image')
        print('SET apod_title')

        print('SET values to redis (OK)')


    @staticmethod
    def run():
        print('>>> run setup cache pipeline')
        response = SetupCachePipeline.handle_apod_api_stage()
        SetupCachePipeline.handle_cache_data_stage(response)