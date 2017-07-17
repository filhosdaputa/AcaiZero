from django.db import models
from outros.models import produto, adicional

# Create your models here.
class item(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    )
    produto1 = models.ForeignKey(produto)
    adicionais = models.ManyToManyField(adicional,)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    obs = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.produto1)

class comanda(models.Model):
    id = models.AutoField(primary_key=True)
    itens = models.ManyToManyField(item,)
    total = models.DecimalField(max_digits=5, decimal_places=2, default='0')

    def __str__(self):
        return str(self.id)