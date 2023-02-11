import requests
import json
import pandas as pd
##  ______________________ todos los pokemones __________________________ #
# URL de la API de PokeAPI
url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=2000"
# url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=10"
response = requests.get(url)
if response.status_code == 200:
    pokemon_all = response.json()
    data_all = pokemon_all['results']
    all_pokemon = []
    for k in data_all:
        poke_pokemon = {}
        url_pokemon = k['url']
        response_url_pokemon = requests.get(url_pokemon)
        if response_url_pokemon.status_code == 200:
            # print('200 ok ->')
            data_pokemon = response_url_pokemon.json()
            ## id del pokemon
            pokemon_id = data_pokemon['id']
            poke_pokemon['pokemon_id']=pokemon_id
            # print(pokemon_id)

            ## nombre del pokemon
            name_pokemon = data_pokemon['name']
            poke_pokemon['name']=name_pokemon

            ## altura del pokemon
            height_pokemon = data_pokemon['height']

            ## peso del pokemon
            weight_pokemon = data_pokemon['weight']

            ## peso del pokemon
            descripction = f'La altura del pokemon {round(float(height_pokemon)*0.1,2)} m y su peso es {round(float(weight_pokemon)*0.1,2)} kg'
            poke_pokemon['descripction']=descripction
            for k in data_pokemon['stats']:
                poke_pokemon[k['stat']['name']]=k['base_stat']

            ## Juegos en los que esta presente el pokemon
            url_imagen= data_pokemon['sprites']['other']
            pokemon_image=url_imagen['official-artwork']['front_default']
            poke_pokemon['img']=pokemon_image
            all_pokemon.append(poke_pokemon)
        else:
            print('404')
    # Guarda los datos del Pokémon en un archivo local en formato JSON
    with open("dbpokemon.json", "w") as file:
        json.dump(all_pokemon, file)
    print("Exito ...")
else:
    print("Falló ...")
df = pd.read_json('dbpokemon.json', orient = 'registros')
# guardar en formato csv
df.to_csv('dbpokemon.csv', index=False)