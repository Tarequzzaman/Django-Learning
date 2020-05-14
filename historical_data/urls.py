from django.conf.urls import url, include
from .views import insert_pice, get_all_data, update

urlpatterns = [
  #url(r'^admin/', admin.site.urls),
      url(r'^insert/', insert_pice),
      url(r'get_all_data/', get_all_data),
      url(r'update', update)
]