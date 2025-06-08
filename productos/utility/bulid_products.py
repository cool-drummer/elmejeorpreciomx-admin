import requests

from auth_mercado_libre.utility import get_access_token


def build_products(product):
    response = {}
    key_mercado_libre = get_access_token()
    url = 'https://api.mercadolibre.com/products/search?status=active&site_id=MLM&q=' + product
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + key_mercado_libre
    }
    response_mercado = requests.get(url, headers=headers)
    data = response_mercado.json()
    response['mercado-libre'] = data
    return response
