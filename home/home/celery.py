import os
from celery import Celery
from django.conf import settings

from celery.schedules import crontab
from celery.schedules import timedelta

# Установка переменной окружения для работы Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# Создание экземпляра приложения Celery
app = Celery('home', broker='redis://localhost:6379/0')

# Загрузка настроек из объекта настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')



app.conf.beat_schedule = {
    'print_time_task': {
        'task': 'celeryone.tasks.print_time_task',
        'schedule': 10
    },
}
app.conf.timezone = 'Europe/Minsk'
app.autodiscover_tasks()