from __future__ import absolute_import, unicode_literals
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aircraft_api.settings')
from django.apps import apps
# from django.conf import settings
import logging

from celery import Celery, shared_task


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aircraft_api.settings')

app = Celery('aircraft_api')

logger = logging.getLogger('__name__')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
print(f"Discovered tasks: {app.tasks.keys()}")

@shared_task
def debug_task():
    # Task logic
   logger.debug('Executing debug task...')
   print('Executing debug task...')