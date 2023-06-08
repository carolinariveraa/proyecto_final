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
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('pics/pet2.jpg')

st.title("Precio de las emisiones CO2")

st.markdown(
    """
Se examina el impacto del dióxido de carbono en el mercado eléctrico español. Se exploran las políticas y regulaciones relacionadas con las emisiones de CO2, así como su influencia en el mercado eléctrico. Además, se presentan predicciones futuras del valor del CO2 para cada día.""")

st.image(Image.open('pics/nuclear.jpeg'))

st.subheader("¿Qué son los derechos de emisión?")

st.markdown("""
Los derechos de emisión de CO2 son instrumentos utilizados en el sistema de comercio de emisiones para controlar y reducir las emisiones de gases de efecto invernadero, especialmente el dióxido de carbono (CO2), que contribuye al cambio climático.

Cada derecho de emisión de CO2 representa el permiso para emitir una determinada cantidad de CO2 a la atmósfera. Estos derechos son emitidos por los gobiernos o autoridades competentes y se asignan a las empresas o instalaciones que son responsables de emisiones contaminantes.

 """)

st.subheader("¿Cómo se fija el precio del CO2?")

st.markdown("""
El precio de las emisiones de CO2 en el mercado se determina mediante el sistema de comercio de emisiones conocido como "Cap and Trade" (Límite y Comercio). En este sistema, el límite total de las emisiones de CO2 que la Unión Europea pone en circulación se reduce cada año con el fin de alcanzar los objetivos propuestos.

En el contexto del comercio de emisiones, el término "Cap" hace referencia al límite total de emisiones establecido, mientras que el término "Trade" indica que los derechos de emisión están sujetos a comercio. Cada derecho de emisión representa una tonelada de emisión de CO2.

Actualmente, el precio del CO2 en el mercado se sitúa alrededor de los 60€ por tonelada. Este precio fluctúa en función de la oferta y la demanda de los derechos de emisión, así como de las políticas y regulaciones relacionadas con la reducción de las emisiones de gases de efecto invernadero.

""")

with st.expander("Causas de la subida de precios de las emisiones de CO2"):

        # Cajas independientes
    st.markdown("""
    El precio de las emisiones de CO2 ha experimentado una evolución significativa en los últimos años debido a diferentes factores y medidas implementadas por la Unión Europea. A partir de 2014, la UE decidió reducir los derechos de emisión en circulación mediante medidas como el backloading, que consistió en el aplazamiento de parte de las subastas entre 2014 y 2016. Además, se implementó la Reserva de Estabilidad de Mercado para controlar los excedentes y establecer un mecanismo de control.

La entrada en operación de esta medida en 2019 impulsó el aumento en la cotización de los derechos de emisión, obligando a las empresas a reducir sus emisiones. Otros factores que influyeron en el precio fueron el Brexit, con la salida de Reino Unido del Régimen de Comercio de Emisiones de la UE, y la aprobación del incremento de la ambición de la UE, estableciendo un objetivo de reducción de emisiones del 55% para 2030.

Como resultado de estas medidas, el precio medio anual del CO2 aumentó de alrededor de 15 euros en 2018 a aproximadamente 25 euros en los años siguientes. Alcanzando actualmente alrededor de 86,60 €. Esta evolución muestra la creciente importancia y valoración de la reducción de emisiones en el mercado, impulsada por las políticas de la UE y las reformas previstas en el régimen de comercio basadas en los nuevos objetivos de reducción.
    """)

co2 = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\co2_clean.csv')
co2_pred = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\co2_pred.csv')

co2["Date"] = pd.to_datetime(co2['Date'])
co2.set_index("Date", inplace=True)
co2["Date"] = co2.index
co2.index = pd.DatetimeIndex(co2.index, dayfirst= True)

st.subheader('Evolución')

st.line_chart(co2["CO2"])

st.title("Predicción del Precio de las emisiones de CO2")

with st.expander("XGB Boosting"):
    st.image(Image.open('..\pics\co2.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.success("RMSE: 1.7423092884529048")


with st.expander("Predicciones"):
    st.dataframe(data=co2_pred, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)

