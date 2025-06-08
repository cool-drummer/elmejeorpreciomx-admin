from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


@api_view(['GET'])
def test(request):
    url = "https://auth.mercadolibre.com.mx/authorization?response_type=code&client_id=2392720368406147&redirect_uri=https://admin.elmejorprecio.mx/auth/callback"
    # url = "https://api.mercadolibre.com/users/me"
    response = requests.get(url)
    if response.status_code == 200:
        print('///////////////////////////////////////////')
        print(response)
        print('///////////////////////////////////////////')
        try:
            user_data = response.json()
            print('--------------------------------------')
            print(user_data)
            print('--------------------------------------')
        except Exception as ex:
            print(response.__dict__)
            print(ex)
            return Response({"PUTO": "DAN"})
    else:
        print('**************************************')
        print(f"Error {response.status_code}: {response.text}")
        print('**************************************')
    return Response({"PUTO": "DAN"})
