from django.conf.urls import url, include
from .views import all_courses, one_course


urlpatterns = [
    url(r'^$', all_courses, name='courses'),
    url(r'^$', one_course, name="course"),
    ]