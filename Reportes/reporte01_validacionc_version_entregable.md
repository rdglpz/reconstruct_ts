# Reporte 1

## Validación Cruzada para reconstrucción de series de tiempo

**Abstract:** El estudio de series de tiempo es un área interdisciplinar donde interactúa (pero no se limita a) la estadística, ciencias de la computación, sistemas dinámicos y teoría de la información. El estudio de series de tiempo tienen aplicación diversa en áreas como economía, ciencias de la tierra, química atmosférica, optimización de aprovechamiento de recursos naturales renovables y no renovables como agua y viento. La principal utilidad del estudio de modelos de series de tiempo es la posibilidad de predecir con cierta precisión a la vez que se minimiza la incertidumbre de los valores de ciertas variables. Sin embargo, para poder estimar estos modelos de predicción, en especial los modelos estadísticos de la familia Box-Jenkins y Exponential Smoothing, se parte del supuesto que la serie de tiempo no contiene datos faltantes, datos atípicos, o erróneos. Este reporte revisa modelos de validación cruzada para modelos de predicción, y basado en estos, la propuesta de validación cruzada para medir la capacidad de reconstrucción de algún modelo. 

### Series de tiempo

Una serie de tiempo es una secuencia de tiempo orientada o una secuencia cronológica de observaciones sobre una variable de interés (Montgomery, Jennings, & Kulahci, 2015)![ejemploST](figuras/ejemploST.png)

Fig. 1 Series de tiempo de las concentraciones de PM 2.5 en la estación Mercedes desde 1985

Muchas instituciones públicas y privadas tienen almacenados series de tiempo que reflejan la evolución de alguna variable en específico, esto hace de las series de tiempo una de las principales fuentes de consulta para la toma de decisiones o para la planeación de diferentes actividades. 

Las series de tiempo pueden reflejar y hacer predicciones a corto, mediano y largo plazo; cada una con un conjunto de problemas propios de su escala. Un problema característico de todas resulta en la calidad de los datos, la desaparición de información, la perdida de formato y en ocasiones la nula existencia de información por errores en la forma de adquisición de la información. Lo anterior hace que la información disponible para la predicción no sea siempre de la mejor calidad y sea necesario una limpieza previa para mejorar los resultados. 

Aunque la mayor parte del tiempo y la mayoría de la gente presupone que un pronóstico es sólo un número, la realidad es que se pueden obtener un conjunto de herramientas numéricas más poderosas que un solo número, como puede ser un intervalo de predicción, un punto estimado, errores de estimación, entre otras herramientas estadísticas. 

Un pronóstico es una predicción de algún evento o eventos futuros. El pronóstico es un problema importante que se presenta en una variedad de campos tanto cientificos, gubernamentales e industriales. Muchos de estos problemas involucran el uso de series de tiempo. La importancia en la predicción de futuros eventos radica en su participación sobre la toma de decisiones en procesos y planeaciones.

 Los modelos cuantitativos usados para predecir hacen uso de los patrones presentes en los datos para expresar una relación estadística entre valores anteriores y actuales de la variable y así mostrar patrones de la variable en el futuro.

El proceso de predicción toma los siguientes pasos:

1.  Definición del problema
2.  Colección de datos
3.  Análisis de datos
4.  Modelo de selección y ajuste
5.  Modelo de validación
6.  Implementación del modelo desarrollado
7.  Monitoreo del modelo de predicción.

![DIAGRAMA](figuras\DIAGRAMA.png)

La recolección de datos, como se ha mencionado, es importante para un buen análisis. Recolectar datos significa, obtener datos históricos relevantes de la variable que será reconstruida. Sin embargo durante este paso, se pueden identificar problemas en los datos recolectados, como la perdida de información o formato, haciendo necesario trabajar con series de tiempo incompletas. 

Es importante recordar que la base del trabajo se encuentra en la serie de datos que se puedan obtener para análisis, por ello se busca trabajar con datos que cumplan con exactitud (que su valor medido sea muy próximo al valor real), completitud (que no haya datos perdidos o atípicos), consistencia (que todos los datos tengan la misma forma de representar los valores). El contar con buenos datos es importante para el proceso de predicción, pues la falta de datos, un mal registro o la nula contingencia de los datos puede hacer imposible la predicción o reflejar resultados fuera de la realidad.

