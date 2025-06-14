from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name = 'home'),
  path('search_api/', views.search_product, name = 'search_api'),
  path('about/', views.about, name = 'about'),
  path('contact/', views.contact, name = 'contact'),
  path('privacy/', views.privacy, name = 'privacy'),
  path('terms/', views.terms, name = 'terms'),
  path('refund/', views.refund, name = 'refund'),
  path('subscribe/', views.subscribe, name = 'subscribe'),
]