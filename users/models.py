from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=127)
    street = models.CharField(max_length=127)
    number = models.IntegerField()
    complement = models.CharField(max_length=127)
    user = models.OneToOneField("users.user", on_delete=models.CASCADE)
    ...


class User(models.Model):
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
