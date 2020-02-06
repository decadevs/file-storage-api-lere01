import dj_database_url
from decouple import config


def generate_url(DEBUG, url):
    if DEBUG == False:

        return {"default": {
            "ENGINE": "djongo",
            "HOST": url
        }}
    else:
        return {
            "default": {
                "ENGINE": "djongo",
                'NAME': 'buckets_db',
                'HOST': 'localhost',
                'PORT': 27017
            }

        }
