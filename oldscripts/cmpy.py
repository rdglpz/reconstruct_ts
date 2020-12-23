##################################
#   Ariel Ceron Gonzalez
#   Servicio Social
#   Queretaro, 2019
#
################################
<<<<<<< HEAD
=======
#COMENTARIOS##########33
#
#Pastel
#Considerar el hueco generado para descartar
#Reconstruir con ceros para evitar consideraralo
#ix = np.where(V==algo)
#A[ix]
#np.any(A[ix])np.any(v2[ix])
#Descripción,readme,reconstrucción
########
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662

#some library
import pandas as pd #Permite leer el CSV
import numpy as np  #Permite trabajar con arreglos de pandas y usar nan
import matplotlib.pyplot as plt #Permite graficar
import os   #Permite interactuar con las rutas de la pc
import math as mt # Permite hacer comparaciones logicas
import csv
from datetime import datetime
import random
from sortedcontainers import SortedList

###############Funciones###############
def toStr(value:int)->str:
    """toStr Transforma un valor numérico en el conjunto de los enteros entre cero y dos, para devolver un carácter.
    
    Para conocer a qué conjunto pertenece cierto elemento del conjunto de datos, se les establece una etiqueta que, en principio es obtenida de forma numérica con el uso de una división y después es transformada a un carácter con el uso de esta función.
    
    Parameters
    ----------
    value : int
        Valor entero entre cero y dos.
    
    Returns
    -------
    str
        Valor string del conjunto [E,P,V]

    Examples
    --------
        >>> num = 0
        >>> strg = cmpy.toStr(num)
        >>> print(strg)
        E
    """    
    if value == 0:
        return('E')
    elif value == 1:
        return('P')
    elif value == 2:
        return('V')

def numNan(lista:list)->int:
    """numNan Cuenta la cantidad de elementos NAN contenidos en una lista.
    
    Parameters
    ----------
    lista : list
        Lista con elementos tipo NAN
    
    Returns
    -------
    int
        Entrega la cantidad de elementos NAN en la lista.

    Example
    -------
        >>> lista = [1,2,3,np.nan,4,5,np.nan,6,np.nan,np.nan,7,8,np.nan,9,10]
        >>> numNan = cmpy.numNan(lista)
        >>> print(numNan)
        5
    """    
<<<<<<< HEAD
    count = 0
    for elemento in lista:
        if mt.isnan(elemento):
            count+=1
    return(count)

def getMask(h:int,tau:int,m:int)->list:
=======
    contar = 0
    for elemento in lista:
        if mt.isnan(elemento):
            contar+=1
    return(contar)

def creaMascara(h:int,tau:int,m:int)->list:
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662
    """getVMask Regresa una mascara de ceros y unos dados los parámetros h, tau, m
    
    Parameters
    ----------
    h : int
        Número de ceros que tendrá el centro de la lista
    tau : int
        Frecuencia de aparición de los unos
    m : int
        2m es la cantidad de unos totales en la lista
    
    Returns
    -------
    list
        Lista binaria [datos hueco datos]
    
    Example
    -------
    >>> h = 1
    >>> m = 2
    >>> tau = 3
<<<<<<< HEAD
    >>> lista = cmpy.getMask(h,tau,m)
=======
    >>> lista = cmpy.creaMascara(h,tau,m)
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662
    >>> print(lista)
    [1, 0, 0, 1, 0, 1, 0, 0, 1]

    """    
    i = j = 0
    tmp = list()
    while(j != m):
        if i%tau == 0:
            tmp.append(1)
            j+=1
        else:
            tmp.append(0)
        i+=1
    vH = [0 for k in range(h)]
    return(tmp+vH+tmp)


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


