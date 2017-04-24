# polls/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^page/(?P<page>[0-9]+)$', views.index, name='index'),
    url(r'^search/(?P<keyword>\S+)/page/(?P<page>[0-9]+)$', views.search, name="search"),
]