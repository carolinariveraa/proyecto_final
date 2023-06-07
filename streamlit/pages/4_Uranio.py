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

st.title("Predicción Demanda")

st.write("El objetivo es ppredecir el precio de la eléctricidad para el día siguiente")

uranio = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\uranio_clean.csv')
uranio_pred = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\uranio_pred.csv')

uranio["Date"] = pd.to_datetime(uranio['Date'])
uranio.set_index("Date", inplace=True)
uranio["Date"] = uranio.index
uranio.index = pd.DatetimeIndex(uranio.index, dayfirst= True)

st.subheader('Precio Uranio')

st.line_chart(uranio["Close"])

st.title("Predicción del Precio del Uranio")

with st.expander("Prophet"):
    st.image(Image.open('..\pics\preduranio.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.info("MAE: 0.28529821240702397")
    st.success("MSE: 0.15712753227843093")
    st.warning("RMSE: 0.39639315367250094")

with st.expander("Predicciones: "):
    st.dataframe(data=uranio_pred, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)
