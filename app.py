import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Visualización de Datos de Vehículos')
start_button = st.button('Iniciar Visualización')

if start_button:
    st.plotly_chart(px.histogram(car_data, x="odometer"))
    st.write("Datos de Vehículos:")
