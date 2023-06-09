import warnings
import streamlit as st
import pandas as pd
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime
import re
import base64
from PIL import Image
import base64



def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack('pet2.jpg')



st.title("Evolución del Precio del Gas Natural")

st.markdown(
    """
Se exploran los factores que influyen en el precio del gas natural y su relación con el mercado eléctrico. Se examina la oferta y demanda interna, la disponibilidad de suministro y los precios internacionales. También se analiza la relación entre el precio del gas natural y el precio de la electricidad, y se ofrecen predicciones futuras del valor del gas natural para cada día.
""")

st.image(Image.open('pics\gasn.jpg'))

st.markdown(
"""
El precio del gas natural, al igual que otros hidrocarburos, ha experimentado un notable aumento en los últimos años.

A pesar de la destacada participación de fuentes de energía renovable, como el viento, agua y sol,
no son suficientes para cubrir toda la demanda eléctrica del país, 
Por lo tanto, es necesario recurrir a la producción de electricidad mediante el uso de gas, ya sea a través de ciclos combinados o cogeneración.

""")


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

st.subheader("Predicción")

with st.expander("Correlación"):

        # Cajas independientes
    st.image(Image.open('pics/gasnvsprice.png'))

with st.expander("XGB Regressor"):
    st.image(Image.open('..\pics\predicciongasn.png'))

with st.expander("Métrica de evaluación"):
    st.info("RMSE: 0.1258")