###############Objetos###############
<<<<<<< HEAD
class toReconst(object):
    
    def __init__(self):
        self.dt = None      #Guarda el conenido del archivo 
        self.name = None    #Guarda el nombre del archivo
        #Banderas que definen el tipo de archivo que se ha almacenado
        self.frdf = None     #Bandera de lectura de archivo
        self.ffile = None
        
    def read_dt(self, name:str,data:list, date:list = [],v:list = [50,25,25] ):
        """read_dt Permite la lectura de datos generados y almacenados en forma de lista
        
        Parameters
        ----------
        name : [type]
            Nombre de los datos
        data : [type]
            Lista de datos
        date : bool, optional
            Lista de fechas, by default False

        Example
        -------
        >>> dataLorenz = lorenz.generateLorenz()
        >>> print(dataLorenz)
        [0.    0.2   0.356 ... 0.    0.    0.   ]
        >>> prueba = cmpy.Data2Object()
        >>> prueba.read_dt('Lorenz',dataLorenz)
        Datos exportados"""       
        try:
            if not date:
                print("First input")
                self.dt = [[i for i in range(len(data))],data]
                self.frdf = True
                self.ffile = False
                self.name = name
                self.dt = self.exp2csv_dt(name,v)

            else:
                if len(date) == len(data):
                    print("Second input")
                    self.dt = [date, data]
                    self.frdf = True
                    self.ffile = False
                    self.name = name
                    self.dt = self.exp2csv_dt(name,v)
                    
                else:
                    print("Los datos ingresados son de diferentes tamaños")
        except:
                self.frdf = False
                print("Datos no exportados")

    def write_csv(self, file:object, data:list):
        """write_csv Escribe contenido en un objeto tipo file
   
        Parameters
        ----------
        file : object
            Objeto file donde se almacenarán los datos
        data : list
            Lista de 4 elementos que se incluirá en el documento.
        """        
        file.write('{},{},{}\n'.format(data[0],data[1],data[2]))


    def exp2csv_dt(self,name, v:list = [50,25,25],n:int = 0)->object:
        """exp2csv_dt Exporta los datos importados con la función read_dt
        
        Parameters
        ----------
        fname : str
            Nombre de la estación a exportar
        v : list, optional
            Porcentaje de datos que serán tomados como entrenamiento, prueba y validación, en ese orden by default [50,25,25]
        n : int, optional
            Permite tomar los n primeros elementos, by default 0
        
        Returns
        -------
        object
            Un data frame con estructura especificada 
        """        
 
               
        if (n == 0):
            n = len(self.dt[0])

        file = open('./CSVfiles/f_%s.csv'%name,'w')
        #Se asigna a la primera linea el encabezado
        file.write('date,x_i,S\n')
        print('Exportando datos del archivo con el nombre %s'%name)

        aux = 0

        for i in range(len(v)): #Obtiene el valor definido de cada conjunto
            s = toStr(i)
            #print(aux,aux+round(n*(v[i]/100))-1)
            for elemento in range(aux,aux+round(n*(v[i]/100))-1): #Especifica el tañamo del conjunto
                
                self.write_csv(file,[self.dt[0][elemento],
                            self.dt[1][elemento],s])
            aux += round(n*(v[i]/100)) # Modifica la posición

            #Informa la finalizacción
        print('Datos exportados')
        file.close() #Cierra el archivo
        print('Archivo f_%s creado'%name) #informa de la creación

        return(pd.read_csv('./CSVfiles/f_%s.csv'%name))



    def read_csv(self,estacion:str):
        """read_csv Importa archivos provenientes de un csv ubicados en ./CSVfiles
        
        Parameters
        ----------
        estacion : str
            Nombre de la estación a importar
        
        Example
        -------
        >>> estaciones = prueba.keys()
        >>> cdmx.read_csv(estaciones[0])
        Archivo leido
        """        
        try:
            self.dt = pd.read_csv('./CSVfiles/f_%s.csv'%estacion)
            self.name = estacion
            self.frdf = False
            self.ffile = True   #Bandera de que existe un archivo
            print('Archivo leido')
        except:
            self.frdf = False
            print('Falló en la exportación')
    

    def count_h(self,nameCol:str = 'x_i')->object:
        """count_h Cuenta los huecos que existen en una columna existente del archivo
        
        Parameters
        ----------
        nameCol : str, optional
            Nombre de la columna a contar, by default 'isNull'
        
        Returns
        -------
        object
            DataFrame que contiene el indice de inicio del hueco y la cantidad de huecos contados

        Example
        -------
        >>> huecos = cdmx.count_h()
        >>> print(huecos)
            posIni  numHuecos
        0          0        240
        1        288        240
        2        544          1
        3        553          6
        4        568          1
        ...      ...        ...
        3827  288838          3
        3828  288886          9
        3829  288910          3
        3830  288982         24
        3831  289126          3

        [3832 rows x 2 columns]
        """        
        #Variables auxiliares para obtener la cantidad de huecos y la posición inicial donde se encuentra el hueco 
        posIni = 0
        numH = 0

        listnum = list()
        listpos = list()
        headstr = ['posIni','numHuecos']

        if self.frdf or self.ffile:
            #Obtenemos la lista de booleanos que tiene el formato
            if nameCol == "x_i":
                lbool = np.isnan(self.dt[nameCol].tolist()) 
            else:
                lbool = self.dt[nameCol].tolist()
            n = self.dt.shape[0]
            #Revisa en todos los datos
            for item in range(n):
                if lbool[item]:#Se revisa en la lista aquellos que son nulos
                    if numH == 0:
                        posIni = item
                        numH += 1
                    else:
                        numH += 1
                else:
                    if numH != 0:
                        listnum.append(numH)
                        listpos.append(posIni)
                        numH = 0
                        posIni = 0
            if numH != 0:
                listnum.append(numH)
                listpos.append(posIni)
                numH = 0
                posIni = 0
            d = list(zip(listpos,listnum))
            df = pd.DataFrame(d, columns = headstr)
            return(df)                    
        else:
            print("No se han ingresado datos")

    def count_d(self,nameCol:str='x_i')->object:
        """count_d Cuenta los datos que existen en una columna existente del archivo
        
        Parameters
        ----------
        nameCol : str, optional
            Nombre de la columna a contar, by default 'isNull'
        Returns
        -------
        object
            DataFrame que contiene el indice inicial de los datos y la cantidad de datos que conto

        Example
        -------
        >>> datos = cdmx.count_d()
        >>> print(datos)
               posIni  numDatos
        0        240        48
        1        528        16
        2        545         8
        3        559         9
        4        569         7
        ...      ...       ...
        3827  288841        45
        3828  288895        15
        3829  288913        69
        3830  289006       120
        3831  289129       140

        [3832 rows x 2 columns]
        """       
        #Variables auxiliares para obtener la cantidad de huecos y la posición inicial donde se encuentra el hueco 
        posIni = 0
        numD = 0

        listnum = list()
        listpos = list()
        headstr = ['posIni','numDatos']

        if self.frdf or self.ffile:
            #Obtenemos la lista de booleanos que tiene el formato
            if nameCol == "x_i":
                lbool = np.isnan(self.dt[nameCol].tolist()) 
            else:
                lbool = self.dt[nameCol].tolist()
            n = self.dt.shape[0]
            for item in range(n):
                if not lbool[item]: #Busca los datos que no son nulos
                    if numD == 0:
                        posIni = item
                        numD += 1
                    else:
                        numD += 1
                else:
                    if numD != 0:
                        listnum.append(numD)
                        listpos.append(posIni)
                        numD = 0
                        posIni = 0
            #Verifica que todos los datos se almecen en las lista de numeros y posiciones
            if numD != 0:
                listnum.append(numD)
                listpos.append(posIni)
                numD = 0
                posIni = 0
            #Crea un DataFrame y lo retorna
            d = list(zip(listpos,listnum))
            df = pd.DataFrame(d, columns = headstr)
            return(df)                    
        else:
            print("No se han ingresado datos")

    def hist(self, data:str = 'h',nameCol:str = "x_i",num:int = 10,getData:bool = False)->tuple:
        """hist Imprime el histograma de los datos encontrados
        
        Parameters
        ----------
        data : str, optional
            Define qué tipos de datos serán exportados, by default 'h'
        num : int, optional
            Indica el porcentaje de datos que serán visualizados, by default 30
        getData : bool, optional
            Inidca si queremos o no obtener datos de salida, by default False
        
        Returns
        -------
        tuple
            Clasificación de los elementos y cantidad de datos
        [Figure]

        Example
        -------
        >>> cdmx.hist()

        """        
        #Dependiendo que histograma se quiera, se dará el histograma de huecos o de datos
        if data == 'h':
            df = self.count_h(nameCol)
            #Obtenemos el histograma
            #bins range(1,maxnumhuecos)
            n,bins,na = plt.hist(df.numHuecos.tolist(),max(df.numHuecos.tolist()))
            plt.close()
            titlestr = "Histograma de Huecos"
        elif data == 'd':
            df = self.count_d(nameCol)
            #Obtenemso el histograma
            n,bins,na= plt.hist(df.numDatos.tolist(),max(df.numDatos.tolist()))
            plt.close()
            titlestr = "Histograma de Datos"
        #Imprimimos el histograma con los datos obtenidos arriba
        plt.figure()
        #num = round((len(bins)/100)*num)
        plt.bar(bins[:num],n[:num])
        plt.title(titlestr)
        plt.xlabel("Bins")
        plt.ylabel("n")
        plt.show()

        if getData:
            return(bins,n)

    def add_col(self,name:str,data:list):
        """add_col Agrega contenido al DataFrame con el que se trabaja
        
        Parameters
        ----------
        name : str
            Nombre de la nueva columna
        data : list
            Datos que se desea ingresar
        """        
        self.dt[name] = data
        print("Datos agregados")

    def exp2csv(self):
        """Actualiza el archivo csv o se crea un nuevo archivo"""
        if self.frdf:
            if self.ffile:
                #Si existe el archivo
                print("Actualizando archvio f_%s"%self.name)
                self.dt.to_csv('./CSVfiles/f_%s.csv'%self.name)
            else:
                print("Se creara archivo f_%s"%self.name)
                self.dt.to_csv('./CSVfiles/f_%s.csv'%self.name)

    def genFail(self,nameCol:str,denH:list,denD:list) -> list:
        """genFail Genera huecos y los agrega a una nueva columna del archivo con el que se trabaja tomando como parámetro 0 si es dato y 1 si es hueco
        
        Parameters
        ----------
        denH : list
            Lista numérica que asigna la cantidad de huecos
        denD : list
            Lista numérica que asigna la cantidad de datos

        Example
        -------
        >>> huecos = huecos.numHuecos.tolist()
        >>> datos = datos.numDatos.tolist()
        >>> cdmx.genFail(huecos,datos)
        Datos agregados
        """       
        #Variables
        count = 0   #contador
        indexh = 0  #Indice de hueco
        indexd = 0  #Indice de datos    
        flag = True #Bandera
        vtmp = list()   #Lista
        #Recorremos todo el vector de datos
        while(count < self.dt.shape[0]):
            #Vamos a saltar entre verdad y falcedad de la bandera para poner huecos o datos
            if flag:
                #Coloca falsos en la lista
                tmp = np.zeros(denH[indexh]).tolist()
                vtmp.extend(tmp)
                count += len(tmp)
                #print("if",indexh)
                indexh += 1
                flag = False

            else:
                #Coloca verdaderos en la lista
                tmp = np.ones(denD[indexd]).tolist()
                vtmp.extend(tmp)
                count += len(tmp)
                #print("else",indexd)
                indexd += 1
                flag = True
        #Aagregamos el vector que creamos en los datos
        self.add_col(nameCol,vtmp[:self.dt.shape[0]])
        #return(vtmp[:self.dt.shape[0]])
        
    def getHole(self,h:int,tau:int,m:int,nameCol:str) -> list:
        """getHole Regresa una lista de posiciones de huecos que cumplen la nula existencia de elementos NAN según los parámetros h, tau, m
=======
class Reconstruir(object):

    def __init__(self):
        """__init__ Constructor del objeto. El objeto inicia vacío, él contiene diferentes atributos que modificara y ordenará durante la manipulación de este objeto. El objeto contendrá un nombre que le identifique, una matriz numpy que contenga los datos y las fechas de registro, así como los datos que se vayan generando. Una bandera de lectura que nos permita conocer el estatus del objeto

        Example
        -------
        >>> objeto = Reconstruir()
        """        
        self.name = None    #Nombre de los datos
        self.dt = None      #Datos numéricos
        self.flag = False   #Bandera de lectura
        self.dic = None     #Diccionario de indices
        self.len = None     #Tamaño del arreglo
        self.nCol = None    #Número de columnas en la matriz
        
    def guardar(self):
        """guardar Almacena un archivo CSV cuando se ha terminado de trabajar con el objeto
        """        
        #Creamos el encabezado del archivo
        strname = ","
        strname = strname.join(self.dic.keys())
        #Ordenamos los datos en forma de columna
        datos = np.array([np.array(xi.astype(str)) for xi in self.dt])
        datos = datos.transpose()
        print(datos)
        #Generamos el archivo csv
        name = self.name + '.csv'
        fmt=['%s' for i in range(self.dt.shape[0])]
        np.savetxt(name,datos,delimiter=",",fmt = fmt, header=strname,comments='')
        #Información de generación
        print("Archivo {}.csv generado".format(self.name))

    def añadirCol(self, name:str, data:list):
        """ Añade un elemento a la matriz con la que se trabaja, remplazando espacios faltantes por NAN y con una etiqueta
        
        Parameters
        ----------
        name : str
            Nombre de la columna que almacenará los datos
        data : list
            Lista de elementos que harán de nueva columna
        """        
        #Verificamos el tamaño de los datos de entrada
        if len(data) == self.len:
            #Agregamos los nuevos datos si miden lo mismo
            aux = self.dt.tolist()
            aux.append(data)
            self.dt = np.array(aux)
        else:
            #Creamos un vector de NAN de los datos faltantes
            aux = np.zeros(self.len-len(data))
            aux[:] = np.nan
            data.extend(aux)
            aux = self.dt.tolist()
            aux.append(data)
            self.dt = np.array(aux)
        #Agregamos el nombre de la columna al diccionario de columnas
        self.nCol += 1
        self.dic[name+str(self.nCol)] = self.nCol
        print("Datos {} agregados".format(name+str(self.nCol)))
        

    def vecS(self,vec:list,n:int)->list:
        """vecS Regresa un vector n dimensional con elementos E,P,V; según el vector dado.
        
        Parameters
        ----------
        vec : list
            Describe el porcentaje que debe cubrir cada letra dentro del arreglo
        
        Returns
        -------
        list
            Lista n dimensional con elemento E,P,V

        Example
        -------
            
        """        
        aux = 0         #Define el rango para generar el arreglo
        v = np.ceil(n*(np.asarray(vec)/100))
        #Definimos los rangos para el arreglo
        #Creamos vectores según el tamaño generado
        l = np.zeros(v[0].astype(int))
        l1 = np.array([toStr(int(i)) for i in l])
        l = np.ones(v[1].astype(int))
        l2 = np.array([toStr(int(i)) for i in l])
        l = np.ones(v[1].astype(int))*2
        l3 = np.array([toStr(int(i)) for i in l])
        aux = np.concatenate((l1,l2,l3),axis=None)
        return(aux[:self.len])

    def leer(self, name:str, data:list, date:list, vec:list = [50,25,25]):
        """read Permite ingresar los datos a evaluar con el objeto. Se debe ingresar tres vectores de datos, los datos, las fechas relacionadas con los datos y la relación de datos que se quiera usar para entrenamiento, validación y prueba. Esta función rellena de parámetros al objeto.

        Parameters
        ----------
        data : list
            Lista de datos que se quieran analizar
        date : list
            Lista de fechas que se le pueda relacionar a cada dato
        vec : list, optional
            Vector que separa los datos en entrenamiento, validación y prueba, by default [50,25,25]

        Example
        -------
            >>> objeto.read("Prueba",[0,1,2,3,4,5],[0,1,2,3,4,5])
        """        
        if len(data) == len(date):
            self.name = name    #Asignación del nombre de los datos
            self.dt = np.array([date,data,self.vecS(vec,len(data)).tolist()])   #Creación de la estructura de datos
            self.flag = True    #Cambio de bandera de lectura
            self.dic = {'Registro':0,'x_i':1,'S':2}     #Nombre de las columnas
            self.len = len(data)
            self.nCol = 2
        else:
            print("Datos no exportados.\n Revisa el tamaño de los arreglos de entrada.")

    def validaIndices(self,nameCol:str,h:int,m:int,tau:float):

        data = self.dt[self.dic[nameCol]]
        if data.dtype == '<U32':
            data = data.astype(np.float64)
        mascara = creaMascara(h,tau,m)
        n = np.round((len(mascara)-h)/2).astype(int)
        indicesV = list()
        for i in range(n,(len(data)-(h+n))):
            v = np.asarray(data[i-n:i+h+n])
            indices = np.where(np.asarray(mascara) == 1)
            if not np.isnan(sum(v[indices])):
                indicesV.append(i)
        return(indicesV)

    def indices(self,nameCol:str,typ:str) -> list:
        """[summary]
        
        Arguments:
            nameCol {str} -- [description]
            typ {str} -- [description]
        
        Returns:
            list -- [description]
        """   
        if typ == 'h':      #Verificamos qué esta buscando
            if self.dt[self.dic[nameCol]].dtype == '<U32':
                posD = np.where(np.isnan(self.dt[self.dic[nameCol]].astype(np.float64)) == True)[0] 
            else:   
                posD = np.where(np.isnan(self.dt[self.dic[nameCol]]) == True)[0]   #Obtenemos el vector de posiciones de los huecos
        elif typ == 'd':
            if (self.dt[self.dic[nameCol]].dtype == '<U32'):
                posD = np.where(np.isnan(self.dt[self.dic[nameCol]].astype(np.float64)) == False)[0]
            #posD = np.where(np.isnan(self.dt[self.dic[nameCol]].astype(np.float64)) == False)   
            else:
                posD = np.where(np.isnan(self.dt[self.dic[nameCol]]) == False)[0]   
            #Obtenemos el vector de posiciones de los datos
        else:
            print("Tipo de busqueda erronea, verifique con d o h") 
            return(False)
        return(posD)

    def contar(self, nameCol:str, typ:str = 'd') -> list:
        """contar Cuenta la cantidad de elementos existentes o nulos que existan en la columna especificada.

        Parameters
        ----------
        nameCol : str
            Nombre de la columna sobre la cual se hará el conteo
        typ : str, optional
            Definición del tipo de busqueda d para datos, h para nulos, by default 'd'

        Returns
        -------
        list
            Regresa una tripleta, en la primera posición una matriz de posiciones, en la segunda el valor máximo de huecos y en la tercera el acumulado
        """       
        if self.flag:    #Verificamos que existan datos
            if nameCol in self.dic:     #Verificamos que exista la columna
<<<<<<< HEAD
                if typ == 'h':      #Verificamos qué esta buscando
                    posD = np.where(np.isnan(self.dt[self.dic[nameCol]].astype(np.float64)) == True)   #Obtenemos el vector de posiciones de los huecos
                elif typ == 'd':
                    posD = np.where(np.isnan(self.dt[self.dic[nameCol]].astype(np.float64)) == False)   
                    #Obtenemos el vector de posiciones de los datos
                else:
                    print("Tipo de busqueda erronea, verifique con d o h")

                i = 0               #Permite el movimiento en el vector de posiciones
                pos = None          #Almacena la posición inicial
                contar = 1           #Almacena la cantidad de elementos continuos
                vecSalida = list()  #Vector que almacena las posiciones y cantidades
                valMax = 0          #Valor máximo registrado
                acum = 0            #Valor acumulado, es decir, la cantidad total de elementos
                #Avanzamos en la lista de posiciones
                while i < len(posD):
                    faux = True     #Bandera de incursión
                    pos = posD[0][i]    #Almacenamiento de la posición inicial
                    if faux:    
                        #Verificación de termino de recorrido por desborde
                        if pos + contar >= len(posD[0]):
                            vecSalida.append((pos,contar))
                            acum += contar
                            if valMax < contar:
                                valMax = contar
                            return(vecSalida,valMax,acum)
                        #Verificación de continuidad en los indices
                        if pos + contar == posD[0][pos + contar]:
                            contar += 1
                        #Reinicio de conteo
                        else:
                            vecSalida.append((pos,contar))
                            acum += contar
                            i += contar
                            if valMax < contar:
                                valMax = contar
                            contar = 1
                            faux = False
=======
                #obtenemos los indices
                posD = self.indices(nameCol,typ)

                contar = 1  #Cuenta los elementos continuos
                vecSalida = list()  #Almacena las posiciones y la cantida
                valMax = 0  #Almacena el valor del hueco máximo
                acum = 0    #Almacena la cantidad total de elementos contados
                posIni = 0
                
                #Empieza en uno porque inicio en uno despues, suponiendo que conozco qué tipo de elemento es el primer elemento
                for indice in range(1,len(posD)):
                    #Verifico que el indice anterior sea igual al que le sigue más uno
                    if posD[indice - 1]+1 == posD[indice]:
                        #En caso de que no haya contado nada aún, significa que no me he movido 
                        if contar == 1:
                            #Mi posición inicial debe ser uno antes por que inicie uno después
                            posIni = posD[indice-1]
                        #Agrego uno en la continuidad
                        contar += 1
                    #Si a mi número anterior no le sigue el número actual
                    else:
                        #Agrego el total de números contados y la posición inicial que tuve
                        vecSalida.append([posIni,contar])
                        #Sumo al acumulado
                        acum += contar 
                        #Verifico que sea el hueco más grande
                        if contar > valMax:
                            valMax = contar
                        #Reinicio mis contadores y modifico la posición inicial
                        contar = 1
                        posIni = posD[indice]
                        
                #Agrego el último elemento registrado y verifico lo mismo
                vecSalida.append([posIni,contar])
                acum += contar 
                if contar > valMax:
                    valMax = contar
                return(vecSalida,acum,valMax)

>>>>>>> d6f32624c75e8cf5c036421cecbfe6845932867d
            else:
                print("No existe la columna ingresada")
        else:
            print("No se han introducido datos aún")
    
    def hist(self, typ:str, nameCol:str, All:bool = False)->list:
        """A la vez que imprime un histograma de la densidad de huecos o datos, según la entrada, regresa una lista de elementos y sus cantidades

        Parameters
        ----------
        typ : str
            Define si se desea un histograma de datos o de huecos
        nameCol : str
            Define la columna sobre la cual se desea trabajar
        All : bool, optional
            Será True si se quiere mostrar todo el histograma, en caso contrario solo se mostrara una parte, by default False

        Returns
        -------
        list
            Regresa una tupla de elementos y la cantidad de elementos encontrados.
        """        
        if self.flag:
            #Obtenemos la lista de posiciones y cantidades, así como el número máximo continuo encontrado
            tupla = self.contar(nameCol,typ)
            #Creamos una lista de elementos de tamaño máximo
            hist = np.zeros(tupla[2]+1)

            #Hago un histograma añadiendo uno en la posición donde haya un elemento
            for item in tupla[0]:
                hist[item[1]] += 1

            if typ == 'h':
                pltstrng = "Histograma de huecos"
            else:
                pltstrng = "Histograma de datos"

            plt.figure()
            x = list(range(len(hist)))
            plt.bar(x,hist)
            plt.title(pltstrng)
            plt.xlabel("Tamaño")
            plt.ylabel("Frecuencia")
            plt.show()

            return(np.array([np.asarray(x),hist]))
        else:
            print("No se han introducido datos")

    def describe(self):
        """describe el objeto con el que se esta trabajando, mostrando en pantalla los parámetros que definen al objeto, el nombre de las columnas, el histograma de los datos originales y la relación de datos que existe
        """        
        if self.flag:
            labels = ["Datos","Huecos"]
            sizes = [self.contar('x_i','d')[1],self.contar('x_i','h')[1]]
            colors = ['green','red']

            print("{} contienen {} elementos".format(self.name,self.len))
            #print("Se tienen las siguientes columnas",self.dic.keys())
            plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%')
            plt.axis('equal')
            plt.show()

            self.hist('h','x_i')
            self.hist('d','x_i')
            
        else:
            print("No se han introducido datos")

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

    def reconstruyeHuecos(self,nameCol:str,h:int,m:int,tau:float):
        """Reconstruye los huecos de tamaño h, teniendo como parámetros de relleno h, tua 

        Arguments:
            nameCol {str} -- Nombre de la columna a rellenar
            h {int} -- Tamaño del hueco a rellenar
            m {int} -- Cantidad de unos en el vector de busqueda
            tau {float} -- Frecuencia (tiene otro nombre pero no recuerdo)
        """ 
        #Siempre vamos a trabajar con nuestros datos
        data = np.asarray(self.dt[self.dic['x_i']])
        if data.dtype == '<U32':
            data = data.astype(np.float64)
        #Creamos la nueva lista
        recList = np.zeros(self.len) 
        
<<<<<<< HEAD
    def obtenerIndiceHueco(self, h:int, nameCol:str)->list:
        """obtenerIndiceHueco Regresa una lista de posiciones de huecos de tamaño h en la columna nameCol
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662
        
        Parameters
        ----------
        h : int
            Tamaño del hueco central
