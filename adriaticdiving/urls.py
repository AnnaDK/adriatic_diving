"""adriaticdiving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as urls_accounts
from courses import urls as urls_courses
from cart import urls as urls_cart
from quiz import urls as urls_quiz
from blog import urls as urls_blog
from django.views import static
from .settings import MEDIA_ROOT

# from search import urls as urls_search
# from checkout import urls as urls_checkout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^courses/', include(urls_courses)),
    url(r'^cart/', include(urls_cart)),
    url(r'^quiz/', include(urls_quiz)),
    url(r'^blog/', include(urls_blog)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]

