​			 CENTRO DE INVESTIGACIÓN EN CIENCIAS DE INFORMACIÓN GEOESPACIAL

​																											SECRETARIA GENERAL

​																										PLANEACIÓN ESAPCIAL

​																														REPORTE No 1



Dr. Rodrigo Frías López

Responsable de Servicio Social 

Licenciatura en Tecnología

Centro de Física Aplicada y Tecnología Avanzada

P r e s e n t e.



Me permito informarle que el alumno **ARIEL CERÓN GONZÁLEZ** con número de cuenta **11000100-7**, de la Licenciatura en Tecnología que se imparte en el Campus UNAM-Juriquilla del Centro de Física Aplicada y Tecnología Avanzada, que realiza su Serivicio Social en esta Dependencia en el Programa: **Software para sistematizar validación de modelos de reconstrucción de Series de Tiempo con aplicación al estudio de las concentraciones de contaminantes PM 2.5**, con clave **2020-61/17-3022**, en el periodo comprendido del <u>17 - febrero</u> al  <u>17 - agosto</u> del <u>2020</u>, ha desarrollado la siguiente actividad en el 1 bimestre:



**Informe de la Actividad:**

## Actividad: Investigar como implementar la Validación Cruzada para reconstrucción de series de tiempo

**Abstract:** El estudio de series de tiempo es un area interdisciplinar donde interactúan diferentes áreas (pero no se limita a estas) como estadística, ciencias de la computación, sistemas dinámicos y teoría de la información. El estudio de series de tiempo tienen aplicación diversa en arás como economía, ciencias de la tierra, química atmosférica, optimización de aprovechamiento de recursos naturales renovables y no renovables como agua y viento. La principal utilidad del estudio de modelos de series de tiempo es la posibilidad de predecir con cierta precisión a la vez que se minimiza la incertidumbre de los valores de ciertas variables. Sin embargo, para poder estimar estos modelos de predicción, en especial los modelos estadísticos de la familia Box-Jenkins y Exponential Smoothing, se parte del supuesto que la serie de tiempo no contiene datos faltantes, datos atípicos, o erróneos. Este reporte revisa modelos de validación cruzada para modelos de predicción, y basado en estos, la propuesta de validación cruzada para medir la capacidad de reconstrucción de algún modelo. 

### Series de tiempo (terminar).

*Definición de serie de tiempo*

*Para que sirve el estudio de series de tiempo?*

*Problemas técnicos con la generación de series de tiempo:  (Mencionar que la tecnología que produce series de tiempo no es infalible a fallas, limitando el modelado para la predicción a solo un subconjunto de datos. Una condición deseable es tener la maxima información disponible y de calidad para ajustar modelos de prediccion.)*

### Modelos populares (terminar Traducir y complementar).

*There are at least two widely used (and complementary) approaches:*

*   *Estadisticos*
    *    *Exponential smoothing based models (Holt-Winters, 1960). The idea is to use weighted averages of past observations, with the decreasing weights exponentially as soon as the observations get older, and also they describe time series from the trend and seasonality point of view.*
    *   *Autoreggresive-Moving Average Based Models (Box-Jenkins, 1974), describing the dynamics with autocorrelations in the data.*
    *   *BATS (**B**ox-Cox transformation, **A**RMA errors, **T**rend and **S**easonal Components)) combines these models complementary. , published in 2011 by A. M. de Livera R. J. Hyndman and R. D. Snyder.*

*   Computacionales
    *   Redes neuronales.
    *   Vecinos cercanos.
    *   Redes bayesianas.

### Predicción (terminar basarse en la introducción del libro de Montgomery).

*Desde Página 1 de Montgomery et. al.*

*Nuestro modelo general de reconstrucción puede verse como una extensión del  propuesto en el libro de Montgomery Fig 1.12*

![foreceastingprocess_montgomery](imagenes/foreceastingprocess_montgomery.png)



### Limitantes del proceso de predicción (terminar).