<<<<<<< HEAD
        tau : int
            Tiempo de retardo
        m : int 
            Cantidad de unos esperados
=======
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662
        nameCol : str, optional
            Nombre de la columna que se lees, by default 'x_i'
        
        Returns
        -------
        list
            Lista de posiciones 

<<<<<<< HEAD
        Example
        -------
        >>> h = 1
        >>> m = 2
        >>> tau = 1
        >>> listH = cdmx.getHole(h,tau,m)
        >>> print(listH)
        [544, 568, 848, 1436, 2267, 6590, 8792, 8802, 8807, 8822, 8827, 9497, 9516, 9658, 9670, 9786, 9903, 9917, 9947, 10215, 10247, 10488, 10672, 10794, 10798, 10808, 10937, 11359, 11418, 11514, 11619, 11685, 11688, 11702, 11814, 11936, 11938, 11940, 11983, 12244, 12399, 12405, 12753, 13116, 13124, 13128, 13142, 13393, 13428, 14839, 15536, 15886, 16555, 16674, 16735, 17066, 17091, 17093, 17095, 17106, 17364, 17582, 18060, 18393, 18836, 18856, 19161, 19338, 19430, 19432, 19556, 19623, 19627, 19652, 19668, 19956, 20036, 20138, 20245,...,]
        """      
        df = self.count_h(nameCol=nameCol) #Obtenemos las posiciones de los huecos
        ltmp = df.loc[df.loc[:,'numHuecos'] == h,:] #filtramos las posiciones donde se encuentre los huecos de tamaño h
        
        ltmp = ltmp.posIni.tolist()
        msk = getMask(h,tau,m) #Obtenemos una mascara de elementos
        n = int((len(msk)-h)/2)  #Obtenemos el tamaño de un lado de la mascara

        vecFinal = list()   #Crea una lista para guardar el vector de huecos
        i = k = 0   #Contadores, i para el tamaño de la mascara, k para el tamaño del vector de huecos

        #Recorremos hasta que se vacie la lista
        while(k != len(ltmp)):
            #Toma el vector de huecos del mismo tamaño que la mascara
            vtmp = self.dt[nameCol][ltmp[k]-n:ltmp[k]+h+n].tolist()
            if nameCol == "x_i":
                vtmp = np.isnan(vtmp)
            
            #Verificamos que i sea verdadero
            if msk[i]:
                if vtmp[i]:
                    k += 1
                    i = 0
                else:   
                    #Verificamos que i sea menor que el tamaño de la mascara
                    if i < len(msk):
                        #Agregamos el valor k-esimo del vector ltmp en el vector final
                        vecFinal.append(ltmp[k])
                        i = 0
                        k += 1
                    i += 1
            else:
                i += 1
        return(vecFinal)
    
    def genData(self,h:int,tau:int,m:int,n:int,nameCol):    
        """genData Genera datos siguiendo una mascara definida
        
        Parameters
        ----------
        h : int
            Tamaño del hueco central
        tau : int
            Frecuencia de aparición de unos
        m : int 
            Cantidad de unos esperados
        """        
        listH = self.getHole(h,tau,m,nameCol)#Vector que almacena las posiciones de los huecos 

        msk = np.array(getMask(h,tau,m)) #Obtenemos la mascara
        m = int((len(msk)-h)/2)  #Obtenemos el tamaño de un lado de la mascara

        listVal = list()#Almacena las aproximaciones
        listPos = list()#Almacena las posiciones

        #Lista ordenada
        sl = SortedList()
        
        k = 0
        #Tomamos cada uno de los elementos de la lista de huecos
        #Para poder observar resultados solo trabajaremos con los primeros diez
        for i in listH:
            print("Procesando...")
            dist = mt.inf
            #Obtenemos el vector a rellenar
            v1 = np.array(self.dt.x_i[i - m:i+h+m].tolist())
            #j = m
            
            #Avanzamos hasta antes de superar el tamaño de la lista
            for j in range(m,self.dt.shape[0] - (h+m+1)):
            #while j <= (self.dt.shape[0] - (h+m+1)):
            #for j in range(m,20):
                v2 = np.array(self.dt.x_i[j-m:j+h+m].tolist())
                if not np.isnan((np.sum(v2))):
                    V = v1 - v2
                    V = V**2
                    Vmsk = V*msk
                    #Obtener las posiciones  de los datos con valor cero
                    #y apartir de esos valores 
                    #Ordenamos los valores encontrados
                    sl.add(np.nansum(Vmsk))
                        
                j += 1 

            #Obtenemos el promedio de los primeros n valores cercanos 
            print(sl[:n])
            prom = sum(sl[:n])
            prom = prom/n
            #Valor encontrado
            listVal.append(prom)
            #Posición del valor
            listPos.append(i)

        return([listVal,listPos])

#####################Ejecución

import lorenz
import datetime

lorenz = lorenz.generateLorenz(1000)
dInicial = datetime.datetime(2014,1,1)
dFinal = datetime.datetime(2019,12,31)
dateLorenz = [(dInicial + datetime.timedelta(days=d)).strftime("%Y-%m-%d") for d in range((dFinal - dInicial).days + 1)]
dateLorenz = dateLorenz[:len(lorenz)]

lorenzP = toReconst()
lorenzP.read_dt("Lorenz",lorenz,dateLorenz)

lorenzP.genFail("userNull",np.random.geometric(p=0.35, size=10000),np.random.geometric(p=0.25, size=10000))
=======
        """        


