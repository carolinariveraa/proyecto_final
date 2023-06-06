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

st.title("Predicción Demanda")

st.write("El objetivo es ppredecir el precio de la eléctricidad para el día siguiente")

uranio = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\uranio_clean.csv')

uranio["Date"] = pd.to_datetime(uranio['Date'])
uranio.set_index("Date", inplace=True)
uranio["Date"] = uranio.index
uranio.index = pd.DatetimeIndex(uranio.index, dayfirst= True)

st.subheader('Precio Uranio')

st.line_chart(uranio["Close"])