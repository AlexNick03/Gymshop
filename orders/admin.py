from django.contrib import admin
from  .models import Order, OrderItem, Courier

class CourierAdmin(admin.ModelAdmin):
    list_display = ['courier_id', 'name', 'phone','price','workin_days_for_delivery', 'created_at', 'updated_at']
admin.site.register(Courier, CourierAdmin)  

class OrderAdmin(admin.ModelAdmin):
    list_display = ['oid', 'user', 'total','courier','adress','created_at',  'updated_at', 'status']
    list_filter = ['status']

admin.site.register(Order, OrderAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'subtotal']

admin.site.register(OrderItem, OrderItemsAdmin)

