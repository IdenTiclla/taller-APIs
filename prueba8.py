import requests
import json


if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = {'nombre':'Iden', 'curso':'python'}
    headers = {'Content-Type':'application/json', 'access-token':'12345'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers
        print(headers_response['Server'])
        parced = json.loads(response.content)
        print(json.dumps(parced, indent=2, sort_keys=True))