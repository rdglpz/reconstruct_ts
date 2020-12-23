**COMPLEMENTO AL REPORTE**

 

**ABSTRACT.**

El estudio de series de tiempo es un área interdisciplinar donde interactúan diferentes áreas (pero no se limita a estas) como estadística, ciencias de la computación, sistemas dinámicos y teoría de la información. El estudio de series de tiempo tiene aplicación diversa en áreas como economía, ciencias de la tierra, química atmosférica, optimización de aprovechamiento de recursos naturales renovables y no renovables como agua y viento. La principal utilidad del estudio de modelos de series de tiempo es la posibilidad de predecir con cierta precisión a la vez que se minimiza la incertidumbre de los valores de ciertas variables. Sin embargo, para poder estimar estos modelos de predicción, en especial los modelos estadísticos de la familia Box-Jenkins y Exponential Smoothing, se parte del supuesto que la serie de tiempo no contiene datos faltantes, datos atípicos, o erróneos. Este reporte revisa modelos de validación cruzada para modelos de predicción, y basado en estos, la propuesta de validación cruzada para medir la capacidad de reconstrucción de algún modelo.



**INTRODUCCIÓN**

Una **serie de tiempo** es una secuencia de tiempo orientada o, una secuencia cronológica, de observaciones sobre una variable de interés  (Montgomery, Jennings, & Kulahci, 2015)

![Promedio](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\Promedio.png)

​                              Figura 1. Series de tiempo de las concentraciones de PM    2.5 en la estación MERCEDES desde 1986 hasta 2018.    

  

Las series de tiempo se pueden pensar como series de datos continuas, aunque en la practica se usan series de datos discretas, esto porque en la mayoría de los casos sólo podemos, o queremos, registrar de manera discreta. El registro de datos presenta en la práctica un conjunto de problemas como la calidad de los datos, la desaparición de información por errores técnicos o del sistema de registro, perdida del formato, entre otras.

Las series de tiempo son usada por muchas instituciones, tanto públicas como privadas, hacen uso de series de tiempo para la toma de decisiones o para la planeación de actividades, obteniendo pronósticos en función de la serie de tiempo. Por ello es importante conseguir datos completos de buena calidad, para poder obtener las mejores decisiones. (García, 2011)

La limpieza de datos es parte del proceso de pronóstico, la limpieza es el proceso mediante el cual se detectan errores potenciales, datos perdidos, valores inusuales u otras inconsistencias y corregirlos. Datos limpios pueden mejorar en gran medida el proceso de predicción.

El proceso de predicción puede resumirse en los siguientes pasos: 

1. **Definición del problema**

Cuestionarse la información que se requiere obtener de la serie de tiempo: horizonte de predicción, intervalo de predicción, nivel de precisión. 

​	2. **Colección de datos**

Obtener los datos históricos relevantes de la variable a predecir. Incluyendo información histórica de variables de predicción potenciales.

3. **Análisis de datos**

Es un paso preliminar para la selección del modelo de predicción. Graficar la serie de tiempo permite observar parámetros que tengan frecuencia, cantidad de datos, huecos y demás datos que puedan ser reconocidos de forma visual.

​	4. **Modelo de selección y ajuste**

En este paso se elige uno o más modelos de reconstrucción y se justa el modelo a los datos.

​	5. **Modelo de validación**

Se evalúan los datos que los modelos de predicción arrojaron para determinar el nivel de error que arroja cada modelo.

​	6. **Implementación del modelo desarrollado**

Una vez verificado, el modelo pasa a ser usado por el usuario final, con el fin de usar la información generada.

​	7. **Monitoreo del modelo de predicción**

Se debe tener un seguimiento sobre el modelo después de ser implementado para asegurarse que sigue funcionando satisfactoriamente. 

![proceso](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\proceso.png)



Existen al menos dos enfoques ampliamente utilizados los estadísticos y los computacionales. 

Los modelos estadísticos hacen uso de variables estadísticas para aproximar o estimar un valor, entre los modelos más usados se encuentran:

- **Exponential Smoothing Bases Models** (Modelos de Suavizado Exponencial).  Los modelos de suavizado remueven el ruido y las fluctuaciones de corto plazo de una serie de dejan sólo su movimiento de largo plazo funcionando como un filtro para obtener una "estimación" de la señal.

  La idea del suavizado exponencial es suavizar la serie original de la misma forma que se mueve su promedio y usa la serie suavizada para pronosticar valores futuros de la variable de interés. En el suavizado exponencial, queremos darle más peso a los valores más recientes de la serie, para tener mayor influencia en el pronóstico de valores futuros a comparación de las observaciones más distantes. (Ostertagova & Ostertag, 2011)

  El suavizado es una técnica popular para suavizar series de tiempo discretas por su simplicidad, eficiencia computaciones y su precisión.![sds](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\sds.png)

