from celery import shared_task
from datetime import datetime, timedelta
from django.db import transaction
from django.db.models import Q
from typing import List

from aircraft.models import ModelCrawl, AircraftCrawl
from mission_match.tasks.get_aircraft_performance import get_aircraft_performance

@shared_task
@transaction.atomic
def periodic_update():
    threshold = datetime.now() - timedelta(days=30)
    next_model = ModelCrawl.objects.filter(
        Q(last_parsed_at__lt=threshold) | Q(last_parsed_at=None)
    ).order_by('last_parsed_at').first()
    print(f'Updating model: {next_model.name}')
    task = get_aircraft_performance.s(next_model.name)
    task()


