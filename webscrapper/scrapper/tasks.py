from celery import shared_task
import time
import os
import requests
from django_celery_beat.models import PeriodicTask,IntervalSchedule
from .models import Info

@shared_task
def add(x, y):
    time.sleep(10)
    return x + y

@shared_task
def download_image(image_url,save_directory,image_name):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory, image_name)
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return image_path 
    return None

@shared_task
def create_info():
    Info.objects.create(info = "This is added by celery beat")

schedule, created = IntervalSchedule.objects.get_or_create(
    every = 1,
    period = IntervalSchedule.SECONDS
)

PeriodicTask.objects.update_or_create(
    name = "Create Info",
    defaults = {
        'task': 'scrapper.tasks.create_info',
        'interval' : schedule,
        'args':'[]'
    }
    
)