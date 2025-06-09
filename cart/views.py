from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart, CartItem
from django.shortcuts import redirect
from products.models import Product
from django.contrib import messages

def cart(request):
    if request.user.is_authenticated:
        return render(request, 'cart/cart.html')
    else:
        messages.error(request, 'You must be logged in to access your cart.')
        return redirect('sign-in')
def add_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.filter(pid=product_id).first()
        quantity = request.POST.get('quantity')
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to add items to your cart.')
        return redirect('sign-in')
    else:
        cart = Cart.objects.filter(user=request.user).first()   
        item, created= CartItem.objects.get_or_create(cart=cart, product=product)
        if created == False:
            item.quantity = item.quantity + int(quantity)
           
        else:
            item.quantity = int(quantity)
           
        item.save()
       
        messages.success(request, f'{product.title} has been added to your cart.')
        return redirect('product', p_id=product.pid, p_title=product.title)

def remove_cart(request, p_id):
    pass