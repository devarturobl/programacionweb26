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
    random_id = random.randint(1, 890)
    return get_pokemon_data(str(random_id))



st.title("Semana 2 - Introducción a Streamlit API")
data = get_random_pokemon_id()

# Desplegar la información del pokemon
if data:
    st.subheader(f"Nombre: {data['name'].capitalize()}")
    st.image(data['sprites']['front_default'], width=200)
    st.image(data['sprites']['back_default'], width=200)
    st.write(f"ID: {data['id']}")
    st.write(f"Altura: {data['height']}")
    st.write(f"Peso: {data['weight']}")
    st.write("Tipos:")
    for type_info in data['types']:
        st.write(f"- {type_info['type']['name'].capitalize()}")
