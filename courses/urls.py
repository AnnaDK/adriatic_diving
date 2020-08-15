from django.conf.urls import url, include
from .views import all_courses, one_course


urlpatterns = [
    url(r'^$', all_courses, name='courses'),
    url(r'^(?P<pk>\d+)/', one_course, name='course'),
    
    ]

