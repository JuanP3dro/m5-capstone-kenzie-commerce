from django.db import models


class User(models.Model):
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
