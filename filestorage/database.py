import dj_database_url


def generate_url(DEBUG, url):

    if DEBUG == False:
        return dj_database_url.parse(url, conn_max_age=600)
    return {
        'NAME': 'buckets_db',
        'HOST': 'localhost',
        'PORT': 27017
    }
