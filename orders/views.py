from django.shortcuts import render
from cart.models import Cart, CartItem
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, OrderItem, Courier
from django.shortcuts import redirect
# Create your views here.
def checkout(request):
    if request.method == 'POST':
        cart_cid = request.POST.get('cart_cid')
        cart = Cart.objects.get(cid=cart_cid)
        items = CartItem.objects.filter(cart__cid = cart_cid)
        for item in items:
            if item.quantity > item.product.stock:
                if item.product.stock == 0:
                    messages.error(request, f'Out of stock for {item.product.title}')
                    item.delete()
                    return redirect('cart')
                messages.info(request, f'Not enough stock for {item.product.title}. The current stock is {item.product.stock}')
                return redirect('cart')  
        couriers = Courier.objects.all()

        return render(request, 'orders/checkout.html', {'couriers': couriers, 'cart_total ': cart.cart_total, 'cart_cid': cart_cid})      
        
    
def place_order(request):
    if request.method == 'POST':
        cart_cid = request.POST.get('cart_cid')
        items = CartItem.objects.filter(cart__cid = cart_cid)
        create_order(request, user=request.user)
        curr_order = Order.objects.get(status='pending', user=request.user)
        for item in items:
            if item.quantity > item.product.stock:
                OrderItem.objects.filter(order=curr_order).delete()
                curr_order.delete()
                if item.product.stock == 0:
                    messages.error(request, f'Out of stock for {item.product.title}')
                    item.delete()
                    return redirect('cart')
                
                messages.info(request, f'Not enough stock for {item.product.title}. The current stock is {item.product.stock}')

                return redirect('cart')   
                 
            OrderItem.objects.create(order=curr_order, product=item.product, quantity=item.quantity)
        for item in OrderItem.objects.filter(order=curr_order):
            item.product.stock -= item.quantity
            item.product.save()
            CartItem.objects.filter(product=item.product, cart__cid = cart_cid).delete()
        
        courier_id = request.POST.get('courier')
        curr_order.courier = Courier.objects.get(id=courier_id)
        curr_order.adress =  request.POST.get('address')
        curr_order.phone =  request.POST.get('phone_number')
        curr_order.email = request.POST.get('email_adress')
        curr_order.country = request.POST.get('country')
        curr_order.county = request.POST.get('county')
        curr_order.city = request.POST.get('localitate')
        curr_order.postal_code =  request.POST.get('cod_postal')
        curr_order.first_name = request.POST.get('first_name')
        curr_order.last_name = request.POST.get('last_name') 
        curr_order.status = 'placed'
        curr_order.save()
        messages.success(request, 'Order has been placed successfully')
        return redirect('cart')

def create_order(request, user):
   order = Order.objects.create(user=user)
   order.save()

