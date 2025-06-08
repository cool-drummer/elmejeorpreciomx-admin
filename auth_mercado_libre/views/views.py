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
        'client_id': '5730485929518412',
        'client_secret': 'SvQ5IGhctNnq1xPmSvHbfVncogW4mdpA',
        'code': request.GET.get('code'),
        'redirect_uri': 'https://admin.elmejorprecio.mx/auth/callback/'
    }
    response = requests.post(url, headers=headers, data=data)
    print('////////////////////////////////////////////////////////////////////////////////////')
    print(response.status_code)
    print(response.json())
    print('////////////////////////////////////////////////////////////////////////////////////')
    return Response({"OK": "OK"})
