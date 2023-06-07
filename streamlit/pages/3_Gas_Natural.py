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

st.title("Evolución del Precio del Gas Natural")

st.image(Image.open('pics\gasn.jpg'))

st.markdown(
"""
El precio del gas natural, al igual que otros hidrocarburos, ha experimentado un notable aumento en los últimos años.

A pesar de la destacada participación de fuentes de energía renovable, como el viento, agua y sol,
no son suficientes para cubrir toda la demanda eléctrica del país, 
Por lo tanto, es necesario recurrir a la producción de electricidad mediante el uso de gas, ya sea a través de ciclos combinados o cogeneración.

""")

st.write("El objetivo es ppredecir el precio de la eléctricidad para el día siguiente")

gasn = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\gasnatural_clean.csv')

gasn_pred = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\pred_gasnatural.csv')

gasn_pred = gasn_pred.drop(columns=['Unnamed: 0'])

gasn["Date"] = pd.to_datetime(gasn['Date'])
gasn.set_index("Date", inplace=True)
gasn["Date"] = gasn.index
gasn.index = pd.DatetimeIndex(gasn.index, dayfirst= True)

st.subheader('Evolución Precio Gas Natural')

st.line_chart(gasn["Close"])

st.markdown(
"""
Debido a la falta de reservas suficientes, España depende de la importación de energía de otros países, principalmente Estados Unidos, Argelia y Nigeria, en lugar de depender principalmente de Rusia como ocurre en otros países europeos. Aunque solo importamos un pequeño porcentaje gas de Rusia, si este país decide aumentar sus precios, se produce un incremento en los precios internacionales del gas, lo que afecta al costo en otros países.

Además, cuando los proveedores de gas aumentan los precios, el costo de producción de las centrales de ciclo combinado también se incrementa, lo que tiene un impacto directo en el precio del megavatio. Dado que el mercado mayorista sigue un modelo marginalista, el precio final de la electricidad por hora está vinculado al precio del combustible más costoso necesario para satisfacer la demanda prevista durante ese período. En este caso, el gas juega un papel fundamental en la determinación del precio del mercado eléctrico en la mayoría de los casos.
""")

st.title("Predicción del Precio del Gas Natural")

with st.expander("XGB Regressor"):
    st.image(Image.open('..\pics\predicciongasn.png'))

with st.expander("Métrica de evaluación"):
    st.info("RMSE: 0.1258")

with st.expander("Predicciones: "):
    st.dataframe(data=gasn_pred, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)