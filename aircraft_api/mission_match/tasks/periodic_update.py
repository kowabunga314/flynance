from celery import shared_task
from datetime import datetime, timedelta
from django.conf import settings
from django.db.models import Q
import logging
from typing import List
logger = logging.getLogger(__name__)

@shared_task
def periodic_update():
    from aircraft.models import ModelCrawl
    from mission_match.tasks.get_aircraft_performance import get_aircraft_performance

    logger.debug('Starting periodic update task...')
    threshold = datetime.now() - timedelta(days=30)
    try:
        queryset = ModelCrawl.objects.filter(
            Q(last_parsed_at__lt=threshold) | Q(last_parsed_at=None)
        ).order_by('last_parsed_at')

        if queryset.count() == 0:
            if settings.ALWAYS_UPDATE_MODELS:
                queryset = ModelCrawl.objects.all().order_by('last_parsed_at')
            else:
                logger.debug('No models to update')
                return

        next_model = queryset.first()
        logger.debug(f'Updating model: {next_model.name}')
        print(f'Updating model: {next_model.name}')
        task = get_aircraft_performance.s(next_model.name)
        task()
    except AttributeError as e:
        raise AttributeError(
            f'There was a problem processing the least recently updated model.'
        ) from e
