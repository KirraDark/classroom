# from celery import shared_task
#
# @shared_task
# def add(x, y):
#     return x + y
# print(add.delay (2,3))


from celery import Celery
import datetime
from home.celery import app

def print_time():
    now = datetime.datetime.now()
    print("Current time is:", now)

@app.task
def print_time_task():
    print_time()