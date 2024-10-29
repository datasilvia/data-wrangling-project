import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Recomendador de Tarifas de Luz y Placas Solares")

# Añadir una imagen
st.image("image.jpg", use_column_width=True)

# Descripción de la aplicación
st.write("""
Esta aplicación recomienda tarifas de luz y placas solares basadas en los datos ingresados por el usuario.
""")

# Formulario para ingresar datos del usuario
st.sidebar.header("Ingrese sus datos")
consumo_mensual = st.sidebar.number_input("Consumo mensual (kWh)", min_value=0)
potencia_contratada = st.sidebar.number_input("Potencia contratada (kW)", min_value=0.0, step=0.1)
horas_sol = st.sidebar.number_input("Horas de sol al día", min_value=0.0, step=0.1)
superficie_placas = st.sidebar.number_input("Superficie disponible para placas (m²)", min_value=0.0, step=0.1)

# Datos de tarifas de ejemplo
tarifas = {
    "Tarifa 1": {"precio_energia": 0.15, "precio_potencia": 0.10},
    "Tarifa 2": {"precio_energia": 0.20, "precio_potencia": 0.08},
    "Tarifa 3": {"precio_energia": 0.18, "precio_potencia": 0.09},
}

# Datos de placas solares de ejemplo
placas = {
    "Placa 1": {"eficiencia": 0.18, "precio": 200},
    "Placa 2": {"eficiencia": 0.20, "precio": 250},
    "Placa 3": {"eficiencia": 0.22, "precio": 300},
}

# Función para recomendar tarifa
def recomendar_tarifa(consumo, potencia):
    mejor_tarifa = None
    menor_costo = float('inf')
    for tarifa, datos in tarifas.items():
        costo = consumo * datos["precio_energia"] + potencia * datos["precio_potencia"]
        if costo < menor_costo:
            menor_costo = costo
            mejor_tarifa = tarifa
    return mejor_tarifa, menor_costo

# Función para recomendar placas solares
def recomendar_placas(horas_sol, superficie):
    mejor_placa = None
    mayor_energia = 0
    for placa, datos in placas.items():
        energia_generada = horas_sol * superficie * datos["eficiencia"]
        if energia_generada > mayor_energia:
            mayor_energia = energia_generada
            mejor_placa = placa
    return mejor_placa, mayor_energia

# Mostrar recomendaciones
if st.sidebar.button("Recomendar"):
    tarifa, costo = recomendar_tarifa(consumo_mensual, potencia_contratada)
    placa, energia = recomendar_placas(horas_sol, superficie_placas)
    
    st.subheader("Recomendación de Tarifa de Luz")
    st.write(f"La mejor tarifa para usted es: **{tarifa}** con un costo mensual estimado de **{costo:.2f} €**.")
    
    st.subheader("Recomendación de Placas Solares")
    st.write(f"La mejor placa solar para usted es: **{placa}** que generará aproximadamente **{energia:.2f} kWh** al día.")

