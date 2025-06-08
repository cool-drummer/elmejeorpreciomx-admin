from django.urls import path
from productos.views import product

urlpatterns = [
    path('product/', product),
]
