import requests
import json

#MÉTODO PUT & DELETE

if __name__ == '__main__':
    url = 'http://httpbin.org/put' #url = 'http://httpbin.org/delete'
    payload = { 
        'name' : 'maths_thoughts',
        'language':'python',
        'level':'orange belt'
    }
    headers = {
        'Content-Type':'application/json',
        'access-token':'56789'
    }
    response = requests.put(url, data=json.dumps(payload), headers=headers) #response = requests.delete(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers
        server = headers_response['Server']
        print(server)