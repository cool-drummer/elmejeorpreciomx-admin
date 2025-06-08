from rest_framework.decorators import api_view
from rest_framework.response import Response

# import requests


@api_view(['GET'])
def callback(request):
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
        'redirect_uri': 'TU_REDIRECT_URI',
        'code_verifier': 'TU_CODE_VERIFIER'
    }
    print('////////////////////////////////////////////////////////////////////////////////////')
    print(request)
    print(data)
    print('////////////////////////////////////////////////////////////////////////////////////')
    return Response({"OK": "OK"})
