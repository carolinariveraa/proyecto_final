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

demanda = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\demanda.csv')

demanda["Fecha"] = pd.to_datetime(demanda['Fecha'])
demanda.set_index("Fecha", inplace=True)
demanda["Fecha"] = demanda.index
demanda.index = pd.DatetimeIndex(demanda.index, dayfirst= True)

st.subheader('Evolución Demanda')

st.line_chart(demanda["Demanda"])