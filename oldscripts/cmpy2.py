##################################
#   Ariel Ceron Gonzalez
#   Servicio Social
#   Queretaro, 2019
#
################################

import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 
import os   
import math as mt 
from numpy import linalg as LA
from datetime import datetime
import random
from sortedcontainers import SortedList
from lorenz import generateLorenz

##############Path################
path = os.getcwd()
os.chdir(path)
pathFig = path+'/Figuras/'
pathCsv = path+'/CSVfiles/'


###############Funciones###############
def toStr(value:int)->str:
    """Realiza una transformación sobre un valor numérico.
    
    Devuelve un carácter perteneciente al conjunto S = ['E','P','V'], en función de un número incluido en el conjunto N= [0,1,2] con la siguiente definición:

    Sea s en S, un carácter del conjunto S y n en N, un número en el conjunto N

        f(n) = E si n = 0,
               P si n = 1,
               V si n = 2
    
    Parameters
    ----------
    value : int
        Valor numérico a transformar
    
    Returns
    -------
    str
        Carácter asociado al número

    Example
    -------
    >>> import cmpy2 as cp
    >>> n = 0
    >>> s = cp.toStr(n)
    >>> print("f({}) = {}".format(n,s))
    f(0) = E
    """    
  
    if value == 0:
        return('E')
    elif value == 1:
        return('P')
    elif value == 2:
        return('V')

def creaMascara(h:int,tau:int,m:int)->list:
    """Devuelve una lista binaria (0,1) siguiendo una frecuencia tau para una cantidad m de elementos verdaderos.
    
    Devuelve una lista binaria, de ceros y unos, en el centro del arreglo se coloca una lista de ceros de tamaño h y a los extremos del vector se coloca una lista binaria de tamaño n, que cumple la relación

        n = 2(m) - 1

    La lista devuelta es de tamaño 2n + h
    
    Parameters
    ----------
    h : int
        Cantidad de datos centrales
    tau : int
        -----------------------
    m : int
        -----------------------
    
    Returns
    -------
    list
        Lista binaria de tamaño 2n + h
    """       
    i = j = 0                       #Contadores
    tmp = list()                    #Lista auxiliar
    while(j != m):                  #Verifica que la cantidad de altos contados sea diferente al requerido
        if i%tau == 0:              #Cada múltiplo de tau
            tmp.append(1)           #Añade un alto
            j+=1                    #Cuenta la cantidad de altos
        else:
            tmp.append(0)           #Añade un bajo
        i+=1                        #Avanza al infinito
    vH = [0 for k in range(h)]      #Construye el vector central
    return([tmp+vH+tmp,len(tmp)])

def distancias(objeto,f,g,S,h,m,tau,k):
    """ Pasos para crear la función:
        1) Obtener la lista de indices de los huecos
        2) Obtener las variables necesarias
        4) Iterar sobre todos los datos para comparar las distancias
        3) Obtener el vector que auxilia al hueco
        5) Obtener el valor que se le va a dar al hueco
        6) Devolver la lista de datos
        """

    #Obtener las variables necesarias
    mascara = creaMascara(h,tau,m)
    datos = np.asarray(objeto.df['x_i'])
    huecos = np.asarray(objeto.df[g[0]])
    #print("Huecos",huecos)
    indicesPositivos = np.where(np.asarray(mascara[0]) > 0)
    n = objeto.len
    Si = np.asarray(objeto.df['S'])
    
    #contenedores
    distancias = SortedList()
    suma = 0
    auxL = [0 for i in range(n)]
    

    #Obtener la lista de indices
    indicesHuecos = np.asarray(objeto.contar2(huecos,'h'))
    #print("Todos los huecos", indicesHuecos)
    idx = np.where(indicesHuecos[:,1] == h)
    #print("Inidce de huecos de tamaño h", idx)
    indicesHuecos = list(indicesHuecos[idx,0].flat) 
    #print("Huecos finales",indicesHuecos)
    
    #iterar sobre los datos y los huecos
    for hueco in indicesHuecos:
        #print("Cambio hueco")
        for indice in range(mascara[1],n - mascara[1] - h):
            #Filtro para omitir mismo indice del hueco
            if indice != hueco:
                v = Si[indice - mascara[1]:indice + mascara[1] + h] == S
                #Filtro para procesar solo datos pertenecientes a S*
                if v[indicesPositivos].all():
                    v1 = datos[indice - mascara[1]:indice + mascara[1] + h]
                    v2 = datos[hueco - mascara[1]:hueco + mascara[1] + h]
                    aux = np.isnan(v1*v2)
                    #print("aux",aux)
                    #print("Indices",indicesPositivos)
                    #print("If",aux[indicesPositivos])
                    #print("Hueco",huecos[indice:indice + h])
                    #Filtro para omitir nan
                    if not aux[indicesPositivos].any():
                        if not np.isnan(huecos[indice:indice + h]).any():
                            distancias.add([f(datos[indice - mascara[1]:indice + mascara[1] + h][indicesPositivos],datos[hueco - mascara[1]: hueco + h + mascara[1]][indicesPositivos]),indice])
        if distancias == []:
            #print("Sin datos")
            pass
        else:
            for dato in range(h):
                auxL[hueco + dato] = datos[distancias[0][1]+dato]
            distancias.clear()
    prueba.añadirCol("h{}m{}t{}k{}".format(h,m,tau,k),auxL)
    return([auxL,indicesHuecos])
    
