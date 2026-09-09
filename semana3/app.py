import requests
import streamlit as st
import base64

# Funcion para poner una imagen de background
def set_background(image_file):
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

# Llamar la función con la ruta de tu archivo
set_background("assets/background.jpg")


# Configutar pagina
st.set_page_config(page_title="The Simpsom APi", layout="wide")

# Estilos
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@700&display=swap');

        /* Título principal con estilo Simpson */
        .simpsons-title {
            font-family: 'Bangers', cursive;
            color: #FED41D; /* Amarillo Simpson */
            font-size: 50px;
            letter-spacing: 2px;
            -webkit-text-stroke: 2px #000000; /* Borde negro característico */
            text-shadow: 3px 3px 0px #000000;
            margin-bottom: 0px;
        }

        /*Estilo para las card*/
        .simpson-card {
            background-color: #FED90F;
            border: 4px solid #000;
            border-radius: 18px;
            padding: 16px;
            margin-bottom: 24px;
            box-shadow: 6px 6px 0px #000;
            text-align: center;
            font-family: 'Comic Neue', cursive;
            transition: transform 0.15s ease-in-out;
        }

        .simpson-card:hover {
            transform: translateY(-4px);
        }

        .simpson-name {
            font-family: 'Bangers', cursive;
            font-size: 26px;
            color: #fff;
            text-shadow: 2px 2px 0px #000, -1px -1px 0px #000;
            margin-top: 10px;
            margin-bottom: 6px;
            letter-spacing: 1px;
        }

        .simpson-badge {
            background-color: #70D1FE;
            color: #000;
            border: 2px solid #000;
            border-radius: 10px;
            display: inline-block;
            padding: 2px 10px;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 6px;
        }

        .simpson-occ {
            color: #111;
            font-size: 14px;
            font-weight: bold;
            margin: 4px 0 0 0;
        }

        .simpson-img-box {
            background-color: #FFF;
            border: 3px solid #000;
            border-radius: 12px;
            padding: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
        }

        .simpson-img-box img {
            max-height: 100%;
            max-width: 100%;
            object-fit: contain;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="simpsons-title">The Simpsom API Personajes</div>', unsafe_allow_html=True)

response = requests.get("https://thesimpsonsapi.com/api/characters")
data = response.json()
personajes = data.get("results", [])

columnas = st.columns(3)

for i, p in enumerate(personajes):
    col = columnas[i % 3]
    img_url = f"https://cdn.thesimpsonsapi.com/500{p.get('portrait_path', '')}"
    nombre = p.get('name', 'Desconocido')
    edad = f"{p.get('age', '?')} años"
    ocupacion = p.get('occupation', "Sin Registro")

    with col:
        st.markdown(f"""
            <div class="simpson-card">
                <div class="simpson-img-box">
                    <img src="{img_url}" alt="{nombre}">
                </div>
                <div class="simpson-name">{nombre}</div>
                <div class="simpson-badge>{edad}</div>
                <div class="simpson-occ>{ocupacion}</div>
            </div>
        """, unsafe_allow_html=True)