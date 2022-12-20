import requests

ENDPOINT = 'https://pokeapi.co/api/v2/pokemon/ditto'

response = requests.get(ENDPOINT)
# print(response.status_code)
resp = response.json()
abilities = resp['abilities']

arr = []
for ability in abilities:
    arr.append(ability['ability']['name'])

print(arr)

