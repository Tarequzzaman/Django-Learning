from django.conf.urls import url, include
from django.contrib import admin
from .views import create_post, get_post
urlpatterns = [
    url(r"create_post", create_post),
    url(r'get_post', get_post)
]
