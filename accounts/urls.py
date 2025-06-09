from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('login/', views.login_view, name = 'sign-in'),
    path('signup/', views.signup_view, name = 'sign-up'),
    path('signout/', views.logout_view, name = 'sign-out'),
    path('account/', views.account, name = 'account'),
    path('password-reset/', views.password_reset_view, name = 'password-reset'),
    path('activate/<uidb64>/<token>', views.activate, name = 'activate'),
    path('password-reset-confirm/<uidb64>/<token>', views.password_reset_confirm, name='password-reset-confirm'),
]