-  **Autoreggresive Moving Average Based Models** (Modelos de Media Móvil Autorregresiva). Un hecho observado es la relación del comportamiento pasado y el comportamiento futuro en muchos fenómenos temporales. El expresar una variable en función de su propio pasado es conocida como *autorregresión*. El modelo de media móvil autorregresiva está formado por dos partes, una parte autorregresiva y otra de media móvil.

  El modelo autorregresivo expresa el valor actual de una serie estacionaria en función de su propio pasado.

  El modelo de promedio móvil expresa la serie de tiempo en función del presente y pasado de una serie de ruido blanco con media cero y varianza finita.(García, 2011)

- **BATS** (**B**ox-Cox transformation, **A**RMA errors, **T**rend and **S**easonal Components). Es un modelo linear homoscedástico, incorporando no-linealidad mediante la integración de la transformación Box-Cox y una representación estacionaria ARMA con el fin de obtener cualquier autocorrelación in los residuos.(Naim, Mahara & Idrisi, 2018). El modelo BEATS es una generalización de los métodos tradicionales que permiten múltiples periodos temporales.

Los modelos computacionales aprovechan además de las variables estadísticas, el poder de computo actual para aproximar las predicciones siguiendo los modelos experimentales y conceptos teóricos, entre los modelos más conocidos tenemos:

- **Redes Neuronales**. Las redes neuronales son modelos matemáticos que intentan copiar el funcionamiento básico de una neurona para el tratamiento de información. La unidad básica de análisis es una neurona artificial que cuenta con elementos funcionales (entradas, salidas, funciones de activación, función de transformación). Al conjunto de neuronas se le conoce como redes neuronales y cada red se caracteriza por los resultados que arrojan, la arquitectura sobre la que trabajan, el número de capas, la función de activación, etc.

  Las redes neuronales son instrumentos muy usados en los sistemas de visión computacional, medicina, mecánica y demás áreas del conocimiento. Esto por la capacidad de extraer información útil y producir inferencias a partir de los datos disponibles gracias a su capacidad de aprendizaje (Bajo & Ballesteros, 2002)

  

  ![rn](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\rn.png)

  

- **Vecinos Cercanos**. El algoritmo de vecinos cercanos es uno de los algoritmos de clasificación más conocidos. En este algoritmos se usa un conjunto de datos clasificados con la etiqueta de entrenamiento, o train, para clasificar a los nuevos elementos. El algoritmo toma el nombre de k-NN (k- Nearest Neighbors) porque clasifica a cada nuevo elemento calculando la distancia entre todos los elementos del conjunto de entrenamiento. 

  El principal problema del algoritmo k-NN es encontrar el valor de k con el que obtengamos un mayor redimiento al clasificar, generalmente se utiliza una técnica conocida como validación cruzada. (Berástegui, 2018) 

  

  ![knn](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\knn.png)

- **Redes Bayesianas**. Las redes bayesianas modelan un fenómeno mediante un conjunto de variables y las relaciones de dependencia entre ellas. Dado este modelo, se puede hacer inferencia bayesiana; es decir, estimar la probabilidad posterior de las variables no conocidas, en base a las variables conocidas. Además, pueden dar información interesante en cuanto a cómo se relacionan las variables del dominio, las cuales pueden ser interpretadas en ocaciones como relaciones causa-efecto. (Sucar, 2006)

  

  ![red1](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\red1.gif)

Todos los modelos de predicción son funcionales siempre y cuando la calidad de los datos sea bueno, buenos datos puede ser entendido como datos que sean exactos (el valor que representa sea muy cercano al valor real), completitud (no hay datos perdidos o datos atípicos), consistencia (todos los datos tienen la misma estructura, formato y significado).  Por otro lado, si no se tiene datos confiables, puede hacer imposible la predicción o reflejar resultados fuera de la realidad. 

Como antes ya se menciono, un paso en el proceso de predicción es la limpieza de datos, pero de forma posterior, es necesario verificar la fiabilidad de los resultados obtenidos.

La **validación** de un modelo consiste en una evaluación estadística para determinar cómo es de probable que funcione en la aplicación prevista. Esto puede proporcionar una guía útil sobre cómo funcionará el modelo de pronóstico cuando esté expuesto a los nuevos datos y, puede ser un enfoque valioso para discriminar entre modelos de pronóstico competitivos.

La **validación cruzada** es una técnica utilizada para evaluar los resultados de un análisis estadístico y garantizar que son independientes de la partición entre datos de entrenamiento y prueba, es uno de los procedimientos más utilizados para la evaluación de modelos de clasificación y regresión. Consiste en repetir y calcular la media aritmética obtenida de las medias de evaluación sobre diferentes particiones. Se utiliza en entornos donde le objetivo principal es la predicción y se quiere estimar la precisión de un modelo que se llevará a cano a la práctica.

