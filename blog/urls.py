from django.conf.urls import url
from .views import blog, single_post


urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^(?P<pk>\d+)/', single_post, name='post'),
    
    ]
