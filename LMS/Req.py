import requests

url = "http://127.0.0.1:8000/api/v1/students/"


res = requests.get(url)
data = res.json()
print(data)
