import requests
import json

if __name__ == "__main__":
    payload = {'nombre':'Iden', 'curso':'APIs'}
    url = 'http://httpbin.org/get'
    
    response = requests.get(url, payload)
    print(response.url)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)