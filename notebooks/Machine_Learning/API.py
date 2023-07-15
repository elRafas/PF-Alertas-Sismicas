import requests
import streamlit as st

url = "https://mlapi2.onrender.com/clasificar_sismo/7.2/6.8"

# Valores de magnitud e intensidad que deseas enviar
magnitud = 7.2
intensidad = 6.8

# Construir la URL con los valores proporcionados
url_con_valores = f"https://mlapi2.onrender.com/clasificar_sismo/{magnitud}/{intensidad}"

# Realizar la solicitud GET
response = requests.get(url_con_valores)

# Obtener la respuesta del servidor
respuesta = response.text

# Mostrar la respuesta obtenida
print(respuesta)