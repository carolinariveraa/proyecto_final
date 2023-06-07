# Mercado eléctrico español
Predicción con Machine Learning del precio de la electricidad en España

![preciomwh](./pics/por.jpeg)

# Resumen

En el mercado eléctrico español, los agentes intercambian energía para cada hora del día siguiente. Las ofertas de compra y venta de energía se utilizan para construir las curvas de oferta y demanda, y el precio y volumen de la energía intercambiada dependen de la intersección entre estas curvas. Una vez que se realiza la casación de las curvas, se establecen los compromisos de entrega de energía y se determina el precio para cada franja horaria. La forma y valor de estas curvas están influenciados por varios factores, como la climatología que afecta la disponibilidad de energías renovables, el precio de los combustibles fósiles y los derechos de emisión de CO2. Por otro lado, la curva de compra está determinada principalmente por la demanda de electricidad de las comercializadoras y los grandes consumidores industriales.

Una vez que los datos están preparados, se plantea resolver el problema utilizando modelos de aprendizaje automático. Se mencionan algunos de estos modelos utilizados, como Prophet, ETS,  SARIMA, ARIMA y árboles de regresión. Estos modelos se emplean para predecir el precio de la electricidad y se utilizan como enfoques iniciales en el proyecto.

## Objetivo

El objetivo principal del trabajo es conocer el precio de la electricidad para el día siguiente. 

# Metodología

### Dataset

Para conocer el precio de la electricidad se van a realizar predicciones previas sobre:

- Potencia generada de las energías renovables,
- Demanda, 
- Precio del uranio 
- Precio del Gas Natural

Por lo tanto se han hecho modelos de Machine Learning para predecir cada una de estas variables y con el conjunto obtener el precio de la electricidad para el día siguiente. La justificación de este método es que la energía en España se compone principalmente de las renovables, la nuclear y del gas natural. Por lo tanto estas variables tienen una alta correlación con el precio de la electricidad.


### Evolución precio de la eléctricidad en España 

![preciomwh](./pics/preciomwh.png)

<details>
<summary>Predicción Demanda</summary>

El modelo que mejor se ajusta a la demanda es ETS ya que tiene un periodo estacional de 7 días

![demanda](./pics/predemanda.png)

</details>

<details>
<summary>Predicción precio Gas Natural</summary>

Tas probar distintos modelos el que mejor se ajusta a la realidad es el XGB Boosting, se muestran los resultados para los próximos cinco días

![preciomwh](./pics/predicciongasn.png)

rmse: 0.1258590053674676
</details>

<details>
<summary>Predicción precio Uranio</summary>

![prediccionuranio](./pics/prediccionuranio.png)
</details>

<details>
<summary>Predicción energías renovables</summary>

El modelo que mejor se ajusta a la energía hidraulica y solar es Prophet 

![prediccionuranio](./pics/hidraulica.png)

![prediccionuranio](./pics/solar.png)
</details>


### Fuentes de información

* Red Eléctrica de España (https://www.esios.ree.es/es)
    - Precio de la eléctricidad
    - Potencia generada
    - Demanda


* Plataforma de inversión con los históricos (https://www.investing.com/)

    - Gas Natural
    - Derechos de emisión del CO2
    - Indice Brent 

* Datos climatologicos 

    - AEMET