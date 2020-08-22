from django.conf.urls import url
from .views import our_blog, single_post, create_or_edit_comment


urlpatterns = [
    url(r'^$', our_blog, name='our_blog'),
    url(r'^(?P<pk>\d+)/', single_post, name='post'),
    url(r'^new/$', create_or_edit_comment, name='comment'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_comment, name='edit_post')
    ]
