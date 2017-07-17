from django.db import models

# Create your models here.
class caixa(models.Model):
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.total)