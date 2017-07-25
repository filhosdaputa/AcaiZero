from django.db import models
import datetime

# Create your models here.
class caixa(models.Model):
    tipo = models.CharField(max_length= 10, default="Entrada")
    data = models.DateTimeField(default=datetime.datetime.now())
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.total)