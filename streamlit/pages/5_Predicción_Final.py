
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

st.title("Predicción precio eléctricidad")

st.title("Dataset final")

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