from django.db import models

class Cart(models.Model):
    products = models.ManyToManyField('products.Product', through='ProductCart', related_name='order')
    user_id = models.OneToOneField('users.user', ON_DELETE = models.CASCADE)

# Create your models here.
