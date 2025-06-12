from django.db import models
from products.models import Product
from accounts.models import User
from cart.models import Cart, CartItem
from shortuuid.django_fields import ShortUUIDField

class Courier(models.Model):
    courier_id = ShortUUIDField( unique=True ,length=10, max_length=30, prefix='cour', alphabet='abcdefgh12345')
    name = models.CharField(max_length=255)
    workin_days_for_delivery = models.PositiveIntegerField(default = 2)
    price = models.PositiveIntegerField(default = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

class Order(models.Model):
    oid = ShortUUIDField( unique=True ,length=10, max_length=30, prefix='ord', alphabet='abcdefgh12345')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)
    total = models.PositiveIntegerField(default = 0)
    adress = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='pending')    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    subtotal = models.PositiveIntegerField(default = 0)
