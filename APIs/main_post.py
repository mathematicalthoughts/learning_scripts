import requests
import json

#MÉTODO POST

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = { 
        'name' : 'maths_thoughts',
        'language':'python',
        'level':'orange belt'
    }
    headers = {
        'Content-Type':'application/json',
        'access-token':'56789'
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers
        print(headers_response)
        server = headers_response['Server']
        print(server)