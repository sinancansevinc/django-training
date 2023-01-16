import requests

endpoint_url = "http://127.0.0.1:8000/api/players"

response = requests.get(endpoint_url)
print(response.json())