Para contar con buenos datos, se emplea la limpieza de los datos mediante el cual se detectan errores potenciales, datos perdidos, valores inusuales u otras inconsistencias, buscando corregirlos. Datos limpios pueden mejorar en gran medida el proceso de pronóstico.

Cuando se tienen un conjunto de datos completos, la necesidad de obtener nuevos valores en función de los que ya se tienen, es lo que encamina a los diferentes profesionales del área a desarrollar métodos de predicción que nos adelante en el futuro. Por desgracia, los modelos de predicción funcionan únicamente (o mejor dicho funcionan mejor) cuando se tiene una serie de datos completa, exacta y consistente. Cosa que , como se ha descrito, no ocurre muy amenudeo.  Sin embargo si se considera un pequeño conjunto de datos y se les considera completos, exactos y concisos, entonces será posible predecir datos futuros en función de esos datos.

![ST](figuras\ST.png)

Un modelo de predicción puede ser adaptado para ser usado como modelo de reconstrucción y con ello obtener una serie de datos completa que permita realizar predicciones mejores.    

Existen al manos dos enfoques ampliamente usados los estadísticos y los computacionales:

 Los modelos estadísticos hacen uso de variables estadísticas y modelos de regresión para aproximar o estimar un valor, entre los modelos más usados se encuentran:

* Modelos basados en suavizado exponencial (Exponential smoothing).  (Holt-Winters, 1960). La idea es usar promedios ponderados de observaciones pasadas, con pesos decrecientes exponencialmente tan pronto como las observaciones envejezcan, y también describen series de tiempo desde el punto de vista de tendencia y estacionalidad. La idea del suavizado exponencial es suavizar la serie original de la forma en que se mueve promedio hace y usar la serie suavizada para pronosticar valores futuros de la variable de interés. Sin embargo, en el suavizado exponencial, queremos permitir los valores más recientes. de la serie para tener mayor influencia en el pronóstico de valores futuros que los más distantes observaciones  (Bajo & Ballesteros, 2002)

  El alisado es probablemente la clase de procedimientos ampliamente utilizados para alisar series de tiempo discretas para pronosticar el futuro inmediato. Esta popularidad se puede atribuir a su simplicidad, su eficiencia computacional, la facilidad de ajustar su capacidad de respuesta a los cambios en el proceso que se pronostica, y su precisión razonable.
*   **Los modelos autoregresivos de medias moviles ARIMA** (Box-Jenkins, 1970), Describe los patrones de la serie de tiempo utilizando las correlaciones temporales de la serie de tiempo, y los errores del pasado.

*   **BATS (Box-Cox transformation, ARMA errors, Trend and Seasonal Components)** Es un modelo que combina los modelos anteriores además de incluir ciertas transformaciones para estabilizar los datos. (LIVERA, 11) 

Computacionales
*   **Redes neuronales.** Funciones de regresión inspiradas en el comportamiento de las neuronas biológicas. Son modelos de neuronas artificiales capaces de capturar patrones muy complejos. Tienen aplicaciones en problemas de clasificación y regresión.
*   **Vecinos cercanos**. Es una técnica de clasificación y predicción el cual explota la evidencia empírica para resolver problemas de clasificación y regresión. Esta técnica es muy poderosa pero depende de la disponibilidad de gran cantidad de datos. El algoritmo k-NN es uno de los algoritmos de clasificación más conocidos. Con este algoritmo usaremos un conjunto de ejemplos ya clasificados a los que llamaremos conjunto de entrenamiento o train para clasificar los nuevos ejemplos El algoritmo se llama así k-NN (k-Nearest Neighbors) porque clasifica cada nuevo ejemplo calculando la distancia de ese ejemplo con todos los del conjunto de train. El principal problema del algoritmo k-NN es encontrar el valor de k con el que optimice los resultados.
*   **Redes Bayesianas o de creencia:**  Son redes de relaciones probabilistas, la cual un dado vector de características de entrada, se calcula la probabilidad de que una variable dependiente presente un valor. Se representan con grafos no dirigidos, donde los nodos representan un conjunto de variables aleatorias. También se puede decir que las redes bayesianas modelan un fenómeno mediante un conjunto de variables y las relaciones de dependencia entre ellas. Dado este modelo, se puede hacer inferencia bayesiana; es decir, estimar la probabilidad posterior de las variables no conocidas, en base a las variables conocidas. Además, pueden dar información interesante en cuanto a cmo se relacionan las variables del dominio, las cuales pueden ser interpretadas en ocasiones como relaciones de causa–efecto (Naim, 2018).

