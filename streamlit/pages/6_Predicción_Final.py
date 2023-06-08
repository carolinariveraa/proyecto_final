
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

st.title("Predicción precio eléctricidad")

st.markdown(
    """
En esta página, se combinan todas las variables analizadas en las páginas anteriores. Se utiliza una red neuronal para realizar predicciones del precio de la electricidad en el mercado spot. Se integran las variables de demanda eléctrica, generación renovable, precio del gas natural, valor del CO2 y precio del uranio en un único dataframe. A partir de este dataframe, se realizan las predicciones diarias del precio de la electricidad utilizando la red neuronal entrenada.""")


st.image(Image.open('pics/pig.jpg'))


st.subheader("Importancia de las variables")

with st.expander("Precio del Gas Natural"):

        # Cajas independientes
    st.info("Muchas plantas de generación de energía utilizan gas natural como combustible. Si el precio del gas natural aumenta, se refleje en un aumento en el costo de generación de energía")

with st.expander("Precio de las emisiones de CO2"):

    st.info(" ")

with st.expander("Precio del Uranio"):

    st.info("Si el precio del Uranio aumenta, será más costoso la generación de energía nuclear lo que se traduce en una subida del precio de la energía")

with st.expander("Generación de Energías Renovables"):

    st.info("Estas fuentes de energía son menos dependientes de los combustibles fósiles y están sujetas a condiciones climáticas y ambientales. Por ejemplo, un aumento en la generación de energía eólica debido a condiciones climáticas favorables puede resultar en una mayor oferta de energía y, por lo tanto, en una reducción del precio de la energía en el mercado.")

with st.expander("Demanda de Energía"):

    st.info("Si la demanda de energía es alta y supera la capacidad de generación, es probable que esto conduzca a un aumento en el precio de la energía. Por el contrario, si la demanda es baja, es posible que se observe una disminución en el precio de la energía.")

st.subheader("Dataset final")

st.write("Para la predicción final del precio de la eléctricidad se ha empleado una red neuronal, MLP Regressor")

dataset = pd.read_csv('../clean_data/finalprecio.csv')
dataset = dataset.drop(columns=['Month'])
dataset = dataset.drop(columns=['Weekday'])
dataset = dataset.drop(columns=['Year'])

st.dataframe(data=dataset, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None)


dataset["Date"] = pd.to_datetime(dataset['Date'])
dataset.set_index("Date", inplace=True)
dataset["Date"] = dataset.index

#Adding a checkbox to be able to filter the dataframe
# Obtener la lista de años, meses y días únicos
years = dataset["Date"].dt.year.unique()
months = dataset["Date"].dt.month.unique()
days = dataset["Date"].dt.day.unique()

# Dividir el espacio horizontal en dos columnas
col1, col2, col3 = st.columns(3)

# Seleccionar el año, el mes y el día
with col1:
    selected_year = st.selectbox("Select year:", years)

with col2:
    selected_month = st.selectbox("Select month:", months)

with col3:
    selected_day = st.selectbox("Select day:", days)

# Filtrar los datos según la selección del usuario
filtered_data = dataset.loc[
    (dataset["Date"].dt.year == selected_year) &
    (dataset["Date"].dt.month == selected_month) &
    (dataset["Date"].dt.day == selected_day)
]

dataset = dataset.drop(columns=['Date'])

# Mostrar los datos filtrados
st.write(filtered_data)


