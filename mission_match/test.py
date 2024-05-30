
from planephd_parse import PlanePHDParser
import sys


def test_import_aircraft(url=None):
    parser = PlanePHDParser()
    parser.get_aircraft_performance(url=url)


if __name__ == '__main__':
    args = sys.argv[1:]
    url = args[0]
    test_import_aircraft(url=url)
