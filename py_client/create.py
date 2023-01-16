import requests
endpoint_url = "http://127.0.0.1:8000/api/players/"

my_data = {'name': 'Michael Jordan','sports':'basketball','estimated_price':100}

response = requests.post(endpoint_url,json = my_data)