El método consiste en dividir en dos conjuntos complementarios los datos de muestra, realizar el análisis de un subconjunto (denominado datos de entrenamiento), y validad el análisis en el otro subconjunto (denominado datos de prueba), de forma que la función de aproximación sólo se ajusta con el conjunto de datos de entrenamiento y a partir de aquí calcula los valores de salida para el conjunto de datos de prueba. 

La evaluación puede depender en gran medida de cómo es la división entre datos de entrenamiento y de prueba, y por lo tanto puede ser significativamente en función de cómo se realice esta división.

La validación cruzada es una manera de predecir el ajuste de un modelo a un hipotético conjunto de datos de prueba cuando no disponemos del conjunto explícito de datos de prueba.

La intención de tener diferentes conjuntos es poder generalizar los resultados obtenidos con el modelo.

![Esquema_castellà](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\Esquema_castellà.jpg)



Un ejemplo de validación cruzada se presenta en [Hyndsight](https://robjhyndman.com/hyndsight/tscv), presenta una serie de datos de prueba, cada uno de los cuales consiste en una sola observación. El conjunto de entrenamiento correspondiente consiste únicamente en observaciones que ocurrieron antes de la observación que forma el conjunto de prueba.

La precisión de la aproximación es obtenida computando sobre los promedios del conjunto de prueba.

Hemos conocido modelos que permiten obtener predicciones en función de los datos pasados y, de la misma forma, validar los resultados obtenidos. El proceso de reconstrucción busca generar datos perdidos en la serie de tiempo.

Una solución a este problema es el uso de modelos de predicción para obtener datos que se aproximen a los datos perdidos. Esta tarea utiliza los mismos datos que las tareas de reconstrucción, pues se pueden tener datos registrados antes del error y después del error. 

Una modificación al procedimiento de predicción permite adaptar para ser un procedimiento de reconstrucción

![DIAGRAMA](D:\Users\dooph\Documents\VisualCode\Servicio\Proyecto\Figuras\DIAGRAMA.png)

### Medidas del error 

Un modelo matemático bien adecuado es aquel que al que un pequeño cambio en la entrada genera un pequeño cambio en la salida, esto es posible si se tiene en cuenta los errores propios de un modelo matemático y los errores que se generan a lo largo de cualquier proceso numérico.

El error se puede entender como la diferencia ente el valor obtenido y el valor real, este tipo de error es conocido como **error absoluto**. Se tiene además otros tipos de errores mejor definidos 

* **Error medio de la media cuadrática**. 
* **Error de las medias absolutas** 
* **Error medio** 

### Propuesta del algoritmo general de reconstrucción.

Construir una herramienta (software) en un lenguaje de programación robusto y popular para facilitar el desarrollo de algoritmos de reconstrucción de series de tiempo y, a la vez, hacer validación de los diferentes modelos. 

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

1. (García, 2011) García, A. M. (2011). *Análisis de series de tiempo*. Pontificia Universidad Javeriana.
2. (Montgomery, Jennings, & Kulahci, 2015) D. Montomery. et al. Time Series Analysis and Forecasting. Second Edition.
3. (Ostertagova & Ostertag, 2011) Ostertagová, E., & Ostertag, O. (2011, September). The simple exponential smoothing model.
4. (Berástegui, 2018) Berástegui Arbeloa, G. (2018). Implementación y comparación del algoritmo de los k vecinos más cercanos (k-NN) con valores locales en k.
5. (Sucar, 2006) Sucar, L. E. (2006). Redes bayesianas. \*BS Araujo, Aprendizaje Automático: conceptos básicos y avanzados\*, 77-100.
6. TISSBERT: Reconstruccion de series de tiempo https://polipapers.upv.es/index.php/raet/article/view/9749/10323
7. What to Do about Missing Values in Time-Series Cross-Section Data. (James Honaker The Pennsylvania State University Gary King Harvard University) 2010
8. E. Castaño: Time Series Data Reconstruction: An Application to the Hourly Demand of Electricity. https://www.researchgate.net/publication/262722662_Time_Series_Data_Reconstruction_An_Application_to_the_Hourly_Demand_of_Electricity
9. R. Hyndman. Cross-validation for time series https://robjhyndman.com/hyndsight/tscv/
10. A. M. de Livera R. J. Hyndman and R. D. Snyder. BATS
11. [https://es.wikipedia.org/wiki/Validaci%C3%B3n_cruzada](https://es.wikipedia.org/wiki/Validación_cruzada)
12. Naim, I., Mahara, T., & Idrisi, A. R. (2018). Effective short-term forecasting for daily time series with complex seasonal patterns. *Procedia computer science*, *132*, 1832-1841.
13. แ enz Bajo, N. S., & ม lvaro Ballesteros, M. (2002). Redes neuronales: concepto, aplicaciones y utilidad en medicina. *Atenci๓n Primaria*, *30*(2), 119-120.



