import warnings
import streamlit as st
import pandas as pd
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.metrics import mean_squared_error
from math import sqrt
import datetime
import re
import base64
from PIL import Image

st.title("Generación de Energías Renovables")

renovables = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\renovables_clean.csv')
pred_renovables = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\pred_renovables.csv')

renovables = renovables.drop(columns=['Unnamed: 0'])

renovables["Fecha"] = pd.to_datetime(renovables['Fecha'])
renovables.set_index("Fecha", inplace=True)
renovables["Fecha"] = renovables.index
renovables.index = pd.DatetimeIndex(renovables.index, dayfirst= True)


# Filtrar los datos para el año 2022
renovables_2022 = renovables.loc[renovables.index.year == 2022]
renovables_2023 = renovables.loc[renovables.index.year == 2023]

# Calcular el porcentaje de cada fuente renovable
total_renovables2022 = renovables_2022.sum()
porcentaje_renovables_2022 = (total_renovables2022 / total_renovables2022.sum()) * 100

total_renovables2023 = renovables_2023.sum()
porcentaje_renovables_2023 = (total_renovables2023 / total_renovables2023.sum()) * 100

# Crear el gráfico de tarta para 2022
fig1, ax1 = plt.subplots()
wedges1, _, autotexts1 = ax1.pie(porcentaje_renovables_2022, autopct='%1.1f%%')
ax1.set_aspect('equal')  # Para que el gráfico sea circular
ax1.legend(wedges1, porcentaje_renovables_2022.index, loc="best")
plt.title('Generación de Energías Renovables 2022')

# Crear el gráfico de tarta para 2023
fig2, ax2 = plt.subplots()
wedges2, _, autotexts2 = ax2.pie(porcentaje_renovables_2023, autopct='%1.1f%%')
ax2.set_aspect('equal')  # Para que el gráfico sea circular
plt.title('Generación de Energías Renovables 2023')

# Configurar la grilla de dos columnas en Streamlit
col1, col2 = st.columns(2)

# Mostrar el gráfico de 2022 en la primera columna
with col1:
    st.pyplot(fig1)

# Mostrar el gráfico de 2023 en la segunda columna
with col2:
    st.pyplot(fig2)


st.title("Predicción de la Generación de Energía por Tecnologia")

st.image(Image.open('pics/renov.jpeg'))

with st.expander("Prophet"):
    st.image(Image.open('../pics/solar.png'))
    st.image(Image.open('../pics/hidraulica.png'))
        
with st.expander("Predicciones: "):
    st.dataframe(data=pred_renovables, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)


