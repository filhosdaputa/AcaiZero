from django.contrib import admin
from outros.models import produto, adicional, acai, acaimix, casadinho, acaienergy, acaicreme, milkshake, fondue, petit, sorvete
from pedidos.models import comanda,item, comanda_acai, comanda_acaimix, comanda_casadinho, comanda_acaienergy
from caixa.models import caixa

admin.site.register(produto)
admin.site.register(adicional)
admin.site.register(comanda)
admin.site.register(item)
admin.site.register(caixa)
admin.site.register(acai)
admin.site.register(acaimix)
admin.site.register(acaienergy)
admin.site.register(casadinho)
admin.site.register(acaicreme)
admin.site.register(milkshake)
admin.site.register(fondue)
admin.site.register(petit)
admin.site.register(sorvete)
admin.site.register(comanda_acai)
admin.site.register(comanda_acaimix)
admin.site.register(comanda_acaienergy)
admin.site.register(comanda_casadinho)


