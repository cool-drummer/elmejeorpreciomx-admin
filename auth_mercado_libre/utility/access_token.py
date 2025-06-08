import requests

from auth_mercado_libre.models import MercadoToken


def get_access_token():
    access = MercadoToken.objects.filter(id=1).first()
    url = 'https://api.mercadolibre.com/oauth/token'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'client_id': '5730485929518412',
        'client_secret': 'SvQ5IGhctNnq1xPmSvHbfVncogW4mdpA',
        'refresh_token': access.refresh_token,
        'redirect_uri': 'https://admin.elmejorprecio.mx/auth/callback'
    }
    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    return data.get('access_token')
