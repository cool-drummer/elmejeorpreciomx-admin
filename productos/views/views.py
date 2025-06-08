from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from auth_mercado_libre.models import MercadoToken

@api_view(['GET'])
def product(request):
    return Response({"OK": "OK"})
