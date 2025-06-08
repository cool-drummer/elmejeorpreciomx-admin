from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from auth_mercado_libre.models import MercadoToken

@api_view(['GET'])
def callback(request):
    url = 'https://api.mercadolibre.com/oauth/token'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': '5730485929518412',
        'client_secret': 'SvQ5IGhctNnq1xPmSvHbfVncogW4mdpA',
        'code': request.GET.get('code'),
        'redirect_uri': 'https://admin.elmejorprecio.mx/auth/callback'
    }
    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    new_token = MercadoToken(
        access_token = data.get('access_token'),
        token_type = data.get('token_type'),
        expires_in = data.get('expires_in'),
        scope = data.get('scope'),
        user_id = data.get('user_id'),
        refresh_token = data.get('refresh_token'),
    )
    new_token.save()
    return Response({"OK": "OK"})
