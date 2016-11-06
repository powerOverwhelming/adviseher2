# coding: utf-8

from django.conf.urls import url
from bootcamp.matchmaking import views

urlpatterns = [
    url(r'^match$', views.matches, name='matchmaking'),
]