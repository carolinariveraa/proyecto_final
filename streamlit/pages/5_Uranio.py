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

set_bg_hack('pics/pet2.jpg')



st.title("Precio del Uranio")

st.markdown(
    """
Se investiga el mercado del uranio y su relación con la generación de energía nuclear. Se analizan los factores que afectan el precio del uranio, como la oferta y demanda mundial y las políticas internacionales. También se ofrecen predicciones futuras del valor del uranio para cada día.""")

with st.expander("El aumento del precio del Uranio se puede atribuir a varios factores"):

        # Cajas independientes
    st.info("Demanda creciente: A medida que más países buscan aumentar su capacidad de generación de energía nuclear o ampliar sus programas existentes, la demanda de uranio aumenta.")
    st.success("Restricciones de suministro: Algunos países productores de uranio han impuesto restricciones a la exportación o han reducido su producción, lo que ha llevado a una disminución en la disponibilidad del mineral en el mercado global.")
    st.warning("Especulación en el mercado: Los inversores y especuladores pueden anticipar un aumento en la demanda futura o una escasez de suministro y comprar uranio como una inversión a largo plazo, lo que puede elevar los precios.")
    st.info("Cambios en las políticas nucleares: Las decisiones políticas y regulatorias también pueden tener un impacto en los precios del uranio.")

uranio = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\uranio_clean.csv')
uranio_pred = pd.read_csv(r'C:\Users\river\Ironhack-data\proyecto_final\clean_data\uranio_pred.csv')

uranio["Date"] = pd.to_datetime(uranio['Date'])
uranio.set_index("Date", inplace=True)
uranio["Date"] = uranio.index
uranio.index = pd.DatetimeIndex(uranio.index, dayfirst= True)

st.subheader('Evolución')

st.line_chart(uranio["Close"])

st.subheader("Predicción")

with st.expander("Prophet"):
    st.image(Image.open('..\pics\preduranio.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.success("MAE: 0.28529821240702397")
    st.warning("MSE: 0.15712753227843093")
    st.info("RMSE: 0.39639315367250094")


with st.expander("Predicciones: "):
    st.dataframe(data=uranio_pred, width=None, height=None, use_container_width=False, hide_index=True, column_order=None, column_config=None)

