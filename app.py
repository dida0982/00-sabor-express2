import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    data_json = response.json()
    data_restaurant ={}
    for item in data_json:
        name_restaurant = item['Company']
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = []
        
        data_restaurant[name_restaurant].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description'],
        })
        
else:
    print('Error:', response.status_code)
    
for name_restaurant, items in data_restaurant.items():
    name_restaurant = f'{name_restaurant}.json'
    with open(name_restaurant, 'w') as file_restaurant:
        json.dump(items, file_restaurant, indent=4)