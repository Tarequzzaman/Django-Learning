from django.conf.urls import url, include
from .views import  create_user, get_user

urlpatterns = [
  #url(r'^admin/', admin.site.urls),
    url(r'create_user', create_user),
    url(r'get_user/', get_user),
]