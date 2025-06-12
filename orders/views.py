from django.shortcuts import render
from cart.models import Cart, CartItem
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from django.shortcuts import redirect
# Create your views here.
def checkout(request):
    if request.method == 'POST':
        cart_cid = request.POST.get('cart_cid')
        items = CartItem.objects.filter(cart__cid = cart_cid)
        for item in items:
            if item.quantity > item.product.stock:
                if item.product.stock == 0:
                    messages.error(request, f'Out of stock for {item.product.title}')
                    item.delete()
                    return redirect('cart')
                messages.info(request, f'Not enough stock for {item.product.title}. The current stock is {item.product.stock}')
                return redirect('cart')        
        return render(request, 'orders/checkout.html')
    
