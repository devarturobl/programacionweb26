import requests
import streamlit as st

# Inicializar el estado de la página si no existe
if "page" not in st.session_state:
    st.session_state.page = 1

def adelante():
    st.session_state.page += 1

def atras():
    st.session_state.page -= 1

def consumo(page):
    response = requests.get(f"https://thesimpsonsapi.com/api/characters?page={page}")
    if response.status_code == 200:
        data = response.json()
        # Nota: adapta 'results' o la clave si la API devuelve una estructura distinta
        for personaje in data.get("results", []):
            st.markdown(personaje.get("name", "Desconocido"))
    else:
        st.error("Error al consultar la API")

st.title("The Simpson API")

# Se pasa la referencia de la función (sin paréntesis)
st.button("Next", on_click=adelante)
st.button("Back", on_click=atras)

# Mostrar la página actual y consumir los datos
st.caption(f"Página actual: {st.session_state.page}")
consumo(st.session_state.page)
