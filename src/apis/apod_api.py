import requests

from dotenv import load_dotenv
from os import getenv

load_dotenv

class ApodApi:
    @staticmethod
    def _url():
        return getenv('APOD_API_KEY')

    @staticmethod
    def get():
        url = ApodApi._url()
        response = requests.get(url)
        return response.json()