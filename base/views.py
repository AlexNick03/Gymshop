from django.shortcuts import render
from products.models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
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
   
def search_product(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)[:5]
    return render(request, 'base/search_results.html', {'products': products})


def subscribe(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You have to login to subscribe to our newsletter.')
        return redirect('sign-in')
    if request.user.is_subscribed:
        messages.warning(request, 'You are already subscribed to our newsletter.')
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        mail_subject = 'Gym Shop Newsletter Subscription'
        message = render_to_string('base/newsletter.html', {
            'user': request.user.username,
            
        })
        email = EmailMessage(
            mail_subject, message, to = [email]
        )
        if email.send():
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            request.user.is_subscribed = True
            request.user.save()
        else:
            messages.error(request, 'There was an error sending the email. Please check if the email you''ve''enterd is valid.')
    return redirect('home')