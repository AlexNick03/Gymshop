from django.urls import path
from . import views

urlpatterns = [
    path('suplimente/', views.suplimente, name = 'suplimente'),
    path('haine/', views.haine, name = 'haine'),
    path('product/<str:p_id>-<str:p_title>', views.product, name = 'product'),
]