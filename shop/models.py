from django.db import models
from django.conf import settings
from django.utils import timezone

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(default = '', max_length = 80)
    brand = models.CharField(max_length = 50, default = "")
    description = models.TextField(default = "")
    in_cart = models.BooleanField(default = False)
    image_root = models.ImageField(default = 'img/product-3_dAtZf9b.jpg',upload_to = 'img/')
    tag = models.CharField(max_length = 50, default = "")
    price_buy = models.FloatField(default = 0)
    price_sell = models.FloatField(default = 0)
    price_sell_no_discount = models.FloatField(default = 0)
    sku = models.CharField(default = '',max_length = 10)

    def __str__(self):
        return self.title
