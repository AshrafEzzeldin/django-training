# django_celery/celery.py

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicplatform.settings")

app = Celery("musicplatform")

app.conf.imports = ['albums.tasks']

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'every-24hours': {
        'task': 'albums.tasks.check_email',
        'schedule': crontab(minute=0, hour='*/24'),
    },
}

app.autodiscover_tasks()
