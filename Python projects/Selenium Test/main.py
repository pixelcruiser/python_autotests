import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c6b15210d116ba75b48082baa996e6a2'
HEADER = {'Content-Type': 'application/json','trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)