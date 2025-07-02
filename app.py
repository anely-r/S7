import pandas as pd
import plotly.express as px
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Visualización de Datos de Vehículos')

# Instrucciones para el usuario
st.write("Selecciona una opción para visualizar los datos:")

# Botón para histograma
hist_button = st.button('Construir histograma del odómetro')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos')
    fig = px.histogram(car_data, x='odometer', nbins=30,
                       title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button(
    'Construir gráfico de dispersión precio vs. odómetro')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para precio vs odómetro')
    fig = px.scatter(car_data, x='odometer', y='price',
                     color='type', title='Precio vs. Kilometraje por tipo')
    st.plotly_chart(fig, use_container_width=True)
