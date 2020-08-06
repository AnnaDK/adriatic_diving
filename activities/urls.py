from django.conf.urls import url, include
from .views import  all_activities


urlpatterns = [
    url(r'^$', all_activities, name='activities'),
    
]