### Validación

La **validación** es importante para medir la capacidad de generalización del modelo. La validación de un modelo consiste en una evaluación estadística para esto es importante organizar antes los datos en diferentes conjuntos  mutuamente excluyentes como entrenamiento validación y prueba.

La **validación cruzada** es una técnica utilizada para evaluar los resultados de un análisis estadístico y garantizar que son independientes de la partición entre datos de entrenamiento y prueba, es uno de los procedimientos más utilizados para la evaluación de modelos de clasificación y regresión. El método consiste en repetir y calcular la media aritmética obtenida de las medias de evaluación sobre diferentes particiones. Se utiliza en entornos donde le objetivo principal es la predicción y se quiere estimar la precisión de un modelo que se llevará a cano a la práctica. (Wikipedia, Validación Cruzada)

El método consiste en dividir en dos conjuntos complementarios los datos de muestra, realizar el análisis de un subconjunto (denominado datos de entrenamiento), y validad el análisis en el otro subconjunto (denominado datos de prueba), de forma que la función de aproximación sólo se ajusta con el conjunto de datos de entrenamiento y a partir de aquí calcula los valores de salida para el conjunto de datos de prueba. 

Con el conjunto de entrenamiento, se ajusta o entrena un modelo de acuerdo a los datos. Con el conjunto de validación se mide el error del modelo entrenado anteriormente y con el conjunto de prueba se da la posibilidad que para que un tercero pruebe el modelo propuesto. Si la muestra de los datos son consistentes, entonces el error del modelo de prueba y validación deben ser parecidos.

![Esquema_castellà](figuras\Esquema_castellà.jpg) Figura tomada de (Wikipedia, Validación Cruzada)

#### Validación de modelos para reconstrucción de datos temporales 

Sobre una serie de tiempo, se genera un nuevo renglón que asigne huecos falsos, sobre esta serie generada se aplica el modelo de predicción de datos, una vez implementado el modelo se hace una comparativa entre el valor observado y el valor medido, conociendo la calidad de predicción sobre los datos.

![DIAGRAMA2](figuras\DIAGRAMA2.png)

### Medidas del error para la evaluación del desempeño de modelos de predicción

La medición del error, consiste en determinar con alguna métrica que tan diferente es valor real $y_i$ comparado con un estimado $\hat{y}_i$ generado por algún modelo de regresión. 

Los modelos de regresión son modelos generales los cuales incluyen los modelos de predicción, reconstrucción, clasificación entre otros.  

Para esto, existen varias medidas que pueden ser utilizadas para la evaluación de un modelo

 En este apartado se reportan algunas métricas populares utilizadas para medir el error de las regresiones tomadas de Douglas et al. que son calculadas a partir de los residuales

$$e_i=y_i-\hat{y}_i$$

Error promedio

$$EP = \frac{1}{n}\sum_{i=1}^n e_i$$.

Este error estima el valor esperado del error el cual tiene una esperanza estadística cero en caso que las estimaciones no estén sesgadas.

Desviación media absoluta 

$$DMA = \frac{1}{n}\sum_{i=1}^n|e_i|$$

Error Promedio de sumas al cuadrado.

$$PSC =  \frac{1}{n}\sum_{i=1}^{n} (e_i)^2$$

$DMA$ y $PSC$ son dos medidas que miden la variabilidad de los errores de regresión. Se busca que la variabilidad sea la menor.

Promedio de los porcentajes absolutos de error

$$MAPE = \frac{1}{n}\sum_{i=1}^n|\frac{y_t-\hat{y}_t}{y_t}|$$

Es una medida sin magnitud que mide la variabiliad relativa en porcentaje al valor real. El problema con esta métrica es que $y_t$ no puede ser cero ya que produce una indeterminación. Otra desventaja es que dependiendo del valor de denominador, la diferencia en el numerador se magnifica o reduce y esto a veces no es deseable.

### Propuesta del algoritmo general de reconstrucción.

