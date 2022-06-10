from requests import get


print(get('http://localhost:8080').json())