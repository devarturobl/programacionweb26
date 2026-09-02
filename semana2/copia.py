import streamlit as st
import random
import requests

# Configuración de la página (debe ser el primer comando de Streamlit)
st.set_page_config(page_title="Pokédex Pro", page_icon="🔴", layout="centered")

def get_pokemon_data(pokemon):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        st.error(f"Error al consumir la API: {e}")
        return None

def get_random_pokemon_id():
    # La API actual tiene más de 1000 Pokémon, lo dejamos en 890 según tu código
    random_id = random.randint(1, 1025)
    return get_pokemon_data(str(random_id))

# Interfaz principal
st.title("🔴 Pokédex Profesional")
st.markdown("Busca los datos de tu Pokémon favorito o genera uno al azar.")

# Controles de búsqueda
col1, col2 = st.columns(2)
data = None

with col1:
    pokemon_name = st.text_input("Ingrese el nombre o ID del Pokémon:")
    if st.button("Buscar Pokémon 🔍", use_container_width=True):
        if pokemon_name:
            data = get_pokemon_data(pokemon_name.lower().strip())
        else:
            st.warning("Por favor, ingresa un nombre o ID.")

with col2:
    st.write("¿No sabes cuál buscar?")
    if st.button("Generar Pokémon Aleatorio 🎲", use_container_width=True):
        data = get_random_pokemon_id()

# Despliegue de datos con diseño profesional
if data:
    st.divider() # Línea divisoria elegante
    
    # Encabezado con Nombre e ID
    st.header(f"{data['name'].capitalize()} #{data['id']}")
    
    # Organización en pestañas
    tab1, tab2, tab3 = st.tabs(["📊 Resumen", "⚔️ Estadísticas Base", "⚔️ Movimientos"])
    
    with tab1:
        img_col, info_col = st.columns([1, 1.5])
        
        with img_col:
            # Imagen oficial de alta calidad
            img_url = data['sprites']['other']['official-artwork']['front_default']
            st.image(img_url, use_container_width=True)
            
            # Reproductor de audio (Grito del Pokémon)
            if 'cries' in data and 'latest' in data['cries']:
                st.audio(data['cries']['latest'], format="audio/ogg")
                
        with info_col:
            # Tipos del Pokémon usando etiquetas Markdown
            tipos = [t['type']['name'].upper() for t in data['types']]
            st.markdown(f"**Tipos:** `{ '` | `'.join(tipos) }`")
            
            # Uso de métricas para datos numéricos
            st.write("### Fisiología")
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                # Convertir decímetros a metros
                st.metric(label="Altura", value=f"{data['height'] / 10} m")
            with m_col2:
                # Convertir hectogramos a kilogramos
                st.metric(label="Peso", value=f"{data['weight'] / 10} kg")
    
    with tab2:
        st.write("### Nivel de Poder")
        # El máximo valor base en Pokémon suele ser 255 (Blissey en HP)
        MAX_STAT = 255 
        
        for stat in data['stats']:
            stat_name = stat['stat']['name'].upper()
            stat_value = stat['base_stat']
            
            # Normalizar el valor para la barra de progreso (0.0 a 1.0)
            progress_value = min(stat_value / MAX_STAT, 1.0)
            
            st.markdown(f"**{stat_name}:** {stat_value}")
            st.progress(progress_value)

    with tab3:
        st.write("### Movimientos")

elif data is False:
    st.error("Pokémon no encontrado. Verifica el nombre o ID.")
        
