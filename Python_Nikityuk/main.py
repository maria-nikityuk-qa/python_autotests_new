import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f5da087371b865860c447714cd07040f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }

body_post_pokemons = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_post_pokemons)
print(response.json())
id = response.json()['id']




body_put_pokemons = {
    "pokemon_id": id,
    "name": "Lara",
    "photo_id": -1
}
response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_pokemons)
print(response_put.json())




body_pokeball = {
    "pokemon_id": id
}
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.json())

