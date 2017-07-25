from django.db import models


# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class adicional(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class acai(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    img = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class sorvete(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class acaimix(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class casadinho(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class acaienergy(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    img = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class acaicreme(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    img = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class milkshake(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tamanho = models.CharField(max_length=1)
    img = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class petit(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class fondue(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome