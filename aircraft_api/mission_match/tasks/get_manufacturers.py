from celery import shared_task
from django.db import transaction
import requests

from aircraft.models import ManufacturerScrape, ModelScrape
from mission_match.planephd_parse import PlanePHDParser

@shared_task
@transaction.atomic
def get_manufacturer_data():
    parser = PlanePHDParser()
    mfgr_data = parser.identify_manufacturers()
    manufacturers = [
        ManufacturerScrape(**mfgr)
        for mfgr in mfgr_data
    ]
    ManufacturerScrape.objects.bulk_create(manufacturers)
