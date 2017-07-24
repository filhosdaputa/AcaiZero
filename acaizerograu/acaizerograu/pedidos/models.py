from django.db import models
from outros.models import produto, adicional, acai, acaimix, casadinho, acaienergy, acaicreme

# Create your models here.
class item(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
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
    itens = models.ForeignKey(produto)
    total = models.DecimalField(max_digits=5, decimal_places=2, default='0')

    def __str__(self):
        return str(self.id)

class comanda_acai(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    itens = models.ForeignKey(acai)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

class comanda_acaimix(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    itens = models.ForeignKey(acaimix)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

class comanda_casadinho(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    itens = models.ForeignKey(casadinho)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

class comanda_acaienergy(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    itens = models.ForeignKey(acaienergy)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)

class comanda_acaicreme(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    itens = models.ForeignKey(acaicreme)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id)