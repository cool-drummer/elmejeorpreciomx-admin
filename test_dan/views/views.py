from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


@api_view(['GET'])
def test(request):
    url = "https://api.mercadolibre.com/users/me"
    headers = {
        "Authorization": "Bearer 6092293103071468-060113-eea6d10dd6e1b71c8ba9a7ac4fd0ba7b-1312992254"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        print('--------------------------------------')
        print(user_data)
        print('--------------------------------------')
    else:
        print('**************************************')
        print(f"Error {response.status_code}: {response.text}")
        print('**************************************')
    return Response({"PUTO": "DAN"})
