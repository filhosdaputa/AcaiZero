from django.contrib import admin
from outros.models import produto, adicional
from pedidos.models import comanda,item
from caixa.models import caixa

admin.site.register(produto)
admin.site.register(adicional)
admin.site.register(comanda)
admin.site.register(item)
admin.site.register(caixa)


