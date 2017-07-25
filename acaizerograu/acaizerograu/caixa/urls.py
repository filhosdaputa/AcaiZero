from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.caixa1),
    url(r'^retirada/$', views.retirada),
    url(r'^retirada_1/$', views.retirada_1),
    url(r'^fechar/$', views.fechar),
    url(r'^fechar_1/$', views.fechar_1),
    ]
