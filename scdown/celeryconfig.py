import os

BROKER_URL = os.getenv("CLOUDAMQP_URL", 'amqp://')
CELERY_RESULT_BACKEND = os.getenv("MONGOLAB_URI", 'mongodb://127.0.0.1:27017/')

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
