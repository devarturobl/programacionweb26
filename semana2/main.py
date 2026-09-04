import streamlit as st
import random
import requests # Libreria para consumir apis

# Funicón para consumir la API de pokemon
def get_pokemon_data(pokemon):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        st.error(f"Error al consumir la API: {e}")
        return None


# Funcion para generar un número aleatorio entre 1 y 890
def get_random_pokemon_id():
    random_id = random.randint(1, 1025)
    return get_pokemon_data(str(random_id))



st.title("Semana 2 - Introducción a Streamlit API")
data = get_random_pokemon_id()

# Desplegar la información del pokemon
if data:
   st.image(data['sprites']['other']['showdown']['front_default']) 
   st.header(f"¿Quien es este pokemon? = {data['name'].upper()}")
   st.subheader(f"Su Id es: {data['id']}")
   for ability in data['abilities']:
       st.write(f"Su habilidad es: {ability['ability']['name']}")
   st.image(data['sprites']['other']['official-artwork']['front_default']) 
   for type in data['types']:
       st.write(f"Su tipo es: {type['type']['name']}")