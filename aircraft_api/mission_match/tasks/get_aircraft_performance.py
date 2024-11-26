from celery import shared_task
from django.db import transaction
import requests
from typing import List

from aircraft.models import ManufacturerCrawl, ModelCrawl, AircraftListing
from aircraft.serializers import AircraftModelSerializer
from mission_match.planephd_parse import PlanePHDParser

@shared_task
@transaction.atomic
def get_aircraft_performance(model_name):
    parser = PlanePHDParser()

    if model_name is not None and isinstance(model_name, str):
        try:
            model = ModelCrawl.objects.get(name=model_name)
        except ModelCrawl.DoesNotExist:
            raise ValueError(f'Aircraft model {model_name} not found.')
    else:
        raise ValueError('Argument "model_name" must be a string.')

    model_data = parser.get_aircraft_performance(model.__dict__)
    aircraft = AircraftListing(**{
        **model_data,
        'listing_url': model_data.get('url'),
        'model_name': model_data.get('model'),
        'model_variant': model_data.get('model'),
        'engine_count': 1,
        'manufacturer': model_data.get('make'),
        'gear_type': 'fixed',
        'flap_type': 'electric',
    })

    with transaction.atomic():
        # Create database record for model
        aircraft.save()

