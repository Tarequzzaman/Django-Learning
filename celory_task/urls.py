from django.conf.urls import url, include


from .views import  run_task

urlpatterns = [
    url(r'run_task', run_task),
]