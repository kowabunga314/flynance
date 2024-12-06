from __future__ import absolute_import, unicode_literals
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aircraft_api.settings')
from django.apps import apps
# from django.conf import settings
import logging
import sys

from celery import Celery, shared_task
from celery.signals import after_setup_logger


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aircraft_api.settings')

app = Celery('aircraft_api')

# @after_setup_logger.connect()
# def logger_setup_handler(logger, **kwargs ):
#     my_handler = logging.StreamHandler(sys.stdout)
#     my_handler.setLevel(logging.DEBUG) 
#     my_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #custom formatter
#     my_handler.setFormatter(my_formatter)
#     logger.addHandler(my_handler)

#     logging.info("My log handler connected -> Global Logging")

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# print(f"Discovered tasks: {app.tasks.keys()}")

@shared_task
def debug_task():
    # Task logic
   logger.debug('Executing debug task...')
   print('Executing debug task...')