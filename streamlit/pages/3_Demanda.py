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

st.title("Demanda energetica Gwh")

st.image(Image.open('pics/men.jpg'))

st.markdown("""
La predicción de la demanda en el mercado eléctrico español es una herramienta importante para planificar y gestionar eficientemente la generación y distribución de energía eléctrica.

La predicción de la demanda eléctrica permite a los operadores del mercado tomar decisiones informadas sobre la producción y distribución de energía, optimizando la capacidad de generación, planificando el mantenimiento de infraestructuras y evitando situaciones de sobrecarga o escasez de suministro. También es útil para los consumidores, ya que les permite ajustar su consumo de acuerdo con las previsiones y aprovechar los periodos de menor demanda para reducir costos.
""")

demanda = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\demanda.csv')

demanda["Fecha"] = pd.to_datetime(demanda['Fecha'])
demanda.set_index("Fecha", inplace=True)
demanda["Fecha"] = demanda.index
demanda.index = pd.DatetimeIndex(demanda.index, dayfirst= True)

# Filtrar los datos a partir de 2022
demanda_2022 = demanda["2022":]

st.subheader('Evolución Demanda')
st.line_chart(demanda_2022["Demanda"])

st.title("Predicción de la Demanda (Gwh)")

with st.expander("ETS "):
    st.image(Image.open('..\pics\predemanda.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.info("MAPE: 0.07048366455511575")
    st.success("MSE: 2792.8266611702916")
    st.warning("RMSE: 52.847201072244985")


