from django.db import models

GENDER = [("MALE", 'male'),
          ("Femaile", 'female'),
          ]
KHARIF = [("RICE", 'rice'),
          ("MAIZE", 'maize'),
          ("MILLET", 'millet'),
          ("RAGI", 'ragi'),
          ("PULSES", 'pulses'),
          ("SOYABEAN", 'soyabean'),
          ("GROUND NUT", 'ground nut'), ]
RABI = [("WHEAT", 'wheat'),
        ("BARLEY", 'barley'),
        ("OATS", 'oats'),
        ("GRAM", 'gram'),
        ("MUSTARD", 'mustard'),
        ]
LOAN = [("YES", 'yes'),
        ("NO", 'no'),
        ]


# Create your models here.


class Register(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    confirmation = models.CharField(max_length=16)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username


class Profile(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    acres = models.IntegerField()
    kharif = models.CharField(max_length=20, choices=KHARIF)
    rabi = models.CharField(max_length=20, choices=RABI)
    loan = models.CharField(max_length=10, choices=LOAN)

    def __str__(self):
        return self.name
