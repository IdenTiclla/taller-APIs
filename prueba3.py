import requests
import json

if __name__ == "__main__":
    payload = {'nombre':'Iden', 'curso':'APIs'}
    url = 'http://httpbin.org/get'
    response = requests.get(url, payload)
    print(response.url)
    if response.status_code == 200:
        content = response.content
        parced = json.loads(content)
        print(json.dumps(parced, indent=2, sort_keys=True))
