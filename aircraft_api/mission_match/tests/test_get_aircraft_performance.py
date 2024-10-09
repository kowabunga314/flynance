# tests.py (in the same app where tasks.py is located)
from django.test import TestCase

from aircraft.models import ModelScrape
from mission_match.tasks.get_aircraft_performance import get_aircraft_performance

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
        self.assertEqual(result.result, 12, "Task did not return the expected result")
