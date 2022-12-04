from urllib import request

URL = 'http://localhost:8000/'

response = request.urlopen(URL)
print(response.read())