def metricaEu(p1:list, p2:list) -> float:
    """Devuelve la distancia euclidiana entre dos puntos p1,p2 siguiendo la ecuación 
        dist(vec(p1) - vec(p2)) = sqrt((p11 - p21)**2 + (p12 - p22)**2 + ... + (p1n - p2n)**2)
    """
    if len(p1+p2) > len(p1):
        suma = []
        aux = 0
        for i in range(len(p1)):
            aux = p1[i] - p2[i]
            aux = aux**2
            suma.append(aux)
        resultado = 0
        for i in range(len(suma)):
            resultado += suma[i]
        return(np.sqrt(resultado))
    else:
        return(LA.norm(p1-p2))
                
def vecinosCercanos(objeto:object,nameCol:str,h:int,m:int,tau:int,k:int,base:str='x_i',S:str = 'E'):      
    """reconstruye los huecos de tamaño definido usando distancias y k primeros elementos

    Parameters
    ----------
    objeto : object
        Hace uso del objeto Reconstruir para usar algunos metodos implementados
    nameCol : str
        Nombre de la columna donde se encuentran los huecos
    h : int
        Valor del hueco
    m : int
        Valor de la cantidad de unos
    tau : int
        Frecuencia *NO*
    k : int
        Vecinos
    S : str, optional
        Conjunto con el que se va a trabajar, by default 'E'
    """    
    #Variables

    mascara = np.asarray(creaMascara(h,tau,m)) #Obtenemos mascara

    #Filtrado de las datos originales
    data1 = objeto.verificaDatos('x_i',S) #Primer filtro de datos, conjunto elegido

    #Filtrado de las datos a trabajar
    data2 = objeto.verificaDatos(nameCol,S)
    indicesHuecos = np.asarray(objeto.contar2(data2,'h')) #Obtenemos indices
    n = int(np.round((len(mascara) - h)/2)) #Tamaño del vector mascara, auxconteo de 
    idx = np.where(indicesHuecos[:,1]== h) #Segundo filtro de datos, tamaño de hueco
    indicesHuecos = list(indicesHuecos[idx,0].flat) #Indices de los huecos que nos interesan

    #Almacenamos los valores encontrados de forma ordenada
    sl = SortedList()

    
    recList = np.zeros(objeto.len)
    indices = np.where(np.asarray(mascara) == 1)[0]

    #Operación
    for elemento in indicesHuecos:                      #Avanzo en los huecos de tamaño 1
        v1 = data1[int(elemento-n):int(elemento+n+h)].reset_index(drop=True)   #Obtengo el primer vector a comparar
        #print(v1)
        modulo = 0       
        for i in range(n,(len(data1)-(h+n))):            #Avanza sobre los datos, dejando espacio para que el vector "entre" y "salga" sin salir del vector de datos
            v2 = data1[i-n:i+n+h].reset_index(drop=True)
            if objeto.validaIndices(v2,indices):        
               #Verifica que el vector que almacena el primer vector a comparar cumpla con las condiciones necesarias y que además no se compare consímismo                   
                V = v2.loc[indices] - v1.loc[indices]
                V = V**2
                V = np.sum(V)                           #Obtenemos el cuadrado de la diferencia entre dos valores
                sl.add((V,i))                           #Agregamos el valor y el indice del elemento 
        k = np.round(np.sqrt(len(sl))).astype(int)      #Obtenemos la cantidad cantidad de "vecinos" cercanos
        for j in range(k):
            print(sl[j])
            #modulo += data1[sl[j][1]]                      #Buscamos los valores reales asociados a los indices de los vecinos cercanos
        #modulo = modulo/k                                  #Obtenemos el promedio, suponemos que todos los datos deben ser muy parecidos
        #recList[elemento] = modulo                #En la lista de ceros, colocamos los valores modificados
        #aux = objeto.df['x_i'].copy()
        #aux[elemento]= modulo
    #objeto.añadirCol("R{}h{}m{}t".format(h,m,tau),recList)                    #Agregamos la lista a los datos
    #return(aux) 


