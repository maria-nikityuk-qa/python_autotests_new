import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f5da087371b865860c447714cd07040f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '38233'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
    
def test_name_of_trainer():
    response_gets = requests.get(url = f'{URL}/trainers/{TRAINER_ID}')
    assert response_gets.json()['trainer_name'] == 'Marie'

