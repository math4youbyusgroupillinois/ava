import os


DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'changeme',     
        'USER': 'changeme',
        'PASSWORD': 'changeme',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

HAYSTACK_CONNECTIONS = {
    #'default': {
    #    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #    'URL': 'http://127.0.0.1:9200/',
    #    'INDEX_NAME': 'haystack',
    #},

    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },

}

MANDRILL_API_KEY = "changeme"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
