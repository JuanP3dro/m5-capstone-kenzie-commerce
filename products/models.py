from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.PositiveSmallIntegerField()
    is_available = models.BooleanField()
