from django.contrib import admin

from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at', 'cart_total']
    search_fields = ['user__username']
    list_filter = ['created_at', 'updated_at']

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity','subtotal', 'added_at']
    search_fields = ['cart__user__username', 'product__name']
    list_filter = ['added_at']

admin.site.register(CartItem, CartItemAdmin)