####Funciones Rodrigo
def generateRandom(cummDist: list) -> int:
    '''
    Genera una variable aleatoria entre [1,len(cummDist)]
    
    Parameters:
    -----------
    
    cummDist: list
        Valid Cummulative Distribution
        
    Returns:
    -------
        
    ts: int
        random integer between [1,len(cummDist)]
        
    >>> np.add(1, 2)
    3
    
    '''
    s = np.random.uniform()
    treshold = s>np.array(cummDist)
    ts = np.sum(treshold)
    return ts

def simulateFailures(n: int, PD_1: list, PD_2: list) -> list:
    '''
    Esta funcion simula fallas en la captura de datos.
    
    
    Parameters:
    -----------
    
    n : int
        Length of the time series
        
    PD_1: list
        Cummulative distribution for failures (holes).
        
    PD_2: list
        Cummulative distribution for continuum data.
    
    
    Returns:
    -------
    
    h : list
        sequence of simmulated failures
        
    
    Example:
    --------

    >>> n = 5
    >>> f1 = [5,5]
    >>> f2 = [5,5]
    >>> H = simulateFailures(n,f1,f2)
    >>> H
    [0.0, 0.0, 1.0, 0.0, 1.0]
    
    
    
    '''
    # Funcion sin nombre de distribucion acumulada normalizada 
    
    f = lambda x:  list(np.cumsum(x/np.sum(x)))
    
    #Generacion de acumulados para cada distribucion
    
    PD_1 = f(PD_1)
    PD_2 = f(PD_2)
    h = list()
    
    while len(h) < n:
        
        # generamos secuencia de datos contiguos (no fallas), de tamaño aleatorio
        
        ts = generateRandom(PD_1)
        ones = np.ones(ts)
        h.extend(ones)
        
        
        
        if len(h) < n:
            
            # generamos secuencia de datos faltantes (fallas), de tamaño aleatorio
            
            ts = generateRandom(PD_2)
            zeros = np.zeros(ts)
            h.extend(zeros)
    
    return h[:n]
#######

