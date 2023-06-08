
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




st.title("Predicción precio eléctricidad")

st.markdown(
    """
En esta página, se combinan todas las variables analizadas en las páginas anteriores. Se utiliza una red neuronal para realizar predicciones del precio de la electricidad en el mercado spot. Se integran las variables de demanda eléctrica, generación renovable, precio del gas natural, valor del CO2 y precio del uranio en un único dataframe. A partir de este dataframe, se realizan las predicciones diarias del precio de la electricidad utilizando la red neuronal entrenada.""")


st.image(Image.open('pics/pig.jpg'))


st.subheader("Importancia de las variables")

with st.expander("Precio del Gas Natural"):

        # Cajas independientes
    st.info("Muchas plantas de generación de energía utilizan gas natural como combustible. Si el precio del gas natural aumenta, se refleje en un aumento en el costo de generación de energía")

with st.expander("Precio de las emisiones de CO2"):

    st.markdown("""
    En la actualidad, la producción de energía renovable no es suficiente para satisfacer la creciente demanda de electricidad. Esto implica que se siga dependiendo de la generación de energía en centrales de ciclo combinado, las cuales deben adquirir derechos de emisión de CO2 en el mercado de Régimen de Comercio de Derechos de Emisión para poder llevar a cabo su actividad y emitir a la atmósfera. Con los precios actuales de los derechos de emisión de CO2, esto se traduce en un incremento de aproximadamente 20 euros por megavatio hora (MWh) en el costo de producción de electricidad.

En resumen, mientras las centrales de ciclo combinado continúen siendo los principales actores en la generación eléctrica, el precio del CO2 seguirá teniendo un impacto significativo en el costo de la electricidad. Esta situación se mantendrá en el corto o medio plazo hasta que se logre cubrir la mayor parte de la demanda con fuentes de energía renovable y energía nuclear.
      """)

with st.expander("Precio del Uranio"):

    st.info("Si el precio del Uranio aumenta, será más costoso la generación de energía nuclear lo que se traduce en una subida del precio de la energía")

with st.expander("Generación de Energías Renovables"):

    st.info("Estas fuentes de energía son menos dependientes de los combustibles fósiles y están sujetas a condiciones climáticas y ambientales. Por ejemplo, un aumento en la generación de energía eólica debido a condiciones climáticas favorables puede resultar en una mayor oferta de energía y, por lo tanto, en una reducción del precio de la energía en el mercado.")

with st.expander("Demanda de Energía"):

    st.info("Si la demanda de energía es alta y supera la capacidad de generación, es probable que esto conduzca a un aumento en el precio de la energía. Por el contrario, si la demanda es baja, es posible que se observe una disminución en el precio de la energía.")

st.subheader("Dataframe final")

st.markdown("""
Para llevar a cabo la predicción final del precio de la electricidad, se ha utilizado una red neuronal conocida como MLP Regressor. Esta red neuronal, que significa Multi-Layer Perceptron Regressor, es un tipo de modelo de aprendizaje automático que se utiliza para resolver problemas de regresión, como la predicción de valores numéricos.

En este proyecto, se ha creado un dataframe que contiene diversas variables que se consideran relevantes para predecir el precio de la electricidad. 
Junto con estas variables, también se ha incluido en el dataframe el precio real de la electricidad en el mercado spot. Este precio se ha recopilado a partir de datos históricos y se utiliza como objetivo de la predicción.

Utilizando el dataframe con todas estas variables, se ha entrenado y ajustado la MLP Regressor para que pueda aprender los patrones y relaciones entre las variables y el precio de la electricidad. Una vez que el modelo está entrenado, se emplea para realizar predicciones futuras del precio de la electricidad en función de los valores de las variables.

Este enfoque basado en redes neuronales permite obtener predicciones más precisas y adaptativas, ya que la MLP Regressor es capaz de capturar patrones complejos y no lineales en los datos. De esta manera, esperamos proporcionar una herramienta útil para predecir el precio de la electricidad y ayudar a las empresas y consumidores a tomar decisiones informadas en el mercado eléctrico.

""")

dataset = pd.read_csv('../clean_data/finalprecio.csv')
dataset = dataset.drop(columns=['Month'])
dataset = dataset.drop(columns=['Weekday'])
dataset = dataset.drop(columns=['Year'])

st.dataframe(data=dataset, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None)


dataset["Date"] = pd.to_datetime(dataset['Date'])
dataset.set_index("Date", inplace=True)
dataset["Date"] = dataset.index

#Adding a checkbox to be able to filter the dataframe
# Obtener la lista de años, meses y días únicos
years = dataset["Date"].dt.year.unique()
months = dataset["Date"].dt.month.unique()
days = dataset["Date"].dt.day.unique()

# Dividir el espacio horizontal en dos columnas
col1, col2, col3 = st.columns(3)

# Seleccionar el año, el mes y el día
with col1:
    selected_year = st.selectbox("Select year:", years)

with col2:
    selected_month = st.selectbox("Select month:", months)

with col3:
    selected_day = st.selectbox("Select day:", days)

# Filtrar los datos según la selección del usuario
filtered_data = dataset.loc[
    (dataset["Date"].dt.year == selected_year) &
    (dataset["Date"].dt.month == selected_month) &
    (dataset["Date"].dt.day == selected_day)
]

dataset = dataset.drop(columns=['Date'])

# Mostrar los datos filtrados
st.write(filtered_data)

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.info("RMSE: 9.814")

