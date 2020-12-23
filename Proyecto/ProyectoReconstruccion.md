#Proyecto Servicio Social: **Software para la reconstrucción de Series de tiempo**.


El proyecto consiste en crear software que sirva como marco de prueba y herramienta para desarrollo de algoritmos de reconstrucción de series de tiempo. 

Este software servira para hacer validación de los diferentes modelos básados en aprendizaje automático.

El software estará compuesto de varias funciones para crear una base de datos con información de la consistencia la serie de tiempo.

## Objetivos Específicos


1. Crear una base de datos (tabla .csv) por cada serie de tiempo que contenga la ubicación del comienzo de las secuencias de datos faltantes así como su tamaño. Por ejemplo:

| ix_comienzo | tamaño | 
|-------------|--------|

2. Una función que genere un histograma para describir los datos faltantes.
3. Una base de datos (csv) que tenga definido 

| t  |  y  | set = {a, b, [c], missingData}  | dato faltante simulado |  Reconstrucción $\hat{y}$ | 
|----|-----|--------------------------------|-----------------|---------------------------|


Objetivos:

1. Diseñar una estructura de base de datos para:
	1. Organizar, las series de tiempo en conjuntos de entrenanamiento, prueba, y validación.
	2. Crear una manera de visualizar los datos faltantes de manera sencilla.
2. Crear una función que simule las fallas (huecos) para probar al menos un método de reconstrucción.
3. Programar un método sencillo de reconstrucción, optimizarlo con el conjunto de entrenamiento, probarlo con el conjunto de prueba, y finalmente reconstruir los datos faltantes.
4. Graficar datos reconstrucción vs datos reales


## Funciones propuestas

1. ixTable = generateMissingDataTableIndexes(Y)
2. trainingTable = generatePlaygroundTable(Y,[a,b,c,d])
3. saveMissingDataTableIndexes(ixTable,"nombre_ixTable.csv")
4. savePlaygroundTable(trainingTable, "nombre_playground.csv")
5. histograma = report(missingDataTable)  # generar histograma #[[holeSize_1,frec_1],[holeSize_2,frec_2]...[holeSize_n,frec_n]]
6. [h,size] = simulateFailure(histogramFail, histogramCorrect) #h = [true | false], tamaño de la secuencia hueco o no hueco. 