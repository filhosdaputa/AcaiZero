from django.db import models


# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class adicional(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome