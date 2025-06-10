from django.urls import path
from . import views
urlpatterns = [
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('change_quantity/<str:p_id>', views.change_quantity, name='change_quantity'),
    path('remove_item/<str:p_id>', views.remove_item, name='remove_item'),
]