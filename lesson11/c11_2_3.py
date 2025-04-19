import json
import urllib.request


url = 'http://httpbin.org/get'

with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)
    print(type(r))
