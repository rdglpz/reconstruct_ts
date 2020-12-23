##################################
#   Ariel Ceron Gonzalez
#   Servicio Social
#   Queretaro, 2019
#
################################

#some library
import pandas as pd #Permite leer el CSV
import numpy as np  #Permite trabajar con arreglos de pandas y usar nan
import matplotlib.pyplot as plt #Permite graficar
import os   #Permite interactuar con las rutas de la pc
import math as mt # Permite hacer comparaciones logicas
from itertools import groupby #Para una funcion
from operator import itemgetter #Para una funcion
import csv
from datetime import datetime
from sklearn.linear_model import LinearRegression
import random

###############Funciones###############
def Nnan(array):
    """Dado un arregle unidimensional, regresa la cantidad de elementos tipo nan"""
    i = 0
    for elemento in array:
        if mt.isnan(elemento):
            i += 1
    return(i)

def doZero(vector):
    """Hace ceros los elementos nan"""
    aux = list()
    for elemento in vector:
        if mt.isnan(elemento):
            aux.append(0)
        else:
            aux.append(elemento)
    return aux

def invec(v):
    return([v[len(v) - item - 1] for item in range(len(v))])

def VMask(h,tau,m):
    """Una funcion que crea un vector con ceros y unos
        de acuerdo a una cantidad de huecos, frecuencia tau
        y una cantidad m de unos."""

    a = list() #Crea una lista para almacenar valores 0,1
    j = i = 0
    vh = [0 for k in range(h)] # crea un vector de ceros

    #for i in range(0,m): #Crea un vector de tamano m con valores 0,1
    #    if i%tau == 0: #El modulo determina la posicion de los unos
    #        a.append(1)
    #    else:
    #        a.append(0)
    while(j != m):
        if i%tau == 0:
            a.append(1)
            j += 1
        else:
            a.append(0)
        i += 1

    c = list() #Se crea el vector final, compuesto por un lado con el vector a, despues el hueco, despues el vector a
    [c.append(item) for item in invec(a)]
    [c.append(item) for item in vh]
    [c.append(item) for item in a]

    #Se regrsa el vector final
    return np.array(c)


###############Objetos#################
class Data2Object(object):

    def __init__(self):
        """Convierte un archivo de datos con extension csv y un formato dado por la siguiente forma:
                            |Fecha|[Estaciones]|
    donde estaciones es un conjunto de 44 estaciones, para tener a la salida un documento por estacion que contenga un formato establecido."""
        self.dt = None

    def read_csv(self, data):
        """Funcion para leer e importar los datos"""
        try:
            self.dt = pd.read_csv(data)
            print("Datos exportados")
        except:
            print("Datos no exportados")

 
    def Ckeys(self):
        """Permite conocer la cantidad de estaciones y los nombres de ellas"""
        try:
            i = 0 #contador
            estaciones = list() #Almacen de las estaciones
            for elemento in self.dt.keys():
                i += 1  #Conteo de las estaciones
                estaciones.append(elemento) #almacenamiento de las estaciones

            i = i - 1 #El primer elemento es la fecha por los que se descarta
            estaciones.pop(0) #eliminacion del primer elemento

            #Se imprime las estaciones y la cantidad de estaciones
            print("El documento contiene {} estaciones".format(i))
            for elemento in estaciones:
                print(elemento,end=',')
            print("en ese orden.")

        except:
            #Si existe una imposibilidad en el documento
            print("Eror al leer el documento")

    def exp2csv(self, estacion, v = [50,25,25],n = 0):
        """Crea un csv de cada estación que contiene el archivo original siguiendo el siguiente encabezado
                |FECHA|DATO MEDIDO|Nulidad en el archivo original|[Tipo de dato]|Nulidad generada||Aproximación|
        Sonde el tipo de dato especifica a qué conjunto pertenece:
            0: Entrenamiento
            1: Prueba
            2: Verificación
        La nulidad generada va a tomar tres valors:
            0: Dato original
            1: Dato nulo generado
            2: Dato creado
        La nulidad en el archivo es un dato booleano que confirma la existencia de nulidad"""
        try:
            #Usado para tomar menos datos de los que contiene el archivo
            if estacion in self.dt.keys():

                if n == 0:
                    n = len(self.dt[estacion]) #Obtiene y asigna la cantidad de datos en la estación especificada

                #Crea el nuevo archivo con el siguiente nombre: format_estacion.
                file = open('./CSVfiles/format_%s.csv'%estacion,'w')
                #Se asigna a la primera linea el encabezado
                file.write('date,x_i,isNull,S,defNull,y_i\n')

                tmp = self.dt #Se almacena temporalmente el archivo en una
                #i = 0   #contador
                #s = 0 #Conjunto
                aux = 0 #Auxiliar para modificar la posición de escritura de datos

                for i in range(len(v)): #Obtiene el valor definido de cada conjunto
        #            print(a[i],b[i],c[i])
        #            print(aux,aux+round(n*(v[i]/100))-1)
                    for elemento in range(aux,aux+round(n*(v[i]/100))-1): #Especifica el tañamo del conjunto
                        file.write('{},{},{},{},{},{}\n'.
                                format(tmp['date'][elemento],tmp[estacion][elemento],
                                        mt.isnan(tmp[estacion][elemento]),
                                        i,0,tmp[estacion][elemento] if not mt.isnan(tmp[estacion][elemento]) 
                                        else None)) #Escribe en el documento los diferentes datos
                    aux += round(n*(v[i]/100)) # Modifica la posición

                #Informa la finalizacción
                print('Datos de la estacción %s exportados'%estacion)
                file.close() #Cierra el archivo
                print('Archivo creado') #innforma de la creación

            else:
                print('Estación no encontrada')

        except:
            print("Eror al leer el documento")

    def exp2csv_all(self,v=None):
        """Crea un CSV de todas las estaciones que se encuentran en el archivo"""

        print("Exportando todas las estación")
        print("Esto puede tardar un tiempo")
        for estacion in self.dt.keys()[1:]:
            print("Exportando los datos de la estación %s"%estacion)
            if v != None:
                self.exp2csv(estacion,v)
            else:
                self.exp2csv(estacion)
            print("Datos de la estación %s exportados"%estacion)

