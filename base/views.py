from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request, 'base/home.html')
def refund(request):
    return render(request, 'base/retur.html')
def contact(request):
    return render(request, 'base/contact.html')
def about(request):
    return render(request, 'base/about_us.html')
def privacy(request):
    return render(request, 'base/privacy.html')
def terms(request):
    return render(request, 'base/terms_and_condition.html')
   

