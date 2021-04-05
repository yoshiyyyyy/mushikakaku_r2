import time
from celery import shared_task

@shared_task
def sleepy(wait):
    time.sleep(wait)
    return None
