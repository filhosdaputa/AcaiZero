from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^realizados/$', views.realizados),
    ]
