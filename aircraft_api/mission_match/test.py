
from planephd_parse import PlanePHDParser
from pprint import pprint
import sys


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


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0] if len(args) > 0 else None
    test_crawl_aircraft(url=url)
