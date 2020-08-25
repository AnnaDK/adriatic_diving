from django.conf.urls import url
from .views import quiz_page, quiz_answer


urlpatterns = [
    url(r'^$', quiz_page, name='quiz'),
    url(r'^(?P<pk>\d+)/', quiz_answer, name='answer'),
    
    ]

