import requests
import streamlit as st
import base64

# Configuración inicial de la página
st.set_page_config(
    page_title="The Simpsons API - Personajes", 
    page_icon="🟡", 
    layout="wide"
)

# Inicialización del estado de la página
if "page" not in st.session_state:
    st.session_state.page = 1

def siguiente():
    st.session_state.page += 1

def anterior():
    if st.session_state.page > 1:
        st.session_state.page -= 1

@st.cache_data(ttl=600)
def consumirapi(page):
    try:
        response = requests.get(f"https://thesimpsonsapi.com/api/characters?page={page}", timeout=5)
        if response.status_code == 200:
            return response.json().get("results", [])
    except Exception:
        pass
    return []

personajes = consumirapi(st.session_state.page)

# Función para la imagen de fondo
def set_background(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass

set_background("assets/background.jpg")

# Estilos CSS Avanzados (Simpsons Theme)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@700&display=swap');

        /* Encabezado Principal */
        .simpsons-header {
            text-align: center;
            padding: 10px 0 20px 0;
            width: 100%;
        }

        .simpsons-title {
            font-family: 'Bangers', cursive;
            color: #FED41D;
            font-size: 75px; /* Título más grande */
            letter-spacing: 3px;
            -webkit-text-stroke: 3.5px #000000;
            text-shadow: 6px 6px 0px #000000;
            margin: 0 auto;
            text-align: center;
            display: block;
        }

        /* Indicador de Página */
        .page-badge {
            background-color: #70D1FE;
            color: #000;
            font-family: 'Bangers', cursive;
            font-size: 24px;
            border: 3px solid #000;
            border-radius: 20px;
            padding: 4px 24px;
            box-shadow: 4px 4px 0px #000;
            display: inline-block;
            margin-top: 15px;
            letter-spacing: 1px;
        }

        /* Estilo de los Botones Streamlit */
        .stButton {
            display: flex;
            justify-content: center;
        }

        .stButton > button {
            width: 100% !important;
            max-width: 280px !important; /* Limitar ancho máximo para mejor aspecto centrado */
            background-color: #FED90F !important;
            color: #000000 !important;
            font-family: 'Bangers', cursive !important;
            font-size: 24px !important;
            letter-spacing: 1.5px !important;
            border: 4px solid #000000 !important;
            border-radius: 14px !important;
            padding: 10px 20px !important;
            box-shadow: 5px 5px 0px #000000 !important;
            transition: all 0.1s ease-in-out !important;
            cursor: pointer !important;
            margin: 0 auto !important;
        }

        .stButton > button:hover {
            background-color: #FFE54C !important;
            transform: translate(-2px, -2px) !important;
            box-shadow: 7px 7px 0px #000000 !important;
        }

        .stButton > button:active {
            transform: translate(3px, 3px) !important;
            box-shadow: 2px 2px 0px #000000 !important;
        }

        /* Botón Deshabilitado */
        .stButton > button:disabled {
            background-color: #CCCCCC !important;
            color: #666666 !important;
            border-color: #666666 !important;
            box-shadow: none !important;
            cursor: not-allowed !important;
            transform: none !important;
        }

        /* Tarjetas de Personajes */
        .simpson-card {
            background-color: #FED90F;
            border: 4px solid #000000;
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 25px;
            box-shadow: 7px 7px 0px #000000;
            text-align: center;
            font-family: 'Comic Neue', cursive;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .simpson-card:hover {
            transform: translateY(-6px);
            box-shadow: 9px 11px 0px #000000;
        }

        .simpson-name {
            font-family: 'Bangers', cursive;
            font-size: 28px;
            color: #FFFFFF;
            text-shadow: 2px 2px 0px #000, -1px -1px 0px #000, 1px -1px 0px #000, -1px 1px 0px #000;
            margin-top: 12px;
            margin-bottom: 6px;
            letter-spacing: 1px;
        }

        .simpson-badge {
            background-color: #FF6B6B;
            color: #FFF;
            border: 2px solid #000;
            border-radius: 10px;
            display: inline-block;
            padding: 2px 12px;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 8px;
            box-shadow: 2px 2px 0px #000;
        }

        .simpson-occ {
            color: #000;
            font-size: 15px;
            font-weight: 700;
            margin: 4px 0 0 0;
            background: rgba(255, 255, 255, 0.5);
            padding: 6px;
            border-radius: 8px;
            border: 1.5px solid #000;
        }

        .simpson-img-box {
            background-color: #FFFFFF;
            border: 3px solid #000000;
            border-radius: 12px;
            padding: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 210px;
            box-shadow: inset 0px 0px 8px rgba(0,0,0,0.15);
        }

        .simpson-img-box img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
    </style>
""", unsafe_allow_html=True)

# UI: Encabezado sin donas, más grande y centrado
st.markdown(f"""
    <div class="simpsons-header">
        <h1 class="simpsons-title">The Simpsons API</h1>
        <div class="page-badge">Página {st.session_state.page}</div>
    </div>
""", unsafe_allow_html=True)

st.write("") 

# Controles de navegación centrados
col_left, col_btn1, col_btn2, col_right = st.columns([2, 2, 2, 2])

with col_btn1:
    st.button("⬅️ Anterior", on_click=anterior, disabled=(st.session_state.page == 1))

with col_btn2:
    st.button("Siguiente ➡️", on_click=siguiente)

st.write("") 

# Galería de personajes
if personajes:
    columnas = st.columns(3)
    for i, p in enumerate(personajes):
        col = columnas[i % 3]
        img_url = f"https://cdn.thesimpsonsapi.com/500{p.get('portrait_path', '')}"
        nombre = p.get('name', 'Desconocido')
        edad = p.get('age', '?')
        ocupacion = p.get('occupation', "Sin Registro")

        with col:
            st.markdown(f"""
                <div class="simpson-card">
                    <div class="simpson-img-box">
                        <img src="{img_url}" alt="{nombre}">
                    </div>
                    <div class="simpson-name">{nombre}</div>
                    <div class="simpson-badge">Edad: {edad}</div>
                    <div class="simpson-occ">💼 {ocupacion}</div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.warning("No se encontraron personajes en esta página.")