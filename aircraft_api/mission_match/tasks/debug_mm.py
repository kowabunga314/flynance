from celery import shared_task


@shared_task
def debug_mm():
    print('Debugging mission_match...')