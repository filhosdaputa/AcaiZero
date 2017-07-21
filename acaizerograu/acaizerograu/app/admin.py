from django.contrib import admin
from outros.models import produto, adicional, acai, acaimix
from pedidos.models import comanda,item, comanda_acai, comanda_acaimix
from caixa.models import caixa

admin.site.register(produto)
admin.site.register(adicional)
admin.site.register(comanda)
admin.site.register(item)
admin.site.register(caixa)
admin.site.register(acai)
admin.site.register(acaimix)
admin.site.register(comanda_acai)
admin.site.register(comanda_acaimix)


