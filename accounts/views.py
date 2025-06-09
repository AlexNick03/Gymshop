from django.shortcuts import render
from accounts.forms import SignupForm
from accounts.forms import P_ResetForm
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate , logout
from accounts.models import User
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from .tokens import account_activation_token
from django.template.loader import render_to_string
from cart.models import Cart
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import password_reset_token

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
          
          user = User.objects.get(email=email)
          
          if user is not None:
                if not user.is_active:
                   
                    activateEmail (request, user, email)
                else:
                    user = authenticate(request, email=email, password=password)
                    if user is not None:
                        login(request, user)
                        if user.is_staff:
                            return redirect('admin:index')
                        return redirect('home')
                    else:
                        messages.warning(request, 'Email or password is incorrect')
          else:
            messages.warning(request, 'Email or password is incorrect')
        
        except:
            messages.warning(request, 'User does not exist')
            
    return render(request, 'accounts/login.html')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your account.'
    message = render_to_string('accounts/vmail.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(
        mail_subject, message, to = [to_email]
    )
    if email.send() :
        messages.success(request, 'Your account is not activated. Please check your email for the activation link.')
    else:
        messages.error(request, 'There was an error sending the email. Please check if the email you''ve''enterd is valid.')

#  Activation view
def activate(request, uidb64, token):
    
    User = get_user_model()
    
    if User :
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    if user is not None and user.is_active == False and account_activation_token.check_token(user, token):
            user.is_active = True
            create_cart(request, user)
            user.save()
            messages.success(request, 'Your account has been activated successfully!')
            return redirect('sign-in')

    else:
       
        if user.is_active:
            messages.info(request, 'Your account is already activated.')
            return redirect('sign-in')
        else: 
            messages.error(request, 'Activation link is invalid! Try to login for a new activation link.')
            return redirect('sign-in')
        


# # Sign up view
def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        
        if form.is_valid():
            user = form.save()
            activateEmail (request, user, form.cleaned_data.get('email'))
            return redirect('sign-in')
            
    else:
        form = SignupForm()
        
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    
    logout(request)
   
    return redirect('sign-in')
        
def account(request):
    return render(request, 'accounts/account.html')

def password_reset_view(request):

    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            user = User.objects.get(email=email)
            if user:
                resetPasswordEmail(request, user, email)
                return redirect('password-reset')
            else:
                messages.error(request, 'Your email is not registered with us. Please sign up first.')      
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')    
    return render(request, 'accounts/resetp.html')

def resetPasswordEmail(request, user, to_email):
    mail_subject = 'Reset your password.'
    message = render_to_string('accounts/rmail.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': password_reset_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    if email.send():
        messages.success(request, 'A link to reset your password has been sent to your email.')
    else:
        messages.error(request, 'There was an error sending the email. Please check if the email you''ve''enterd is valid.')

def password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    
    if User:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    if user is not None and password_reset_token.check_token(user, token):
        if request.method == 'POST':
            form = P_ResetForm(request.POST or None)
            new_password = form.data.get('password1')
            confirm_password = form.data.get('password2')
            if new_password == confirm_password and form.is_valid():
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been reset successfully!')
                return redirect('sign-in')
        else:
            form = P_ResetForm()
        context = {
            'form': form,
            'user': user
        }   
        return render(request, 'accounts/newp.html', context)
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('sign-in')
    
def create_cart(request, user):
   cart = Cart.objects.create(user=user)
   cart.save()