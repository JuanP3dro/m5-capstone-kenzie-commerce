from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=127)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=127)
    user = models.OneToOneField("users.user", on_delete=models.CASCADE)
