#  How to connect to an API using Python  (I am using Pokemon API )

import requests # For requestion API

base_url = "https://pokeapi.co/api/v2/"  # the link of API

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"    # this is the style that pokeapi use Like this:  (pokemon/pikachu)
    response = requests.get(url)

    if response.status_code == 200:    # status_code is number ..Like 200 for success 404 for error and many others
        pokemon_data = response.json() # get data as a json file format
        return pokemon_data           # we will get all data of pikachu 
        
    else: 
        print(f"Failed to retrive data {response.status_code}")
    
pokemon_name = "typhlosion"

pokemon_info=get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")