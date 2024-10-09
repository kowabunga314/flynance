from celery import shared_task
from django.db import transaction
import requests
from typing import List

from aircraft.models import ManufacturerScrape, ModelScrape
from mission_match.planephd_parse import PlanePHDParser

@shared_task
@transaction.atomic
def get_model_data(mfgrs: List[str]=[]):
    parser = PlanePHDParser()
    model_data = []

    if len(mfgrs):
        mfgrs = ManufacturerScrape.objects.filter(name__in=mfgrs)
    else:
        mfgrs = ManufacturerScrape.objects.all()

    for mfgr in mfgrs:
        model_data = [*model_data, *parser.identify_models(mfgr)]
    with transaction.atomic():
        for model in model_data:
            # Replace manufacturer string with reference
            model['manufacturer'] = mfgrs.get(name=model.get('manufacturer'))
            # Create database record for models
            ModelScrape.objects.update_or_create(**model)

