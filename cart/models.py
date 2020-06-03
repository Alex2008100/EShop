from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(default=datetime.now)
    def add(product, product_price):
        CartItem.product = product
        CartItem.price = product_price
        models.Item.objects.create(cart=self.cart, product=product, unit_price=product_price, quantity=quantity)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price * (1 + TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.product
