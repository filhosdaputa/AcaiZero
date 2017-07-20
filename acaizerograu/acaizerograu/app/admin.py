from django.contrib import admin
from outros.models import produto, adicional, acai
from pedidos.models import comanda,item, comanda_acai
from caixa.models import caixa

admin.site.register(produto)
admin.site.register(adicional)
admin.site.register(comanda)
admin.site.register(item)
admin.site.register(caixa)
admin.site.register(acai)
admin.site.register(comanda_acai)


