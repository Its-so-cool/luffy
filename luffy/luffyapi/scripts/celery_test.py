from celery import Celery


broker = 'redis://127.0.0.1:6379/1'

backend = 'redis://127.0.0.1:6379/2'

app = Celery(__name__,broker=broker,backend=backend)