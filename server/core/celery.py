
import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


app.conf.broker_url = 'amqp://rabbitmq'  # points to the RabbitMQ service
# app.conf.result_backend = 'rpc://' 

app.autodiscover_tasks()

app.config_from_object(settings, namespace='CELERY')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
