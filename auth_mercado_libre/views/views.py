from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


@api_view(['GET'])
def callback(request):
    print('*****************************')
    print(request.__dict__)
    print('*****************************')
    url = 'https://api.mercadolibre.com/oauth/token'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': '2392720368406147',
        'client_secret': 'f1GThB6n9jyCbAgFgK4eWJNsipjGlPwd',
        'code': request.GET.get('code'),
        'redirect_uri': 'https://admin.elmejorprecio.mx'
    }
    response = requests.post(url, headers=headers, data=data)
    print('////////////////////////////////////////////////////////////////////////////////////')
    print(response.status_code)
    print(response.json())
    print('////////////////////////////////////////////////////////////////////////////////////')
    return Response({"OK": "OK"})
