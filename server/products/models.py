from django.db import models


class Category(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)


# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    category = models.CharField(max_length=150, unique=True)
