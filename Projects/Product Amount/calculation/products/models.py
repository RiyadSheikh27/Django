from django.db import models

# Create your models here.
from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.product} - {self.amount}"