from django.urls import path
from auth_mercado_libre.views import callback

urlpatterns = [
    path('callback', callback),
]
