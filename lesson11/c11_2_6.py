import json

import urllib
import urllib.request


payload = {"key1": "value1", "key2": "value2"}
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/put', data=payload, method='PUT')

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
