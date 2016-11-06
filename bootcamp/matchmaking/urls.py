# coding: utf-8

from django.conf.urls import patterns, include, url
from bootcamp.matchmaking import views

urlpatterns = [
    url(r'^$', views.matches, name='matchmaking'),
]