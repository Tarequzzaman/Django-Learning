from celery import shared_task
import time

@shared_task
def sample_task_1(counter):
    email = "hassanzadeh.sd@gmail.com"
    time.sleep(1000)
    print(email)
    print(counter)
    return '{} Done!'.format(counter)