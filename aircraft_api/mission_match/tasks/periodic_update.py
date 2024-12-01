from celery import shared_task
from datetime import datetime, timedelta
from django.db.models import Q
import logging
from typing import List
# logger = logging.getLogger('__name__')

@shared_task
def periodic_update():
    from aircraft.models import ModelCrawl
    from mission_match.tasks.get_aircraft_performance import get_aircraft_performance

    logging.debug('Starting periodic update task...')
    threshold = datetime.now() - timedelta(days=30)
    next_model = ModelCrawl.objects.filter(
        Q(last_parsed_at__lt=threshold) | Q(last_parsed_at=None)
    ).order_by('last_parsed_at').first()
    logging.debug(f'Updating model: {next_model.name}')
    print(f'Updating model: {next_model.name}')
    task = get_aircraft_performance.s(next_model.name)
    task()


