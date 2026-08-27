import streamlit as st

# Titulo del app web
st.title("Este es mi primer codigo de Streamlit")
st.header("Primer Vista de APP WEB")
st.subheader("Usando Rerun")

st.badge("New")
st.badge("Success", icon="🤖", color="green")

def sumar(a, b):
    return a + b

resultado = sumar(50,25)

st.write(resultado)

def mensaje(mimensaje):
    for a in range(10):
        st.text(mimensaje)

mensaje("Hola esto funciona")