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
CATEGORY = [("AGRICULTURE", 'agriculture'),
            ("AQUACULTURE", 'aquaculture')
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


class Tools(models.Model):
    tcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=12)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Seeds(models.Model):
    seeds_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=32)
    s_category = models.CharField(max_length=20, choices=CATEGORY)
    s_quantity = models.IntegerField()
    s_price = models.FloatField()

    def __str__(self):
        return self.s_name