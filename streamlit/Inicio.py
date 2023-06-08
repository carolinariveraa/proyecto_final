import streamlit as st
import warnings
warnings.filterwarnings("ignore")
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






st.title("Predicción del Precio de la Eléctricidad")


st.markdown(
"""
¡Hola! Mi nombre es Carolina Rivera y te presento este proyecto de predicción del precio de la electricidad. En este proyecto, exploraremos las variables que afectan el mercado eléctrico español y utilizaremos diversas técnicas de Machine Learning y aprendizaje no supervisado para realizar predicciones.

El motivo por el cual decidí embarcarme en este proyecto es por mi interés en comprender el mercado eléctrico y su funcionamiento. Considero que el conocimiento de las variables que influyen en el precio de la electricidad es de gran utilidad tanto para las empresas del sector como para los consumidores, ya que les permite tomar decisiones informadas y optimizar sus estrategias.

A lo largo de este proyecto, analizaremos datos históricos del mercado eléctrico español y exploraremos diferentes modelos de Machine Learning, como regresión lineal, redes neuronales y random forest, para encontrar el modelo que mejor se ajuste a los datos y nos brinde las predicciones más precisas.

Espero que este proyecto sea de utilidad tanto para las empresas del sector eléctrico como para los consumidores, y que nos permita comprender mejor el comportamiento del mercado eléctrico y anticiparnos a sus fluctuaciones de precio.
"""
)

st.subheader("Distribución")

st.markdown(
"""
En las siguientes páginas, encontrarás información detallada sobre cada una de las variables clave que afectan el mercado eléctrico español, junto con un análisis exhaustivo y predicciones a futuro:

- **Página de Mercado Eléctrico:** Explora el precio de la electricidad en el mercado spot y el funcionamiento del mercado eléctrico español.

- **Página de Demanda de Energía:** Analiza la variable de demanda eléctrica, incluyendo patrones de consumo y predicciones futuras.

- **Página de Generación Renovable:** Estudia la contribución de las fuentes de energía renovable y ofrece predicciones de generación renovable.

- **Página de Gas Natural:** Examina los factores que influyen en el precio del gas natural y su relación con el mercado eléctrico, incluyendo predicciones futuras del valor del gas natural.

- **Página de CO2:** Explora el impacto del dióxido de carbono en el mercado eléctrico y presenta predicciones futuras del valor del CO2.

- **Página de Uranio:** Investiga el mercado del uranio y su relación con la generación de energía nuclear, incluyendo predicciones futuras del valor del uranio.

- **Página de Predicción Final:** Combina todas las variables analizadas en las páginas anteriores y realiza predicciones del precio de la electricidad utilizando una red neuronal.

En la página de Predicción Final, encontrarás el dataframe final con las predicciones del precio de la electricidad basadas en las variables seleccionadas. Este análisis integral te permitirá tener una visión completa y precisa del mercado eléctrico y las tendencias futuras del precio de la electricidad.
"""
)


