from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^acai1/$', views.acai1),
    url(r'^acai_1/$', views.acai_1),
    url(r'^finalizar/$', views.finalizar),
    url(r'^pagamento/$', views.pagamento),
    url(r'^sorvete/$', views.sorvete),
    ]
