from django.db import models

class ProductCart(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, related_name='product_cart')
    products = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.PositiveSmallIntegerField()

class Cart(models.Model):
    products = models.ManyToManyField('products.Product',through=ProductCart, related_name='product_cart')
    user = models.OneToOneField('users.user', on_delete = models.CASCADE, related_name='cart')


# Create your models here.
