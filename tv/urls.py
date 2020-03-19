from django.conf.urls import include, url
from django.contrib import admin
from tv import views

urlpatterns = [
    url(r'live$', views.live),
    url(r'index$', views.index),
]