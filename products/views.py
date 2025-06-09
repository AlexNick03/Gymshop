from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def suplimente(request):
    products = Product.objects.filter(category=1)
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/suplimente.html', {'page_obj': page_obj})


def add_cart(request, p_id):
  pass

def haine(request):
  pass
def product(request, p_title, p_id):
    product = Product.objects.filter(pid = p_id, title=p_title).first()
    return render(request, 'products/product.html', {'product': product})

    
