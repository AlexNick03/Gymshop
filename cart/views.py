from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart, CartItem
from django.shortcuts import redirect
from products.models import Product
from django.contrib import messages
from django.core.paginator import Paginator


def cart(request):
    if request.user.is_authenticated:
        cart  = Cart.objects.get(user = request.user)
        items = CartItem.objects.filter(cart=cart)
        page_number = request.GET.get('page',1)
        paginator  = Paginator(items, 1)
        page_obj =  paginator.get_page(page_number)
        cart_total = cart.cart_total
        cart_id = cart.cid
        if request.headers.get("HX-Request") == "true":

            return render(request, "cart/cart_partial.html", {"page_obj": page_obj,
                                                              "cart_total": cart_total,
                                                              "cart_cid": cart_id})
        else:
            return render(request, "cart/cart.html", {"page_obj": page_obj,
                                                      "cart_total": cart_total,
                                                      "cart_cid": cart_id})
    
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

def change_quantity(request, p_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        item = CartItem.objects.get(product__pid=p_id)
        item.quantity = quantity
        item.save()
        return redirect('cart')
def remove_item(request, p_id):
    if request.method == 'POST':
        item = CartItem.objects.get(product__pid=p_id)
        item.delete()
        return redirect('cart')