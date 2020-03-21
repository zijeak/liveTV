from django.conf.urls import include, url
from django.contrib import admin
from tv import views

urlpatterns = [
    url(r'index/(?P<id>\d*)$', views.index,name="index"),
]