#How to connect with an API using Pyhton
import requests
base_url = "https://pokeapi.co/api/v2/"
#--------------------------------------------------------------------------------------
pokemon_name = input("What Pokémon are you searching for (don't use spaces or special characters)?: ")
pokemon_name = pokemon_name.lower()

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data retrieved!")
        poke_data = response.json()
        return poke_data
    else:
        print("Pokémon doesn't exist")

poke_info = get_info(pokemon_name)

if poke_info:
    print(f"Name: {poke_info["name"].capitalize()}")
    print(f"Pokedex Number: {poke_info["id"]}")
    print(f"Height: {poke_info["height"] / 10}m")
    print(f"Weight: {poke_info["weight"]/ 10}kg")
    if 1 <= poke_info["id"] <= 151:
        print("Region Introduced: Kanto")
    elif 152 <= poke_info["id"] <= 251:
        print("Region Introduced: Johto")
    elif 252 <= poke_info["id"] <= 386:
        print("Region Introduced: Hoenn")
    elif 387 <= poke_info["id"] <= 493:
        print("Region Introduced: Sinnoh")
    elif 494 <= poke_info["id"] <= 649:
        print("Region Introduced: Unova")
    elif 650 <= poke_info["id"] <= 721:
        print("Region Introduced: Kalos")
    elif 722 <= poke_info["id"] <= 809:
        print("Region Introduced: Alola")
    elif 810 <= poke_info["id"] <= 898:
        print("Region Introduced: Galar")
    elif 899 <= poke_info["id"] <= 905:
        print("Region Introduced: Hisui")
    elif 906 <= poke_info["id"] <= 1025:
        print("Region Introduced: Paldea")