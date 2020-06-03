from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=300)

class ProductInCart(models.Model):
    sku = models.CharField(max_length=10)
    quantity = models.IntegerField(default=1)
