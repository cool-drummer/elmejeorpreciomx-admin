from django.urls import path
from test_dan.views import test

urlpatterns = [
    path('test/', test),
]
