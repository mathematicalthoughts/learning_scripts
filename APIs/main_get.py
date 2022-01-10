import requests
import json

#MÉTODO GET

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = { 
        'name' : 'maths_thoughts',
        'language':'python',
        'level':'orange belt'
    }
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:

        print('*'*33)
        print('Primer Método para trabajar objetos JSON')
        response_json = response.json()
        origin = response_json['origin']
        print(origin)

        print('*'*33)
        print('Segundo Método para trabajar objetos JSON')
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)