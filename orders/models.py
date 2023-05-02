from django.db import models


class Status(models.TextChoices):
    REALIZADO = 'Pedido Realizado'
    ANDAMENTO = 'Pedido em Andamento'
    CONCLUIDO = 'Pedido Concluido'

class Order(models.Model):
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.REALIZADO)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.