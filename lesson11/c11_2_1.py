import urllib.request


url = 'http://httpbin.org/get'

with urllib.request.urlopen(url) as f:
    print(f.read())
