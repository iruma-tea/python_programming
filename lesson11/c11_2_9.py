import requests


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post', data=payload)

print(r.status_code)  # 200
print(r.text)
print(r.json())
