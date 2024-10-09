
from planephd_parse import PlanePHDParser
from pprint import pprint
import sys

from aircraft.models import ModelScrape


def test_import_aircraft(url=None):
    parser = PlanePHDParser()
    parser.get_aircraft_performance(url=url)


def test_identify_aircraft(url=None):
    parser = PlanePHDParser()
    parser.identify_models()


def test_crawl_aircraft(url=None):
    parser = PlanePHDParser()
    parser.crawl_aircraft()


def test_crawl_manufacturers(url=None):
    parser = PlanePHDParser()
    manufacturers = parser.identify_manufacturers()
    pprint(manufacturers)

def test_aircraft_performance():
    aircraft = ModelScrape.objects.first()
    parser = PlanePHDParser()
    aircraft_data = parser.get_aircraft_performance(aircraft)
    pprint(aircraft_data)


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0] if len(args) > 0 else None
    test_aircraft_performance()
