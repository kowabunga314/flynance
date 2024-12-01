from celery import shared_task
from datetime import datetime
from django.db import transaction
from pprint import pprint
import requests
from rest_framework.serializers import ValidationError
from typing import List

from aircraft.models import ManufacturerCrawl, ModelCrawl, AircraftCrawl
from aircraft.serializers import AircraftCrawlSerializer, AircraftDataMapper
from mission_match.parsers.planephd_parse import PlanePHDParser

@shared_task
# @transaction.atomic
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

    data_mapper = AircraftDataMapper(data=model_data)
    mapped_data = data_mapper.get_normalized_data()
    mapped_data['model_name'] = model.name
    mapped_data['manufacturer'] = model.manufacturer.name
    aircraft = AircraftCrawlSerializer(data=mapped_data)

    with transaction.atomic():
        model.last_parsed_at = datetime.now()
        if aircraft.is_valid():
            try:
                old_model = AircraftCrawl.objects.get(
                    model_name=aircraft.validated_data.get('model_name')
                )
                AircraftCrawl.objects.filter(
                    id=old_model.id
                ).update(**aircraft.validated_data)
            except AircraftCrawl.DoesNotExist:
                aircraft.save()
            model.save()
        else:
            raise ValidationError(aircraft.errors)

    # TODO: Produce event to translate crawler model to actual aircraft model

    return aircraft.validated_data

