import requests

endpoint = "https://shiny-space-zebra-6qj6wjxvrxj2rx79-8000.app.github.dev/"

response = requests.get(endpoint, json={'query': "hello world"})

print(response.text)
# print(response.json())
print(response.status_code)