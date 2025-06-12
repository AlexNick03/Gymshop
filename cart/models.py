from django.db import models
from products.models import Product
from accounts.models import User
from shortuuid.django_fields import ShortUUIDField
class Cart(models.Model):
    cid = ShortUUIDField(unique=True,auto_created=True ,length=10, max_length=30, prefix='cart', alphabet='abcdefgh12345')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    cart_total = models.PositiveIntegerField(default = 0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"
    def cart_total(self):
        return sum(item.subtotal() for item in CartItem.objects.filter(cart=self))
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    subtotal = models.PositiveIntegerField(default = 0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in Cart {self.cart.id}"
    def subtotal(self):
        return self.product.price * self.quantity
    class Meta:
        unique_together = ('cart', 'product')