class Reconstruir(object):
    """Reconstruir y estudiar series de tiempo.

    El estudio de series de tiempo es un área interdisciplinar donde interactúan diferentes áreas (pero no se limita a estas) como estadística, ciencias de la computación, sistemas dinámicos y teoría de la información. El estudio de series de tiempo tienen aplicación diversa en áreas como economía, ciencias de la tierra, química atmosférica, optimización de aprovechamiento de recursos naturales renovables y no renovables como agua y viento. La principal utilidad del estudio de modelos de series de tiempo es la posibilidad de predecir con cierta precisión a la vez que se minimiza la incertidumbre de los valores de ciertas variables. Sin embargo, para poder estimar estos modelos de predicción, en especial los modelos estadísticos de la familia Box-Jenkins y Exponential Smoothing, se parte del supuesto que la serie de tiempo no contiene datos faltantes, datos atípicos, o erróneos. Este reporte revisa modelos de validación cruzada para modelos de predicción, y basado en estos, la propuesta de validación cruzada para medir la capacidad de reconstrucción de algún modelo.

    Attributes
    ----------
    name : str
        El nombre de los datos a tratar
    df : padas.DataFrame
        Variable que almcena un DataFrame de los datos y su tratamiento
    len : int
        Cantidad de elementos en una columna del df
    nCol : int
        Cantidad de columnas del df


    Methods
    -------
    leer(self, data:list, date:list, name:str="default", vec: list = [60,20,20])
    """
    

    def __init__(self, data:list, date:list, name:str="default", vec: list = [0.6,0.2,0.2]):        
        """        
        Parameters
        ----------
        data : list
            Lista de datos numéricos a tratar
        date : list
            Lista de asocia a cada dato, un tiempo representativo para los datos
        name : str, optional
            Nombre representativo de los datos, by default "default"
        vec : list, optional
            Porcentaje de distribución en el conjunto de entrenamiento, prueba y verificación, by default [60,25,15]

        Example
        -------
        >>> import cmpy2 as cp
        >>> import numpy as np
        >>> lista_datos = [0,1,2,np.nan,3]
        >>> lista_fechas = ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04', '2017-10-05']
        >>> r = cp.Reconstruir(lista_datos,lista_fechas,"Prueba")   
        Datos exportados
        """        
        
        if len(data) == len(date):
            self.name = name    #Asignamos un nombre a los datos
            self.len = len(data)    #Tamaño de datos
            self.ncol = 0       #Número de columnas existentes en el archivo
            self.creaDF(data,date,vec)
            print("Datos importados")
        else:
            print("Datos no importados\n.La cantidad de datos y de fechas deben ser las mismas.\n") 

    def creaDF(self,data:list,date:list,vec:list):
        """Inicia la estructura principal del objeto.
        
        Apoyado de los datos de entrada, se crean las primeras tres columnas del objeto DataFrame con el que va a funcionar el objeto Reconstruir.
        
        Parameters
        ----------
        data : list
            Lista de datos numéricos a tratar
        date : list
            Lista de asocia a cada dato, un tiempo representativo para los datos
        vec : list
            Porcentaje de distribución en el conjunto de entrenamiento, prueba y verificación
        """              
        self.df = pd.DataFrame()
        self.añadirCol('date',pd.to_datetime(date),False)   #pd.to_datetime(date)
        self.añadirCol('x_i',data,False)
        self.añadirCol('S',self.vecS(vec),False)

    def añadirCol(self,name:str,data:list,flag:bool = True):
        """ Agrega una coluna al DataFrame.

        Agrega una columna de nombre name con los datos data.
        """        
        if flag:
            name = name + str(self.ncol)
            
        self.df[name] = data
        print("Datos agregados")
        self.ncol += 1    

    def vecS(self,vec:list)->list:
        """Devuelve una lista dividida en tres grupos.
        
        Dado un vector de porcentaje (vec) se crea una lista del tamaño del objeto, separada en tres grupos según el porcentaje, a saber ['E','P','V']
        
        Parameters
        ----------
        vec : list
            Lista de porcentajes para cada grupo, la suma de los elementos debe dar 1.
        
        Returns
        -------
        list
            Lista segmentada

        Example
        -------
        >>> v = [0.4,0.2,0.4]
        >>> vp = r.vecS(v)
        >>> vp
        ['E', 'E', 'P', 'V', 'V']

        """               
        if sum(vec) == 1:
            aux = 0         #Define el rango para generar el arreglo
            n = self.len
            v = np.ceil(n*np.asarray(vec))
            #Crea los vectores según el porcentaje
            l0 = [toStr(0) for i in range(v[0].astype(int))]
            l1 = [toStr(1) for i in range(v[1].astype(int))]
            l2 = [toStr(2) for i in range(v[2].astype(int))]
            aux = l0 + l1 + l2
            return(aux[:self.len])
        else:
            print("Valores no reconocidos")
            self.vecS([0.6,0.25,0.15])

    def describe(self, nameCol:str = "x_i"):
        """Representa gráficamante la proporción de los datos.
        
        Imprime tres gráficos:
            1) Gráfico de pastel entre la relación de datos y huecos.
            2) Frecuencia de los conjuntos de datos
            3) Frecuencia en los conjuntos de huecos
        
        Parameters
        ----------
        nameCol : str, optional
            Nombre de la columna a representar, by default "x_i"
        
        Example
        -------
        >>> r.describe()
        """        

        if nameCol in self.df.columns:
            labels = ["Datos", "Huecos"]    #Etiqueta de datos
            nD = self.contar(nameCol,'d')[1]
            nH = self.contar(nameCol,'h')[1]
            sizes = [nD,nH]   #Obtenemos la cantidad de datos y de huecos
            colors = ["green","red"]    #Asignamos color a los gráficos

            print("{} elementos en {}. \n {} datos y {} huecos".format(self.len,self.name,nD,nH))
            plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%')
            plt.axis('equal')
            plt.savefig(pathFig+"pie_{}.png".format(self.name))
            plt.show()

            self.hist(nameCol,'d')      #Imprimimos el histograma de huecos
            self.hist(nameCol,'h')      #Imprimimos el histograma de datos
        else:
            print("No hay columnas con el nombre ", nameCol)

    def contar2(self, datos:list, typ:str) -> list:
        """Devuelve una lista con posiciones inciales y cantidad de elementos

        Devuelve una lista de posiciones iniciales y cantidad de elementos qcontinuos que le siguen a la posición inicial. Se puede contar datos ('d') o huecos ('h') contenidos en la lista de datos de entrada, a la salida se regresa la posición del dato o hueco y la contidad de elementos continuos del mismo tipo

        Parameters
        ----------
        datos : list
            Lista de datos que será contada
        typ : str
            Tipo de dato que se está contando

        Returns
        -------
        list
            Lista de datos, en la primera posición contiene el indice y en la segunda posición contiene la cantidad

        Example
        -------
        data = [1,1,2,3,nan,2,3]
        >>> r.contar(data,'h')
        ([[4, 1]], 1, 1)
        >>> r.contar(data,'d')
        ([[0, 4], [5, 2]], 4, 3)
        """        

        if len(data) == 0:
            #Verificamos que haya datos
            return(False)
            #Si hay datos podemos contnuar
        else:
            #Obtenemos los indices de los datos o huecos
            if typ == 'd':
                d2i = self.data2index(datos)[0]
            else:
                d2i = self.data2index(datos)[1]
            #Si no hay datos terminamos
            if d2i == []:
                return(False)

            #Creamos variables
            indexL = list()
            i = 0

            #Caminamos por cada indice
            for indice in d2i:
                if not np.isnan(datos[indice-1]):
                    try:
                        while np.isnan(datos[indice]) == np.isnan(datos[indice + i]):
                            i += 1
                        indexL.append([indice,i])
                        i = 0
                    except:
                        pass
                
            #indexL.append([pos,contar])
            return(indexL)

    def data2index(self, datos:list) -> list:
        """Devuelve una lista de listas que contienen las posiciones de cada uno de los datos

        Devuelve una lista de listas, en la primera posición estarán los indices de los datos y en la segunda posición estará la lista de los indices de los huecos.

        Parameters
        ----------
        datos : list
            Lista de datos
        typ : str
            Tipo de dato a trasnformar

        Returns
        -------
        list
            Vector de tamaño 2, en la primera posición una lista de posiciónes de datos, en la segunda posición de huecos
        """       

        if len(datos) == 0:
            return(False) 

        else:
            indexd = []
            indexh = []
            for i in range(len(datos)):
                if np.isnan(datos[i]):
                    indexh.append(i)
                else:
                    indexd.append(i)
            return([indexd,indexh])

    def contar(self, nameCol:str, typ:str) -> list:
        """Devuelve una lista con posiciones iniciales y cantidad de elementos.
        
        Devuelve una lista de posiciones iniciales y cantidad de elementos continuos que le siguen a la posición inicial. Se puede contar datos ('d') o huecos en una columna ('h').
        
        Parameters
        ----------
        nameCol : str
            Nombre de la columna a contar
        typ : str
            Indica lo que se está buscando, huecos o datos.

        Returns
        -------
        tuple
            Regresa un tripleta de datos, la primera posición es una lista de posiciones y tamaños, la segunda posición refleja el total acumulado y la tercera el valor máximo.

        Example
        -------
        namecol = 'x_i'
        >>> r.contar(namef<col,'h')
        ([[0, 1]], 1, 1)
        >>> r.contar(namecol,'d')
        ([[0, 3], [4, 1]], 4, 3)
        """                

        if nameCol in self.df.columns: #Verificamos que exista la columna

            #Obtenemos los indices de los datos a contar
            posD = self.indices(nameCol,typ)
            #En caso de que no haya valores
            if posD == []:
                return([[0, 0]],0,0)
            else:

                #Definimos variables a usar
                contar = 1
                vecSalida = list()
                valMax = 0  #Tamaño continuo máximo
                acum = 0    #Datos totales contados
                posIni = 0

                #Supongo que el segundo dato debe ser del mismo tipo que el segundo, por ello empiezo el contador en uno.
                #Nos movemos en los indices que se obtuvieron
                for i in range(1,len(posD)):
                    #Verifico que el indice anterior y el actual sean continuos
                    if posD[i - 1]+1 == posD[i]:
                        #Si no he contado nada aún, no me he movido
                        if contar == 0:
                            #Mi posición inicial es uno antes
                            posIni = posD[i - 1]
                        #Aumento el contado
                        contar += 1
                    else:
                        #Agrego el total de números contados, la posición inicial y verifico los valores máximos y acumulado
                        vecSalida.append([posIni,contar])
                        acum += contar
                        if contar > valMax:
                            valMax = contar
                        #Reinicio variables
                        contar = 1
                        posIni = posD[i]
                #Agrego datos que pudieran quedar fuera
                vecSalida.append([posIni,contar])
                acum += contar
                if contar > valMax:
                    valMax = contar
                return(vecSalida,acum,valMax)
        else:
            print("No existe la columna")

    def indices(self,nameCol:str,typ:str) -> list:
        """Devuelve una lista de indices de datos o huecos.
        
        Devuelve una lista de indices analizando los datos que se encuentran en nameCol y buscando huecos o datos, según typ.
        
        Parameters
        ----------
        nameCol : str
            Nombre de la columna a analizar
        typ : str
            Tipo de dato a identificar

        
        Returns
        -------
        list
            Lista de indices.

        Example
        -------
        >>> r.indices('x_i','h')
        [3]
        >>> r.indices('x_i','d')
        [0, 1, 2, 4]
        """        
        if typ == 'h':
            posD = self.df[nameCol][self.df[nameCol].isna()].index.tolist()
            return(posD)
        elif typ == 'd':
            posD = self.df[nameCol][self.df[nameCol].notna()].index.tolist()
            return(posD)
        else:
            print("Error en la entrada")
            return([])
    
    def hist(self,nameCol:str, typ:str, n:int = 50 ,plot:bool = True) -> tuple:    
        """Devuelve una tupla de datos e imprime un histograma.
        
        Devuelve una tupla de datos, el primer elemento es una lista de bins y el segundo representa las alturas para cada dato. Además imprime un histograma con estos dos datos
        
        Parameters
        ----------
        nameCol : str
            Columna sobre la cual se realiza el histograma
        typ : str
            Se define sobre qué se desea hacer el histograma, datos o huecos
        plot : bool, optional
            Se puede negar la aparición de graficas, by default True
        
        Returns
        -------
        tuple
           Devuelve una tupla de datos. La primera posición es un vector de bins, la segunda lista son alturas para los bins.

        Example
        -------
        >>> bins,h = r.hist('x_i','h',False)
        >>> bins
        [0, 1]
        >>> h
        [0, 1]
        >>> bins,h = r.hist('x_i','d',False)
        >>> h
        [0, 1, 0, 1]
        >>> bins
        [0, 1, 2, 3]
        """        
        #Condición para mostrar todo el histograma y evitar el desvordamiento
        if n == 0:
            n = self.len
        elif n > self.len:
            n = self.len
        
        #Obtenemos una tupla de indices y datos
        tupla = self.contar(nameCol,typ)
        
        if tupla[0][0][1] == 0 or len(tupla[0]) < 2:
            return(False)
        else:            
            #Creamos un vector de ceros de tamaño máximo
            hist = [0 for i in range(tupla[2] + 1)]

            #Rellenamos el vector con unos
            for item in tupla[0]:
                hist[item[1]] += 1
            x = list(range(len(hist)))

            if len(hist) < 50:
                n = len(hist)
            
            #Imprimimos el gráfico
            if plot:
                if typ == 'h':
                    pltstrng = "Histograma de huecos"
                else:
                    pltstrng = "Histograma de datos"

                plt.figure()            
                plt.bar(x[:n],hist[:n])
                plt.title(pltstrng)
                plt.xlabel("Tamaño")
                plt.ylabel("Frecuencia")
                plt.savefig(pathFig+"hist_{}_{}.png".format(typ,self.name))
                plt.show()

            return(x,hist)
        
    def guardar(self):
        """Actualiza el archivo csv o se crea un nuevo archivo"""
        self.df.to_csv(pathCsv+'/f_%s.csv'%self.name,index=False)

    def generadorHuecos(self, denH:list, denD:list,inicialTyp:str='d')->list:
        """generadorHuecos A partir de una lista de densidades de huecos y de densidades de datos, se genera un vector de huecos y datos

        Parameters
        ----------
        nombreCol : str
            Nombre de la columna a generar
        denH : list
            Densidad de huecos
        denD : list
            Densidad de datos

        Returns
        -------
        list
            Regresa una lista con unos y nan
        """        
        #Elegimos qué lista va a ser la primera, empezar con huecos o con datos, en genral se empieza con datos
        if inicialTyp == 'd':
            #Creamos la primera lista de datos
            aux = np.ones(denD[0])
            flag = False
            ih = 0
            id = 1
        elif inicialTyp == 'h':
            #Creamos la primera lista de huecos
            aux = np.zeros(denH[0])
            aux[:] = np.nan
            flag = True
            ih = 1
            id = 0
        else:
            return("Comando no identificado, intente d o h")

        #Creamos una lista almenos tan grande como el tamaño de los datos totales
        while len(aux) < self.len:
            #Aseguramos que se vuelva a iniciar el recorrido por la lista.
            if id >= len(denD) or ih >= len(denH):
                id = ih = 0
            #Usamos un if para cambiar entre datos y huecos
            if flag:
                aux = np.append(aux,np.ones(denD[id]),axis = None)
                id += 1
                flag = False
            else:
                aux2 = np.zeros(denH[ih])
                aux2[:] = np.nan
                aux = np.append(aux,aux2,axis = None)
                ih += 1
                flag = True

        #Tomamos solo la cantidad de datos que queremos y agregamos en el archivo de datos
        aux = aux[:self.len]
        
        self.añadirCol("HGV",aux)
        return(aux)

    def validaIndices(self, vector:list,indices:list):
        """validaIndices Valida que el vector de entrada tenga datos útiles en las posiciones de la mascara

        Parameters
        ----------
        vector : list
            Datos a verificar
        mascara : list
            Lista de posiciones
        """        
        if not np.isnan(sum(vector.loc[indices])):
            return(True)
        else:
            return(False)

    def verificaDatos(self,nameCol,S:str):
        """verificaDatos regresa los datos pertenecientes a un conjunto definido
        
        Parameters
        ----------
        nameCol : [type]
            Nombre de la columna a buscar
        S : str
            Tipo de dato a buscar
        """        
        return(self.df[nameCol][self.df.S == S])                 #Regresamos el vector de datos que le corresponde al conjunto 

