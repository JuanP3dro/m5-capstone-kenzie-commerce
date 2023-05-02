from django.db import models

class Cart(models.Model):
    products = models.ManyToManyField('products.Product', related_name='order')
    user_id = models.OneToOneField('users.user', on_delete = models.CASCADE)

# Create your models here.
