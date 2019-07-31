import requests
import json

if __name__ == "__main__":
    url = 'http://httpbin.org/get?nombre=iden&curso=api'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        parced = json.loads(content)
        print(json.dumps(parced, indent=2, sort_keys=True))