=======
        #Creamos una mascara con los datos de entrada
        mascara = np.asarray(creaMascara(h,tau,m))

        #Tamaño del vector mascara
        n = int(np.round((len(mascara) - h)/2))

        #Obtenemos los indices de los huecos
        indicesHuecos = np.asarray(self.contar(nameCol,'h')[0])
        idx = np.where(indicesHuecos[:,1]== h)[0]
        indicesHuecos = list(indicesHuecos[idx,0].flat)
        
        #Obtenemos indices que puedan funcionarnos en TODOS los datos
        indicesValidados = self.validaIndices(nameCol,h,m,tau)  

        #Almacenamos los valores encontrados de forma ordenada
        sl = SortedList()

        #Obtenemos el vector a rellenar
        for elemento in indicesHuecos:

            #Buscamos los elementos más cercanos
            v1 = data[int(elemento-n):int(elemento+n+h)]
            #Variable para almacenar el valor nuevo
            prom = 0

            #Quitar de la lista de indices el elemento
            indicesVal = np.delete(indicesValidados,np.where(np.asarray(indicesValidados)==elemento))

            for i in indicesVal:
                v2 = data[i-n:i+n+h]
                V = v2[np.where(mascara ==1)] - v1[np.where(mascara ==1)]
                V = V**2
                V = np.sum(V)
                sl.add((V,i))
            
            pn = 3
            #Hacemos el promedio con los primeros diez
            for j in range(pn):
                prom += data[sl[j][1]]
                prom = prom/pn
            recList = np.insert(recList,elemento,prom)
            
        self.añadirCol("R{}h{}m{}t".format(h,m,tau),recList[:self.len])
        print(len(recList))
        return(recList[:self.len])
>>>>>>> d6f32624c75e8cf5c036421cecbfe6845932867d
>>>>>>> bd7ba44339767b795ec8e12be974c13d67aad662
