import streamlit as st
import warnings
warnings.filterwarnings("ignore")
from PIL import Image


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
El objetivo de este proyecto es predecir el precio de la eléctricidad, para ello estudiaré las varibales que afectan el mercado eléctrico español y posteriormente se tratará de realizar una serie de predicciones mediante el uso de diversos modelos de Machine Learning y aprendizaje no suervisado.

"""
)

st.image(Image.open('pics\por.jpeg'))

