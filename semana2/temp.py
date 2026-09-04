import streamlit as st
import requests

# 1. Obtener datos
res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()

name = res["name"].upper()
hp = res["stats"][0]["base_stat"]
poke_id = f"N.° {res['id']:04d}"
height = res["height"] / 10
weight = res["weight"] / 10
img_url = res["sprites"]["other"]["official-artwork"]["front_default"]

# 2. Renderizar Card
with st.container(border=True):
    # Encabezado
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(name)
    with col2:
        st.subheader(f"PS {hp}")

    # Imagen
    st.image(img_url, use_container_width=True)
    
    # Barra de datos físicos
    st.caption(f"{poke_id} • Altura: {height} m • Peso: {weight} kg")
    st.divider()

    # Ataques
    col_atk1, col_atk2 = st.columns([3, 1])
    with col_atk1:
        st.markdown(f"**{res['moves'][0]['move']['name'].replace('-', ' ').title()}**")
    with col_atk2:
        st.markdown("**30**")