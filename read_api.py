import requests

api_url = "http://192.168.0.156:8788/gapminder?country=Malaysia"

resp = requests.get(api_url)

data = resp.json()

print(data)
