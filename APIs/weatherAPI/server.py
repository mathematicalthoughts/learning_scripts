import requests
import json

if __name__ == '__main__':
    url = 'https://www.metaweather.com/es/'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.content)