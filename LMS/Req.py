import requests

url = "http://127.0.0.1:8000/api/v1/students/"


res = requests.get(url)
data = res.json()
print(data)








#Pagination
#page_size -> value like 10, for 10 response in one page
#page offset -> limit=100 offset=110

#Golabl pagination
#Custom Pagination
