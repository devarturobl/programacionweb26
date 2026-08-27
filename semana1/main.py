import streamlit as st

# Titulo del app web
st.title("Este es mi primer codigo de Streamlit")
st.header("Primer Vista de APP WEB")
st.subheader("Consulta el repositorio: https://github.com/devarturobl/programacionweb26")

st.badge("New")
st.badge("Success", icon="🤖", color="green")

def sumar(a, b):
    resultado = int(a) + int(b)
    return st.write(resultado)



def mensaje(mimensaje):
    for a in range(10):
        st.text(mimensaje)

st.header("Usando Input Widgets")
st.subheader("Botones")

if st.button("Saludar"):
    mensaje("Hola Clase")

dato1 = st.text_input("Introduce el numero 1")
dato2 = st.text_input("Introduce el nuemero 2")

if st.button("Sumar"):
    sumar(dato1,dato2)
