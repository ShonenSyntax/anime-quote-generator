import requests
import json
import random

url = "https://api.animechan.io/v1/quotes/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    quote = data['data']['content']
    anime = data['data']['anime']['name']
    character = data['data']['character']['name']

    print(f"{character} ({anime}): \n{quote}")

else:
    print('Failed to fetch quote,Status Code: ',response.status_code)