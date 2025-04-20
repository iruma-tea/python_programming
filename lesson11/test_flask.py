import requests

# r = requests.post('http://127.0.0.1:5000/post', data={'username': 'mike'})
# r = requests.put('http://127.0.0.1:5000/post', data={'username': 'mike'})
# r = requests.delete('http://127.0.0.1:5000/post', data={'username': 'mike'})
# r = requests.get('http://127.0.0.1:5000/post', data={'username': 'mike'})

r = requests.get('http://127.0.0.1:5000/employee/jun', data={'name': 'jun'})
print(r.text)
r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)
r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'jun', 'new_name': 'sakai'})
print(r.text)
r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'sakai'})
print(r.text)
