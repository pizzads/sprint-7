import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Vehículos Usados en EE. UU.')

# BOTÓN (acción puntual)
if st.button('Mostrar histograma de precios'):
    st.write('Distribución de los precios de los vehículos')
    fig = px.histogram(df, x='price', nbins=50, title='Distribución de Precios')
    st.plotly_chart(fig)

# CHECKBOXES (estado mantenido)
if st.checkbox('Mostrar relación entre precio y kilometraje'):
    fig2 = px.scatter(df, x='odometer', y='price',
                      title='Precio vs Kilometraje')
    st.plotly_chart(fig2)

if st.checkbox('Mostrar boxplot de precios por tipo de vehículo'):
    fig3 = px.box(df, x='type', y='price',
                  title='Precio por Tipo de Vehículo')
    st.plotly_chart(fig3)
