import requests

URL = "http://127.0.0.1:8000/aiinfo/"

response = requests.get(url = URL)
print("response: ", response)
data = response.json()
print('data:\n',data)