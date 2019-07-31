import requests
import json

if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = {'nombre':'Iden', 'curso':'APIs'}
    
    response = requests.post(url, data=json.dumps(payload))

    if response.status_code == 200:
        content = response.content
        parced = json.loads(content)
        print(json.dumps(parced, indent=2, sort_keys=True))