class R_format(object):

    def __init__(self,estacion):
        """Dado el formato establecido en Data2Form, se exporta una estacion para observar y modificar su contenido"""
        try:
            self.dt = pd.read_csv('./CSVfiles/format_%s.csv'%estacion)
            self.name = estacion
            print('Archivo leido')
        except:
            print('Falló en la exportación')

    def Cdata(self):
        """ Muestra un esquema general del contenido en el archivo, además crea un documento que muestra la posición de los huecos en el archivo"""
        #Impresión de información
        nnull= Nnan(self.dt['x_i'].tolist()) #Obtiene la cantidad de nulls
        #nnull= Nnan(self.dt[' x_i'].tolist())
        print("La estación {} contiene {} datos, de los cuales {} son nulos".format(self.name,self.dt.shape[0],nnull))
        print('Formato y primeros 10 elementos del archivo')
        print(self.dt.head(10))

        #Creación del documento que facilita el histograma
        self.exportH(self.dt['isNull'],self.name)
        #self.exportH(dt[' isNull'],self.name)

        #Lectuara del archivo creado
        dh = pd.read_csv('./CSVfiles/hist_%s.csv'%self.name)
        plt.figure(figsize=[10,10])
        plt.subplot(2,1,1)
        plt.title('Relación de datos faltantes')
        plt.pie(self.Nnan(self.dt['isNull']),labels=['Datos','NAN'],explode=(0.1,0))
        plt.subplot(2,1,2)
        plt.title('Histograma de huecos')
        plt.xlabel('Número de huecos')
        plt.ylabel('Cantidad de huecos')
        plt.hist(dh['Size'])
        plt.show()

    def exportH(self,array,estacion):
        """La entrada debe ser un array de booleanos, la salida indica
            la posición de los booleanos positivos y la cantidad de ellos"""
        f = open(r'./CSVfiles/hist_%s.csv'%estacion,'w')
        f.write('PosIni,PosFin,Size\n')
        count = 0
        ini = 0
        fin = 0
        for pos in range(len(array)):
            if array[pos]:
                if count == 0:
                    ini = pos
                count += 1
            else:
                if count != 0:
                    fin = pos - 1
                    f.write('{},{},{}\n'.format(ini,fin,count))
                count = 0
        if count != 0:
            fin = len(array)-1
            f.write('{},{},{}\n'.format(ini,fin,count))
        f.close()

    def Nnan(self,array):
        """Normaliza la cantidad de datos"""
        s = len(array)
        sn = 0
        for elemento in array:
            if elemento:
                sn+=1
        sn = (sn/s)*100
        s = 100 - sn
        return([s,sn])

    def Rellena(self,h=1,tau=1,m=1):
        """El objeto es una base de datos, por lo que dado el objeto R_format, se buscar rellenar todos los huecos que esten en él de tamaño h y definida con los parámetros tau, m"""
        #Por precausión
        dtc = self.dt.copy()
        #Se crea la ventana que recorrera el arreglo
        ventana = VMask(h,tau,m)
        #La ventana es un arreglo de tamaño 2sventana + hueco
        # |sventana|hueco|sventana|
        sventana = int((len(ventana)-h)/2)#Elementos despues del centro
        #Inicio del indice que se movera la ventana sobre el arreglo
        
        #Se obtiene el indice de la posición inicial del hueco y un vector de tamaño 2sventana + hueco
        tmp = None
        PosIni = None
        while PosIni != False:
            indice = 0
            vmax = 100   #Valor frontera
            [v2, PosIni] = self.getEmpty(h,sventana) #Obtiene un vector que tenga aun hueco de tamaño h en funcion del tamaño del vector mascara y la ubicación del hueco
            print(PosIni)
            print("Vector a rellenar",v2)
        #Recorre los datos hasta antes de que haya un desvordamiento de datos
            while(indice < (self.dt['x_i'].size)-sventana+h):
            #Se verifica que el arreglo a comparar no tenga ningun elemento nan
                if self.dt.iloc[:,[1]][indice:indice+len(ventana)].isnull().values.any():
                #Si tiene un elemento nan se desplaza
                    indice += 1
                else:
                
                #Sino realiza la operación compara tamaños y se desplaza
                ##Revisa cómo sumar con pandas
                    v1 = np.array(self.dt.iloc[:,[1]][indice:indice+len(ventana)]).transpose()
                    res = v1-v2
                    res = res*ventana
                #No puedo operar con nan
                #Dado que los nan solo estaran en el hueco
                #res = np.sqrt(np.square(res).sum(axis = 1))
                    resi = np.sqrt(np.square(res[:,:sventana]))
                    resd = np.sqrt(np.square(res[:,sventana+h:]))
                    if resi < vmax and resd < vmax:
                        vmax = (resi+resd)/2
                        tmp = [indice,v1]
                        print("Cambio de vmax",vmax)
                        print("Mejor vector ahora",v1)
                    indice+=1

