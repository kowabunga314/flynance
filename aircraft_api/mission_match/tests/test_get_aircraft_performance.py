# tests.py (in the same app where tasks.py is located)
from django.test import TestCase

from aircraft.models import ModelScrape
from mission_match.tasks.get_aircraft_performance import get_aircraft_performance


expected_result = {'url': 'https://planephd.com/wizard/details/146/CESSNA-120-specifications-performance-operating-cost-valuation', 'make': 'CESSNA', 'model': 'CESSNA 120', 'engine_hp': 85, 'cruise': 100, 'range': 390, 'fuel_burn_cruise': 4.8, 'stall_speed': 43, 'rate_of_climb': 640, 'ceiling': 15500, 'takeoff_distance': 650, 'landing_distance': 460, 'takeoff_distance_50': 1850, 'landing_distance_50': 1530, 'gross_weight': 1450, 'empty_weight': 818, 'fuel_capacity': 25, 'total_cost_of_ownership': 12458.19, 'total_fixed_cost': 3762.05, 'total_variable_cost': 8696.14, 'engine_manufacturer': 'Cont Motor', 'engine_model': 'C-85-12', 'engine_tbo': 1800, 'engine_tbo_years': 12}


class AircraftPerformanceTaskTest(TestCase):
    fixtures = ['manufacturer_scrape', 'model_scrape']

    def test_basic_task(self):
        # Get a model to use for tests
        model = ModelScrape.objects.first()
        # Call the task synchronously and get the result
        result = get_aircraft_performance.apply(args=(model.name,))

        # Ensure that the task completes successfully
        self.assertTrue(result.successful(), "Task did not complete successfully")

        # Check the result of the task
        self.assertEqual(result.result, expected_result, "Task did not return the expected result")

    def test_multiple_import(self):
