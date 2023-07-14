import requests
import tkinter as tk
from tkinter import messagebox

def obtener_respuesta():
    # Crear una ventana emergente
    ventana = tk.Tk()

    # Función para manejar el clic en el botón de enviar
    def enviar_valores():
        # Obtener los valores de magnitud e intensidad ingresados por el usuario
        magnitud = float(entry_magnitud.get())
        intensidad = float(entry_intensidad.get())

        # Construir la URL con los valores proporcionados
        url_con_valores = f"https://mlapi2.onrender.com/clasificar_sismo/{magnitud}/{intensidad}"

        # Realizar la solicitud GET
        response = requests.get(url_con_valores)

        # Obtener la respuesta del servidor
        respuesta = response.text

        # Mostrar la respuesta obtenida en una ventana emergente
        messagebox.showinfo("Respuesta", respuesta)

        # Cerrar la ventana después de mostrar la respuesta
        ventana.destroy()

    # Crear etiquetas y campos de entrada para los valores de magnitud e intensidad
    label_magnitud = tk.Label(ventana, text="Magnitud:", font=("Arial", 14))
    label_magnitud.pack()
    entry_magnitud = tk.Entry(ventana, font=("Arial", 14))
    entry_magnitud.pack()

    label_intensidad = tk.Label(ventana, text="Intensidad:", font=("Arial", 14))
    label_intensidad.pack()
    entry_intensidad = tk.Entry(ventana, font=("Arial", 14))
    entry_intensidad.pack()

    # Crear botón para enviar los valores
    boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_valores, font=("Arial", 14))
    boton_enviar.pack()

    # Configurar el tamaño de la ventana de preguntas
    ventana.geometry("500x400")

    # Ejecutar la ventana
    ventana.mainloop()

obtener_respuesta()
