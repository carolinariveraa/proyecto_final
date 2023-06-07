import streamlit as st
import pandas as pd
import numpy as np
pd.options.display.max_columns = None
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from PIL import Image
import seaborn as sns

# Establecer el tema y los estilos
st.markdown(
    """
    <style>
    body {
        color: #000000;
        background-color: #ffffff;
        font-family: serif;
    }

    .stTextInput, .stTextArea, .stNumberInput, .stSelectBox, .stColorPicker, .stCheckbox, .stRadio {
        background-color: #e0d7c7 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Mercado Eléctrico")

st.image(Image.open('pics\por.jpeg'))

with st.expander("Funcionamiento mercado Eléctrico Español"):
    st.markdown(""" 
    El precio diario de la electricidad se determina en el mercado mayorista, donde las centrales eléctricas ofertan la cantidad de energía que están dispuestas a suministrar y a qué precio. Este proceso establece las horas más caras y más baratas de electricidad para el día siguiente.

  >
  >  
    
Existen tres factores principales que influyen en el precio de la electricidad:

1. Meteorología: Las condiciones climáticas, como días ventosos, pueden aumentar la generación de electricidad eólica, lo que a su vez reduce el precio de la electricidad.

2. Picos de consumo: Los días de frío intenso, cuando se utiliza la calefacción, o los días de calor intenso, cuando se utiliza el aire acondicionado, pueden generar picos de consumo eléctrico, lo que puede llevar a un aumento en el precio de la electricidad.

3. Precio de las materias primas: El precio del gas, el petróleo y el carbón, que son utilizados en la generación de electricidad, también influyen en el costo de la electricidad. Si estos precios aumentan, es probable que se refleje en un aumento del precio de la electricidad.

Estos factores combinados determinan el precio diario de la electricidad y pueden variar en función de la oferta y la demanda, así como de las condiciones del mercado.
    
    """)


#plotting

euaspot = pd.read_csv('..\clean_data\euaspot.csv')

euaspot["date"] = pd.to_datetime(euaspot['date'])
euaspot.set_index("date", inplace=True)
euaspot["date"] = euaspot.index
euaspot.index = pd.DatetimeIndex(euaspot.index, dayfirst= True)

st.subheader('Evolución Precio Eléctricidad 2020-2023')



euaspot = euaspot.loc["2020":]


st.line_chart(euaspot["value"])


st.title("¿Por qué sube la luz en 2021 y 2022?")

st.write("Las energías renovables no son suficientes")


with st.expander("El COVID-19"):
    st.markdown("""Durante la pandemia, muchas restricciones a nivel global fueron implementadas. Como resultado, numerosos negocios tuvieron que cerrar debido a que las personas se quedaron en casa. En relación al sector energético, el consumo de gas disminuyó significativamente debido a que la demanda energética se redujo. Esto generó un exceso de oferta, lo cual no fue favorable para los productores, ya que redujo considerablemente los precios de la energía. En respuesta a esta situación, los proveedores de combustible optaron por disminuir su producción hasta que los confinamientos por la pandemia finalizaran.  
>    
>  
En 2021, la demanda de gas ha aumentado a medida que el mundo se recupera de la pandemia. Sin embargo, los proveedores de combustible no estaban preparados para esta rápida recuperación, lo que ha provocado una escasez de suministro de gas. Esta escasez de suministro, combinada con el aumento de la demanda, ha generado un incremento significativo en los precios de la energía a nivel global. Como resultado, estamos experimentando un aumento en nuestras facturas de luz mensuales debido a esta situación de escasez en el suministro de gas.""")

with st.expander("La guerra de Rusia y Ucrania"):
    st.write("Rusia es uno de los principales países exportadores de gas en Europa. Entre las sanciones económicas impuestas por la comunidad internacional a Moscú pasan por reducir su dependencia del gas y el petróleo ruso por lo que han provocado que el precio de la electricidad en el mercado mayorista ascienda notablemente.")


with st.expander("El precio del petróleo"):
    st.write("La fuerte recuperación económica posterior a la crisis ha provocado un aumento de los precios del petróleo")

with st.expander("El precio del gas natural"):
    st.write("El mercado marginalista establece que el proveedor con el precio más alto determina el precio final. Esto significa que el precio del gas natural tiene un impacto directo en el precio de la electricidad en todo el sistema. En el siguiente gráfico puedes ver que la gran subida de la electricidad en España se produce a partir de la segunda mitad de 2021 coincidiendo con el fuerte incremento del precio del gas en el mercado internacional. Tras un descenso moderado al inicio de 2022, el precio escala de nuevo al iniciarse el ataque ruso a Ucrania")


