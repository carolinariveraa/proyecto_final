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

st.title("Predicción Precio Gas Natural")

st.write("El objetivo es ppredecir el precio de la eléctricidad para el día siguiente")

gasn = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\gasnatural_clean.csv')

gasn["Date"] = pd.to_datetime(gasn['Date'])
gasn.set_index("Date", inplace=True)
gasn["Date"] = gasn.index
gasn.index = pd.DatetimeIndex(gasn.index, dayfirst= True)

st.subheader('Evolución Precio Gas Natural')

st.line_chart(gasn["Close"])