*Mencionar que funciona siempre y cuando la calidad de los datos sea buena (no datos atípicos, no datos faltantes, datos calibrados).*

### Modelo de reconstrucción se relaciona con el de predicción (terminar).

*Describir el proceso de reconstrucción y como se conecta con el proceso de predicción*



![extension_reconst](imagenes/extension_reconst.jpg)



### Validación (terminar).

*Porque es importante validar el modelo?* 

*Como los datos se organizan en diferentes conjuntos: entrenamiento validacion y prueba, y para que?* (te pongo un ejemplo en esta sección)

[*ejemplo: Los modelos se entrenan con un conjunto de entrenamiento, y se mide su desempeño o capacidad de generalizacion con el conjunto de validación.*

*El conjunto de prueba se utiliza para que un tercero pruebe el modelo propuesto.* 

*Si la muestra de los datos son consitentes, entonces el error del modelo de prueba y validación deben ser parecidos.*]

#### Validación de modelos para datos independientes de contexto. (atemporales y no espaciales)(terminar)



**Validación cruzada *$k$-fold* **

[*(Modificar el ejemplo de validación de clasificación para convertirlo en un problema de predicción)*, usar referencia de wikipedia https://es.wikipedia.org/wiki/Validaci%C3%B3n_cruzada]

![Esquema_castellà](imagenes/Esquema_castella.jpg)

#### Validacion de modelos para predicción de datos temporales.(terminar)

*Leer la referncia https://robjhyndman.com/hyndsight/tscv/ y basado en eso escribir esta sección*

*Retomar la Propuesta de Hyndman. (Re-hacer la gráfica para no infringir derechos de autor, puede ser este ejemplo, y ademas simplificado, e.g., menos datos y unos cuantos renglones )*



![cv1-1](imagenes/cv1-1.png)

#### Validación de modelos para reconstrucción de datos temporales (terminar).

*Descripción de la propuesta con palabras*

*Esta figura no existe, hay que elaborarla y es importante porque es lo que proponemos*

![propuesta_validacion_cruzada_reconstr](imagenes/propuesta_validacion_cruzada_reconstr.png)



### Medidas del error (yo lo completo)

*Mean Squared Error: MSE*

*Mean Absolute Errors: MAE*

*Otras medidas del error:*

### Propuesta del algoritmo general de reconstrucción (terminar).

*por ejemplo:*

1.  *Organizar serie de tiempo en conjuntos de entrenamiento, validación y prueba.*
2.  *generar fallas aleatorias a la serie de tiempo*
3.  *Reconstruir datos faltantes con un modelo de reconstrucción.*
4.  *Medir el error de reconstrucción*

*Describir de manera general como queremos diseñar el software, puede ser textual, diagrama de bloques, UML, las funciones o clases*

### Conclusiones



### Referencias

1. TISSBERT: Reconstruccion de series de tiempo https://polipapers.upv.es/index.php/raet/article/view/9749/10323
2. What to Do about Missing Values in Time-Series Cross-Section Data. (James Honaker The Pennsylvania State University Gary King Harvard University) 2010
3. E. Castaño: Time Series Data Reconstruction: An Application to the Hourly Demand of Electricity. https://www.researchgate.net/publication/262722662_Time_Series_Data_Reconstruction_An_Application_to_the_Hourly_Demand_of_Electricity
4. R. Hyndman. Cross-validation for time series https://robjhyndman.com/hyndsight/tscv/
5.  A. M. de Livera R. J. Hyndman and R. D. Snyder. BATS
6. D. Montomery. et al. Time Series Analysis and Forecasting. Second Edition.
7. [https://es.wikipedia.org/wiki/Validaci%C3%B3n_cruzada](https://es.wikipedia.org/wiki/Validación_cruzada)



Sin otro particular por el momento, reciba un cordial saludo.



​														**A T E N T A M E N T E**

​							**Campus UNAM-Juriquilla, Qro a XX de XXXX de 2020**



​											_____________________________________________________________________________________________________________________