import requests
import json
import pandas as pd
##  ______________________ Extracción todos los pokemones __________________________ #
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
            data_pokemon = response_url_pokemon.json()
            ## id del pokemon
            pokemon_id = data_pokemon['id']
            poke_pokemon['pokemon_id']=pokemon_id

            ## Nombre del pokemon
            name_pokemon = data_pokemon['name']
            poke_pokemon['name']=name_pokemon

            ## Altura del pokemon
            height_pokemon = data_pokemon['height']

            ## Peso del pokemon
            weight_pokemon = data_pokemon['weight']

            ## Descripcion del pokemon
            # Altura: decimetros a metros
            # Peso: hectogramos a kilogramos
            descripction = f'La altura del pokemon {round(float(height_pokemon)*0.1,2)} m y su peso es {round(float(weight_pokemon)*0.1,2)} kg'
            poke_pokemon['descripction']=descripction

            ## Habilidades del pokemon
            for k in data_pokemon['stats']:
                poke_pokemon[k['stat']['name']]=k['base_stat']

            ## Imagen del pokemon
            url_imagen= data_pokemon['sprites']['other']
            pokemon_image=url_imagen['official-artwork']['front_default']
            poke_pokemon['img']=pokemon_image
            all_pokemon.append(poke_pokemon)
        else:
            print('404')
    # Guardar en formato JSON
    with open("dbpokemon.json", "w") as file:
        json.dump(all_pokemon, file)
    print("Exito ...")
else:
    print("Falló ...")
df = pd.read_json('dbpokemon.json', orient = 'registros')
# Guardar en formato csv
df.to_csv('dbpokemon.csv', index=False)