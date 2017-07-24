from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^produtos/$', views.produtos),
    url(r'^produtos_1/$', views.produtos_1),
    url(r'^acaienergy/$', views.acaienergy1),
    url(r'^acaienergy_1/$', views.acaienergy_1),
    url(r'^acaicreme/$', views.acaicreme1),
    url(r'^acaicreme_1/$', views.acaicreme_1),
    url(r'^acai1/$', views.acai1),
    url(r'^casadinho/$', views.casadinho1),
    url(r'^casadinho_1/$', views.casadinho_1),
    url(r'^acaimix/$', views.acaimix1),
    url(r'^acaimix_1/$', views.acaimix_1),
    url(r'^acai_1/$', views.acai_1),
    url(r'^finalizar/$', views.finalizar),
    url(r'^pagamento/$', views.pagamento),
    url(r'^sorvete/$', views.sorvete),
    ]
