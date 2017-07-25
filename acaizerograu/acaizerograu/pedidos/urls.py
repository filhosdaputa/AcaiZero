from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^milkshake/$', views.milkshake1),
    url(r'^milkshake_1/$', views.milkshake_1),
    url(r'^fondue/$', views.fondue1),
    url(r'^fondue_1/$', views.fondue_1),
    url(r'^petit/$', views.petit1),
    url(r'^petit_1/$', views.petit_1),
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
    url(r'^finalizar_1/$', views.finalizar_1),
    url(r'^pagamento/$', views.pagamento),
    url(r'^pagamento_1/$', views.pagamento_1),
    url(r'^sorvete/$', views.sorvete1),
    url(r'^sorvete_1/$', views.sorvete_1),
    ]
