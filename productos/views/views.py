import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

from auth_mercado_libre.models import MercadoToken
from productos.utility import build_products

@api_view(['POST'])
def product(request):
    products = build_products(request.data.get('product'))
    return Response(products)
