from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<vinylid>\d+)$', views.view),
    url(r'^add/$', views.add),
    url(r'^delete/$', views.delete),
]
