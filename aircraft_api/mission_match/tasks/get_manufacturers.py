from celery import shared_task
from django.db import transaction
import requests

from aircraft.models import ManufacturerCrawl, ModelCrawl
from mission_match.planephd_parse import PlanePHDParser

@shared_task
@transaction.atomic
def get_manufacturers():
    parser = PlanePHDParser()
    mfgr_data = parser.identify_manufacturers()
    manufacturers = [
        ManufacturerCrawl(**mfgr)
        for mfgr in mfgr_data
    ]
    ManufacturerCrawl.objects.bulk_create(manufacturers)
