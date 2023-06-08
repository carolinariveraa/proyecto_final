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

st.title("Precio de las emisiones CO2")

st.markdown(
    """
Se examina el impacto del dióxido de carbono en el mercado eléctrico español. Se exploran las políticas y regulaciones relacionadas con las emisiones de CO2, así como su influencia en el mercado eléctrico. Además, se presentan predicciones futuras del valor del CO2 para cada día.""")

st.image(Image.open('pics/nuclear.jpeg'))

with st.expander("El aumento del precio de las emisiones de CO2 se puede atribuir a varios factores CAMBIAR"):

        # Cajas independientes
    st.info("Demanda creciente: A medida que más países buscan aumentar su capacidad de generación de energía nuclear o ampliar sus programas existentes, la demanda de uranio aumenta.")
    st.success("Restricciones de suministro: Algunos países productores de uranio han impuesto restricciones a la exportación o han reducido su producción, lo que ha llevado a una disminución en la disponibilidad del mineral en el mercado global.")
    st.warning("Especulación en el mercado: Los inversores y especuladores pueden anticipar un aumento en la demanda futura o una escasez de suministro y comprar uranio como una inversión a largo plazo, lo que puede elevar los precios.")
    st.info("Cambios en las políticas nucleares: Las decisiones políticas y regulatorias también pueden tener un impacto en los precios del uranio.")

co2 = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\co2_clean.csv')
co2_pred = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\co2_pred.csv')

co2["Date"] = pd.to_datetime(co2['Date'])
co2.set_index("Date", inplace=True)
co2["Date"] = co2.index
co2.index = pd.DatetimeIndex(co2.index, dayfirst= True)

st.subheader('Precio CO2')

st.line_chart(co2["CO2"])

st.title("Predicción del Precio de las emisiones de CO2")

with st.expander("XGB Boosting"):
    st.image(Image.open('..\pics\co2.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.success("RMSE: 1.7423092884529048")


with st.expander("Predicciones: "):
    st.dataframe(data=co2_pred, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)

