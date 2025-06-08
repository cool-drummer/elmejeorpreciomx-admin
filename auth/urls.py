from django.urls import path
from auth.views import callback

urlpatterns = [
    path('callback/', callback),
]
