from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 80)
    brand = models.CharField(max_length = 50, default = "")
    description = models.TextField(default = "")
    in_cart = models.BooleanField(default = False)
    tag = models.CharField(max_length = 50, default = "")
    price_buy = models.IntegerField()
    price_sell = models.IntegerField()
    price_sell_no_discount = models.IntegerField()
    sku = models.CharField(max_length = 10)

    def __str__(self):
        return self.title
