import requests

from auth_mercado_libre.utility import get_access_token


def build_products(product, limit, offset):
    response = {}
    key_mercado_libre = get_access_token()
    url = 'https://api.mercadolibre.com/products/search?status=active&site_id=MLM&q=' + product + '&limit=' + limit + '&offset=' + offset
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + key_mercado_libre
    }
    response_mercado = requests.get(url, headers=headers)
    data = response_mercado.json()
    for product_result in data['results']:
        url = 'https://api.mercadolibre.com/items/' + product_result['id'] + '/prices'
        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + key_mercado_libre
        }
        response_mercado = requests.get(url, headers=headers)
        print('------------------------------------------')
        print(response_mercado)
        print('------------------------------------------')
        data_product = response_mercado.json()
    response['mercado-libre'] = data
    return response
