import streamlit as st
import pandas as pd
import numpy as np
pd.options.display.max_columns = None
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.metrics import mean_squared_error
from math import sqrt
import datetime
import re
import base64

#esto no funciona

st.set_page_config(
    page_title="Hola",
   
)

st.title("Predicción precio eléctricidad")

st.write("El objetivo es ppredecir el precio de la eléctricidad para el día siguiente")

dataset = pd.read_csv('data/dataset.csv')
dataset = dataset.drop(columns=['Unnamed: 0'])
dataset = dataset.drop(columns=['weekend'])
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

# Seleccionar el año, el mes y el día
selected_year = st.selectbox("Select year:", years)
selected_month = st.selectbox("Select month:", months)
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

#plotting

st.write("Evolución del precio de la electricidad")

euaspot = pd.read_csv('..\clean_data\euaspot.csv')

euaspot["date"] = pd.to_datetime(euaspot['date'])
euaspot.set_index("date", inplace=True)
euaspot["date"] = euaspot.index
euaspot.index = pd.DatetimeIndex(euaspot.index, dayfirst= True)

st.subheader('Evolución Precio Eléctricidad 2015-2023')

st.line_chart(euaspot["value"])