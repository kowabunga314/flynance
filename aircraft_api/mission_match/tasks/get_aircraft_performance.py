from celery import shared_task
from django.db import transaction
from pprint import pprint
import requests
from rest_framework.serializers import ValidationError
from typing import List

from aircraft.models import ManufacturerCrawl, ModelCrawl, AircraftCrawl
from aircraft.serializers import AircraftCrawlSerializer, AircraftDataMapper
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

    parser_response = parser.get_generic_performance(model.__dict__)
    model_data = parser_response.get('data')
    print('Got model data:')
    pprint(model_data)

    data_mapper = AircraftDataMapper(data=model_data)
    mapped_data = data_mapper.get_normalized_data()
    mapped_data['model_name'] = model_name
    aircraft = AircraftCrawlSerializer(data=mapped_data)

    if aircraft.is_valid():
        aircraft.save()
    else:
        raise ValidationError(aircraft.errors)

    # TODO: Produce event to translate crawler model to actual aircraft model

    return aircraft.validated_data

