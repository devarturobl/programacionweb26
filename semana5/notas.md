# Unidad 2 - Base de datos SUPABASE
## Crear una cuenta en supabase
    Preferentemente con GITHUB

## Crear una organización
    Programacion Web

## Creamos un nuevo proyecto
![alt text](image.png)
![alt text](image-1.png)

## Crear Una Tabla
![alt text](image-2.png)
![alt text](image-3.png)

## Insertar 3 Registros
![alt text](image-4.png)
![alt text](image-5.png)

# Crear entorno virtual e instalaciones
python -m venv .venv
pip install streamlit
pip install supabase



# Supabase data
## URL importante solo se coloca hasta .co 
### incorrecto
https://xitmsuybpmskpjyaejvj.supabase.co/rest/v1/
### Correcto
https://xitmsuybpmskpjyaejvj.supabase.co/


## anon
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhpdG1zdXlicG1za3BqeWFlanZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY3NjA3NzAsImV4cCI6MjEwMjMzNjc3MH0.T6u_geduJhgOGtlTmxmawfopWBl6tj9GNi9KkpBkqy4

## install
pip install supabase

## Conexion
el codigo de conexion esta en el archivo app.py

# python-dotenv-1.2.2
Esto es para manejo de variables desde archivos .env mantiene seguridad a claves
pip install python-dotenv

# Creamos un archivo .env en entorno virtual
Aqui agregaremos las claves de supabase

# Codigo base primeras pruebas antes de optimizar
import os
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from supabase import Client, create_client

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Falta SUPABASE_URL o SUPABASE_KEY en el archivo .env")

supabase: Client = create_client(url, key)


def get_posts():
    try:
        response = supabase.table("post").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Error al conectar con Supabase: {e}")
        return []


def insert_post(title, content):
    try:
        data = {"title": title, "content": content}
        supabase.table("post").insert(data).execute()
        return True
    except Exception as e:
        st.error(f"Error al insertar datos en Supabase: {e}")
        return False


st.title("CRUD con Supabase y Streamlit")


# 1. Definición de la ventana modal (compatible con móviles)
@st.dialog("Confirmación")
def show_success_modal():
    st.success("✅ **¡Registro Exitoso!**")
    st.write("Los datos se han guardado correctamente en la base de datos.")

    if st.button("Aceptar", use_container_width=True, type="primary"):
        st.session_state.form_counter += 1
        st.session_state.show_modal = False
        st.rerun()


# 2. Inicializamos el estado
if "form_counter" not in st.session_state:
    st.session_state.form_counter = 0

if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

# Si la bandera está activa, abrimos el modal
if st.session_state.show_modal:
    show_success_modal()

# 3. Formulario principal
with st.form("insert_form", clear_on_submit=False):
    title = st.text_input(
        "Título", key=f"form_title_{st.session_state.form_counter}"
    )
    content = st.text_area(
        "Contenido", key=f"form_content_{st.session_state.form_counter}"
    )
    submitted = st.form_submit_button("Insertar")

    if submitted:
        # Validación de campos
        if not title.strip() or not content.strip():
            if not title.strip() and not content.strip():
                st.error("Faltan tanto el título como el contenido.")
            elif not title.strip():
                st.error("El campo 'Título' es obligatorio.")
            else:
                st.error("El campo 'Contenido' es obligatorio.")
        else:
            # 1. Se guardan los datos
            exito = insert_post(title, content)
            if exito:
                # 2. Activamos la bandera y recargamos para disparar el modal limpiamente
                st.session_state.show_modal = True
                st.rerun()

# 4. Listado de registros
st.subheader("📋 Registros en la base de datos")

posts = get_posts()

if posts:
    df = pd.DataFrame(posts)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_order=["id", "title", "content"],
        column_config={
            "id": st.column_config.NumberColumn(
                "ID",
                help="Identificador único del registro",
                width="small",
                format="%d",
            ),
            "title": st.column_config.TextColumn(
                "Título",
                help="Título de la publicación",
                width="medium",
            ),
            "content": st.column_config.TextColumn(
                "Contenido",
                help="Cuerpo de la publicación",
                width="large",
            ),
        },
    )

    st.caption(f"Total de registros: **{len(df)}**")
else:
    st.info("ℹ️ No hay registros en la base de datos todavía.")


# Optimizar codigo para que en tiempo real se refresquen los datos


