from django.contrib import admin
from .models import Product , Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cid', 'title', 'category_image']
    search_fields = ['title']
admin.site.register(Category, CategoryAdmin)    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'stock','price', 'is_available', 'category', 'date', 'updated'] 
    search_fields = ['title', 'pid', 'category__title']
admin.site.register(Product, ProductAdmin)


    