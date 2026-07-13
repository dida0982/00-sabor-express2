import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    print(data_json)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")