from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=60)

class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    index = models.CharField(max_length = 20)
    categorie = models.ForeignKey(Categories)