#Modificar la forma en que se guardan los archivos                    
            for i in range(len(ventana)):
                dtc['defNull'][PosIni + i] = 2
                
            for i in range(h):
                print(dtc['y_i'][PosIni + i])
                dtc['y_i'][PosIni + i] = v1[:,sventana+i]    
                print(dtc['y_i'][PosIni + i])
            self.dt.update(dtc)
            print("Archivo modificado")
        self.dt.to_csv('./CSVfiles/format_%s.csv'%self.name)
            #print(list(range(indice,indice+len(ventana))))
            #print(self.dt.iloc[:,[1]][indice:indice+len(ventana)])
            #print(self.dt['x_i'][indice+(self.dt['x_i'].size)-sventana:indice+h+(self.dt['x_i'].size)-sventana])

    def getEmpty(self,h,n):
        """Dado un conjunto de datos y un tamaño h, regresa un vector y un indice"""
        dh = pd.read_csv('./CSVfiles/hist_%s.csv'%self.name)#Lectura del histograma
        order = dh.sort_values(by=['Size']) #Ordenamiento al tamaño
        #print(dh.head())
        flag = False
        aux = None
        for item in order.index:
            #print('Item')
            #print(item)
            aux = dh.iloc[item]
            ##print(dh.iloc[item])
            if aux[2] == h:
                for i in range(aux[0],aux[1]+1):
                    ##print('GetEmpty')
                    ##print(self.dt['defNull'][i])
                    if self.dt['defNull'][i] == 0:
                        flag = True
                    else:
                        flag = False
                if flag:
                    #print(aux[0],aux[1])
                    return(np.array(self.dt['x_i'][aux[0] - n:aux[1]+n+1]).transpose(),aux[0])
            else:
                print("No hay huecos con ese tamaño")
                return (False,False)
                



############Run file

#cdmx = Data2Form()
#cdmx.read_csv('O3 CDMX 1986-2018 all sites.csv')
#cdmx.exp2csv('MER', n=1000)

#print("Lectura de los datos MER")
#cdmx_mer = R_format('MER')
#print("Relleno de los datos")
#cdmx_mer.Rellena()