from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from taggit.managers import TaggableManager

class Category(models.Model):
    cid =ShortUUIDField(unique=True, length=10, max_length=30, prefix='cat',alphabet='abcdefgh12345')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category')
    

    class Meta:
        verbose_name_plural = 'Categories'
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title



class Product(models.Model):
    pid = ShortUUIDField(unique=True ,length=10, max_length=30, prefix='prd', alphabet='abcdefgh12345')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    price = models.DecimalField(max_digits=100000, decimal_places=2, default=1.99)
    #old_price = models.DecimalField(max_digits=100000, decimal_places=2, null=True, blank=True, default=2.99)
    description = models.TextField(null=True, blank=True, default='This is the product')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    specifications = models.TextField(null=True, blank=True, default='specification')
    tag = TaggableManager()
    stock = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix='sku', alphabet='1234567890')
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Products'

    def product_image(self):
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
            return self.title
    #def get_precent_discount(self):
            #new_price = (self.price/self.old_price) * 100
            #return new_price
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    images = models.ImageField(upload_to='product_images', default='product.jpg')
    alt_text = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Products Images'


   
            
