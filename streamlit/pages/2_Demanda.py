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
import seaborn as sns
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



st.title("Demanda energetica Gwh")

st.markdown(
    """
A continuación, se realiza un análisis detallado de la variable de demanda eléctrica. Se examinan los patrones de consumo a lo largo del tiempo, se identifican tendencias estacionales y diarias, y se analizan los factores que influyen en la demanda eléctrica. Además, se ofrecen predicciones futuras del valor de la demanda eléctrica para cada día.    """
)

st.subheader("Demanda de energía en el mercado Español")

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

st.subheader('Evolución de la Demanda')
st.line_chart(demanda_2022["Demanda"])

demanda_s2022 = demanda["2022"]

st.subheader('Meses con mayor demanda')
datos_mes = demanda_s2022.copy()
datos_mes = pd.DataFrame(datos_mes.groupby(datos_mes['Fecha'].dt.strftime('%B'))['Demanda'].sum())

datos_mes = datos_mes.sort_values(by="Demanda", ascending=False)

st.bar_chart(datos_mes.sort_values(by="Demanda", ascending=False))

st.subheader("Predicción (Gwh)")

with st.expander("ETS "):
    st.image(Image.open('..\pics\predemanda.png'))

with st.expander("Métrica de evaluación"):

        # Cajas independientes
    st.info("MAPE: 0.07048366455511575")
    st.success("MSE: 2792.8266611702916")
    st.warning("RMSE: 52.847201072244985")


