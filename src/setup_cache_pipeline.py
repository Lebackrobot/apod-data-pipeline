from src.apis.apod_api import ApodApi
from deep_translator import GoogleTranslator
from src.configs.logging_config import logging
from src.configs.cache_connect import cache_connection
from time import sleep

log = logging.getLogger(__name__)

class SetupCachePipeline:
    @staticmethod
    def handle_apod_api_stage():
        try:
            return ApodApi.get()
    
        except Exception as error:
            log.info('APOD API endpoint error')
            sleep(60)

            SetupCachePipeline.handle_apod_api_stage()
        

    @staticmethod
    def handle_cache_data_stage(response_data):
        googleTranslator = GoogleTranslator(source='en', target='pt')

        apod_date = response_data['date']
        apod_description = response_data['explanation']
        apod_url_image = response_data['url']
        apod_title = response_data['title']

        apod_description = googleTranslator.translate(apod_description)
        apod_title = googleTranslator.translate(apod_title)

        log.info(apod_description)        
        log.info(apod_title)

        log.info('SET values to redis')

        cache_connection.set('apod_date', apod_date)
        cache_connection.set('apod_description', apod_description)
        cache_connection.set('apod_url_image', apod_url_image)
        cache_connection.set('apod_title', apod_title)

        log.info('SET apod_date')
        log.info('SET apod_description')
        log.info('SET apod_url_image')
        log.info('SET apod_title')

        log.info('SET values to redis (OK)')


    @staticmethod
    def run():
        log.info('Run setup cache pipeline')
        response = SetupCachePipeline.handle_apod_api_stage()
        SetupCachePipeline.handle_cache_data_stage(response)