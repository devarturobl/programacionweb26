import streamlit as st
from supabase import Client, create_client
import pandas as pd

# url = https://myejqqmfrfynpuulmvey.supabase.co/rest/v1/
# key = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im15ZWpxcW1mcmZ5bnB1dWxtdmV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAxNDIwMTEsImV4cCI6MjEwNTcxODAxMX0.FXqSiqrp3Oi2Nj1FGtcE5oDZfVXjDOlvpMGsGbWY-gA

url: str = "https://myejqqmfrfynpuulmvey.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im15ZWpxcW1mcmZ5bnB1dWxtdmV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAxNDIwMTEsImV4cCI6MjEwNTcxODAxMX0.FXqSiqrp3Oi2Nj1FGtcE5oDZfVXjDOlvpMGsGbWY-gA"

supabase: Client = create_client(url, key)

# Codigo para testear la conexion a supabase
#try:
#    test = supabase.table("datos").select("*").execute()
#    print("Conexión exitosa a Supabase", test.data)
#except Exception as e:
#    print("Error al conectar con Supabase:", e)

st.title("Crud con Supabase y Streamlit")

def get_datos():
    try:
        response = supabase.table("datos").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"Error al conectar con Supabase: {e}")
        return []

st.subheader("Lista de Registros en Supabase")

datos = get_datos()

if datos:
    datosfilas = pd.DataFrame(datos)
    st.dataframe(
        datosfilas, 
        use_container_width=True,
        hide_index=True,
        column_order= ["id", "nombre", "detalle"],
        column_config={
            "id": st.column_config.NumberColumn(
                "ID",
                help="Identificador",
                width="small",
                format="%d"
            ),
            "nombre": st.column_config.TextColumn(
                "Tarea",
                help="Nombre de la Tarea",
                width="medium"
            ),
            "detalle": st.column_config.TextColumn(
                "Detalles",
                help="Detalle de la tarea",
                width="large"
            )
        }
    )





