from django.apps import AppConfig


class MissionMatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mission_match'

    def ready(self):
        from django_celery_beat.models import IntervalSchedule, PeriodicTask
        from celery import current_app

        tasks = current_app.tasks.keys()
        print(f'Got tasks: {tasks}')

        # Define the interval (e.g., every 10 minutes)
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.SECONDS,  # Options: SECONDS, MINUTES, HOURS, DAYS, WEEKS
        )

        # Register the task
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="Update oldest model every 30 seconds",  # Unique name
            task="mission_match.tasks.periodic_update.periodic_update",  # Full path to the task
        )
