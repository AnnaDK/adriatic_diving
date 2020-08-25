from django.conf.urls import url
from .views import our_blog, single_post


urlpatterns = [
    url(r'^$', our_blog, name='blogposts'),
    url(r'^(?P<pk>\d+)/', single_post, name='post'),
  ]
