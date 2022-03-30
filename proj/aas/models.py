from django.db import models


# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    confirmation = models.CharField(max_length=16)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username