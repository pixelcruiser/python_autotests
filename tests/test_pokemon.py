import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c6b15210d116ba75b48082baa996e6a2'
HEADER = {'Content-Type': 'application/json','trainer_token' : TOKEN}
TRAINER_ID = '12905'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response_trainer_id():
    response_get = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == 'pixelcruiser' 


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'accelgor' 

@pytest.mark.parametrize('key, value',[('name', 'accelgor'),('trainer_id', TRAINER_ID), ('id','175374')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value