1. Construir una herramienta (software) en un lenguaje de programación robusto y popular para facilitar el desarrollo de algoritmos de reconstrucción de series de tiempo y, a la vez, hacer validación de los diferentes modelos. 

   La herramienta contendrá funciones que permitan visualizar y ordenar la información de entrada, en general se busca que el algoritmo pueda ejecutar las siguientes actividades.

   1. Lectura de los datos junto con la temporalidad asociada
   2. Organización de la información y asignación de un conjunto (S) entre *entrenamiento, validación y prueba* 
   3. Visualización de la serie de tiempo
     * Cantidad de datos
     * Relación entre datos numéricos y datos faltantes
     * Histograma de los datos
    4. Generar fallas aleatorias a la serie de tiempo
    5. Generar datos faltantes para cierto conjunto y con un modelo de reconstrucción específico
    6. Medición del error en la construcción

   ### Conclusiones

   Una serie de tiempo es una secuencia ordenada de observaciones de una variable en particular, estas son utilizadas para generar predicciones en el tiempo y con ello tomar decisiones o hacer planeaciones. Las series de tiempo, por desgracia, presentan en muchas ocasiones una falta de datos, presencia de datos atípicos o algún otro error que impide generar predicciones de calidad.

   El proceso de predicción intenta solucionar este problema limpiando los datos antes de aplicar algún modelo a los datos. El proceso de limpieza involucra la detección de datos atípicos y datos faltantes y su ajuste para contar con la mayor cantidad de datos útiles. 

   Por otro lado, un modelo de predicción, promete facilitar predicciones en el futuro con datos del pasado. 

   Ahora se busca, mediante el desarrollo de una herramienta (software), lograr visualizar, reconstruir y verificar los datos de una serie de tiempo usando modelos de predicción.





### Referencias

1. (García, A.M. 2011) . *Análisis de series de tiempo*. Pontificia Universidad Javeriana.
2. (Montgomery, Jennings, & Kulahci, 2015) D. Montomery. et al. Time Series Analysis and Forecasting. Second Edition.
3. (Ostertagova & Ostertag, 2011) Ostertagová, E., & Ostertag, O. (2011, September). The simple exponential smoothing model.
4. (Berástegui, 2018) Berástegui Arbeloa, G. (2018). Implementación y comparación del algoritmo de los k vecinos más cercanos (k-NN) con valores locales en k.
5. (Sucar, 2006) Sucar, L. E. (2006). Redes bayesianas. \*BS Araujo, Aprendizaje Automático: conceptos básicos y avanzados\*, 77-100.
6. (TISSEBERT) TISSBERT: Reconstruccion de series de tiempo https://polipapers.upv.es/index.php/raet/article/view/9749/10323
7. What to Do about Missing Values in Time-Series Cross-Section Data. (James Honaker The Pennsylvania State University Gary King Harvard University) 2010
8. E. Castaño: Time Series Data Reconstruction: An Application to the Hourly Demand of Electricity. https://www.researchgate.net/publication/262722662_Time_Series_Data_Reconstruction_An_Application_to_the_Hourly_Demand_of_Electricity
9. (Hyndman, 2016)R. Hyndman. Cross-validation for time series https://robjhyndman.com/hyndsight/tscv/
10. (LIVERA, 11) A. M. de Livera R. J. Hyndman and R. D. Snyder. BATS, 2011https://www.academia.edu/2996051/Forecasting_time_series_with_complex_seasonal
11. (Wikipedia, Validación Cruzada) [Wikipedia, Validación cruzada](https://es.wikipedia.org/wiki/Validación_cruzada)
12. (Naim, 2018) Naim, I., Mahara, T., & Idrisi, A. R. (2018). Effective short-term forecasting for daily time series with complex seasonal patterns. *Procedia computer science*, *132*, 1832-1841.
13. (Bajo & Ballesteros, 2002) N. Saenz Bajo, A. Ballesteros  (2002). Redes neuronales: concepto, aplicaciones y utilidad en medicina. *Atenci๓n Primaria*, *30*(2), 119-120. https://www.elsevier.es/es-revista-atencion-primaria-27-pdf-13033737
14. (Box-Jenkins, 1970) Box, G.E.P., and Jenkins, G., (1970) *Time Series Analysis, Forecasting and Control,* Holden- Day, San Francisco.