#################
n = 10000
data = generateLorenz(n).tolist()
#db = pd.read_csv("fCDMX.csv")
#date = db.date.tolist()
#data = db.MER.tolist()
#Lista de fechas
date = ['01/01/1986 01:00:00' for i in range(n)]
print(len(data))

####################
prueba = Reconstruir(data[:50000],date[:50000],"Prueba")
prueba.generadorHuecos([1,2,1,3,4,5],[5,6,7,8,9])

k = 1
h = 1
for j in range(4):
    print("Hueco tamaño: ",j)
    m = random.randrange(1,4)
    tau = random.randrange(1,3)
    k = random.randrange(1,4)
    print("m {}, tau{}".format(m,tau))
    for i in range(2):
        print("Reconstuccion")
        reg = distancias(prueba,metricaEu,['HGV3'],'E',h+j,m,tau,k)
        #############
        #El error sirve para conocer cuales son los mejores parametrosprint()
        error = 0
        count = 0
        for indice in reg[1]:
            #print("Error: ",prueba.df['x_i'][indice] - reg[0][indice])
            if not np.isnan(prueba.df['x_i'][indice] - reg[0][indice]):
                error += abs(prueba.df['x_i'][indice] - reg[0][indice])
                count += 1
        print("Parametros elegidos")
        print("h{},m{},tau{},k{}".format(h+j,m,tau,k))
        print("Error",error/count)

        #Impresion
        plt.figure(figsize=(10,10))
        plt.plot(prueba.df['x_i'],'o-')
        plt.plot(reg[0],'o')
        plt.savefig("./Reportes/tercerreporte/Figuras/M4h{},m{},tau{},k{}.png".format(h+j,m,tau,k))
        #plt.show()
        
#Recuperar la variable de error
