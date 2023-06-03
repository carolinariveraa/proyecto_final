# proyecto_final
Predicción con Machine Learning del precio de la electricidad en España

# Resumen

El proyecto abarca la implementación de un modelo de aprendizaje automático o análisis de datos que se centra en modelar la serie de precios del mercado eléctrico. Este mercado mayorista presenta ciertas imperfecciones debido a restricciones técnicas y la existencia de mercados secundarios para regular los desajustes en la oferta y demanda de energía. El objetivo es predecir esta serie de precios con el fin de ofrecer mejores ofertas de precio fijo a los clientes y reducir los riesgos financieros asociados.

Para abordar este problema, se ha realizado la extracción de datos utilizando diferentes métodos y se ha llevado a cabo un proceso de limpieza y tratamiento de los mismos.

Una vez que los datos están preparados, se plantea resolver el problema utilizando modelos de aprendizaje automático. Se mencionan algunos de estos modelos utilizados, como Prophet, SARIMA, ARIMA y árboles de regresión. Estos modelos se emplean para predecir el precio de la electricidad y se utilizan como enfoques iniciales en el proyecto.

## Objetivo

Predecir el precio en 24 horas



# Metodología

### Datasets

Se han probado distintos modelos para predecir el precio de la electricidad

1. Escenario 1

Previamente a la elección de moldelos se realizan análisis de la estacionaridad de las variables como el test de dickey-fuller

Se compone de el precio del Gas Natural, la potencia generada de las energías renovables y el precio del Uranio. Por lo tanto se han hecho modelos de Machine Learning para predecir cada una de estas variables y con el conjunto obtener el precio de la electricidad para el día siguiente. La justificación de este método es que la energía en España se compone principalmente de las renovables, la nuclear y del gas natural. Por lo tanto estas variables tienen una alta correlación con el precio de la electricidad.

- Hidráulica, Eólica, Solar (Fotovoltaica y Térmica),Otras Renovables, Residuos Renovables, Gas Natural, Uranio, EUA Spot

### Precio de la eléctricidad en España 

![preciomwh](./pics/preciomwh.png)

### Predicción precio Gas Natural

Tas probar distintos modelos el que mejor se ajusta a la realidad es el XGB Boosting, se muestran los resultados para los próximos cinco días

![preciomwh](./pics/predicciongasn.png)

rmse: 0.1258590053674676

### Predicción precio Uranio

![prediccionuranio](./pics/prediccionuranio.png)

### Modelos testeados

1. Prophet
2. Arboles de decisión 
3. XGB Boosting
4. ARIMA, SARIMA

### Predicción energías renovables



![prediccionuranio](./pics/hidraulica.png)

![prediccionuranio](./pics/solar.png)

### Fuentes de información

Red Eléctrica de España (https://www.esios.ree.es/es)

Plataforma de inversión con los históricos (https://www.investing.com/)
- Gas Natural
- Derechos de emisión del CO2
- Indice Brent 
- Uranio