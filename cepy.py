##################################
#   Ariel Ceron Gonzalez
#   Servicio Social
#   Queretaro, 2020
#
################################
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 
import math as mt 
from numpy import linalg as LA
import random
from sortedcontainers import SortedList
from lorenz import generateLorenz


############Objetos

class AnalisisDatos(object):

    def __init__(self, data:list, time:list, name:str, vector = [0.6,0.2,0.2]):
        ##Quiero poner un error en la creación para que no se pueda creae el objeto
        if self.__checkdata__(data,time):
            self.dt = data
            self.index = time
            self.id = name
            self.len = len(data)
            self.size = self.__sizeof__()
            self.S = [round(v*len(data)) for v in vector]
            if not sum(self.S) == self.len:
                self.S[-1] += self.len - sum(self.S)
            #Aquí voy a almacenar todo
            self.dicc = {}
        else:
            pass
            #Revisar TypeError __init__()
            #Revisar destroy myself (existe)?
        
    def __sizeof__(self,data:list = None) -> list:
        """
            Regresa el tamaño de dos conjuntos, el de datos y el de huecos.

            Dada una lista de datos cuenta la cantidad de elementos que son nan y los que no. Regresa una tupla de números que representa el tamaño de estos conjuntos.

            Parameter
            -----------
        o-------
            

            Salidas
            -------
            sdt: int
                Un número entero que representa la cantidad de elementos que no son NAN
            snan: int
                Un número entero que representa la cantidad de elementos que son NAN

            Ejemplo
            ------
                >>> datos = [1,2,3,np.nan]
                >>> fechas = [i for i in range(len(datos))]
                >>> objeto = AnalisisDatos(datos,fechas)
                >>> print(objeto.size)
                >>> [3,1]
        """
        snan = 0
        sdt = 0

        if data == None:
            data = self.dt

        for valor in data:
            if np.isnan(valor):
                snan += 1
            else:
                sdt += 1
        return([sdt,snan])     

    def __checkdata__(self,data:list,time:list):
        """
            Verifica los datos de entrada.

            Los datos de entrada deben ser estructuras tipo lista, por lo que la función checa dos condiciones: 
                1) Que los datos sean listas
                2) Que las listas sean del mismo tamaño
            Si se cumplen ambas condiciones entonces se retorna un booleano verdadero.

            Parameter
            -----------
            data:list
                Lista de datos
            time:list
                Lista de fechas
                
            Salidas
            -------
            bool:
                Regresa un booleano, si cumple las condiciones será verdadero, falso en otro caso

            Ejemplo
            -------
                >>> datos = [1,2,3,np.nan]
                >>> fechas = [i for i in range(len(datos-1))]
                >>> objeto = AnalisisDatos(datos,fechas,'Nombre')
                >>> El tamaño de los datos debe coincidir
        """
        if type(data) == list:
            if len(data) == len(time):
                return True
            else:
                print("El tamaño de los datos debe coincidir")
                return False
        else:
            print("Tipo de dato no valido, solo se aceptan listas")
            return False
    
    def __sizedic__(self,data:list = None)->list:
        """
            Función auxiliar para crear un histograma.

            Regresa dos diccionarios relacionados a la cantidad y posición de datos y huecos. Para ambos la key es el tamaño del continuo y el dato es la lista de las posiciones.

            Salida
            ------
            list
                En la primera posición se encuentra una lista 
        """
        #Reglas para terminar el programa
        if data == None:
            dt = self.dt
            lenght = self.len
        else:
            if type(data) == list:
                dt = data
                lenght = len(data)
            else:
                return(False)
        if lenght == 0:
            return False
        else:
            flag = False #True for nan
            cnan = 0; Mnan = 0
            cdt = 0;  Mdt = 0
            indexdt = {}
            indexnan = {}

            for i in range(lenght):
                if np.isnan(dt[i]):
                    cnan += 1
                    if not flag:
                        try:
                            indexdt[cdt] += [i-(cdt)]
                        except:
                            indexdt[cdt] = [i-(cdt)]
                        if cdt > Mdt:
                            Mdt = cdt
                        cdt = 0
                        flag = True
                else:
                    cdt += 1
                    if flag:
                        try:
                            indexnan[cnan] += [i-(cnan)]
                        except:
                            indexnan[cnan] = [i-(cnan)]
                        if cnan > Mnan:
                            Mnan = cnan112.0,

                        cnan = 0
                        flag = False
            if cnan > 0:
                try:
                    indexnan[cnan] += [lenght - cnan]
                except:
                    indexnan[cnan] = [lenght - cnan]
                if cnan > Mnan:
                    Mnan = cnan
            if cdt > 0:
                try:
                    indexdt[cdt] += [lenght - cdt]
                except:
                    indexdt[cdt] = [lenght - cdt]
                if cdt > Mdt:
                    Mdt = cdt
            return([indexnan,indexdt])

    def histograma(self, tipo:str, data:list = None, bins:int = 50,savefig:bool=False):
        """
            Crea un histograma
        """
        labels = ["Huecos","Datos"]
        colors = ["red","green"]

        if tipo == 'h':
            dic = self.__sizedic__(data)[0]
            slc = 0
            if not dic:
                return False
        elif tipo == 'd':
            dic = self.__sizedic__(data)[1]
            slc = 1
            if not dic:
                return False
        else:
            return False

        #Ordenamos los tamaños
        x = sorted(list(dic.keys()))
        altura = []
        #Medimos la frecuencia de aparición
        for k in x:
            altura.append(len(dic[k]))
        if len(altura) < 50:
            bins = len(altura)

        #Imprimimos el histograma
        plt.figure(figsize=(10,10))
        plt.bar(x[:bins],altura[:bins],color=colors[slc])
        plt.title("Histograma de {}".format(labels[slc]))
        plt.xlabel("Tamaño")
        plt.grid()
        plt.ylabel("Frecuencia")
        if savefig:
            plt.savefig("hist_{}_{}.png".format(tipo,self.id)) 
        plt.show()
        
        return(x,altura)

    def genera_huecos(self,randt:list,randnan:list)->list:
        """
            Genera una lista de huecos

            A la entrada un vector formado con una función de distribución de probabilidad, a la salida huecos aleatorios que comparten la misma función.

            Input:
            ------
                randt:list
                    Lista con valores aleaotrios, relacionados con la función de distribución de los datos
                randnan: list
                    Lista con valores aleaotrios, relacionados con la función de distribución de los huecos
            Output:
            -------
            list:
                Lista de huecos de tamaño len(datos).

            Example:
            -------
                >>> denH = [1,3,5]
                >>> denD = [4,2,3]
                >>> nuevaCol = prueba.genera_huecos(denH,denD)
                >>> 
        """
        print("Generando huecos...")
        ini = round(random.random())
        
        if ini:
            lini = randnan
            lfin = randt
        else:
            lini = randt
            lfin = randnan

        laux = []
        ii = fi = 0
        flag = True
        prc = 0

        while(len(laux) <= self.len):
            if ii >= len(lini):
                ii = 0
            if fi >= len(lfin):
                fi = 0
            #print("{:.0f}% de avance".format((len(laux)/self.len)*100))
            #Creamos tantos datos como como lo permita el vector de entrada
            if flag:
                aux = [True for i in range(lini[ii])]
                laux.extend(aux)
                #Nos movemos en el vector y cambiamos de distribución
                ii += 1
                flag = False
            else:
                aux = [np.nan for i in range(lfin[fi])]
                laux.extend(aux)
                #Nos movemos en el vector y cambiamos de distribución
                fi += 1
                flag = True
        #Como salida un vector tan grande como el tamaño de los datos de entrada
        print("Huecos generados")
        return(laux[:self.len])

    def describe(self,data:list = None, nombre:str = "Null", savefig:bool = False) -> set:
        """
            Imprime un resumen de los datos de entrada
        """
        if data == None:
            data = self.dt
            size = self.size
        else:
            size = self.__sizeof__(data)
        
                
        print("--------------------------------------")
        print("----------ANÁLISIS DE DATOS-----------")
        print("")
        print("Nombre de la serie: ",self.id)
        print("Tamaño de la serie: ",self.len)
        print("---- {}-- {} ----".format(self.index[0],self.index[-1]))
        print("Cantidad de datos nulos:",self.size[1])
        print("Cantidad de datos no nulos:",self.size[0])
        print("")
        
        plt.figure(figsize=(10,10))
        plt.pie([size[0],size[1]],explode=(0.0,0.2),labels=["Datos","Huecos"],colors=['green','red'],autopct='%1.1f%%')
        plt.title("Relación de datos")
        plt.axis('equal')
        if savefig:
            plt.savefig("pie_{}.png".format(self.id))
        plt.show()

        datos = self.histograma('d',data=data,savefig=savefig)
        huecos = self.histograma('h',data=data,savefig=savefig)

        return(self.size,datos,huecos)

    def obtener(self,nombre:str):
        """
            Regresa el vector asociado al nobre
        """
        try:
            return(self.dicc[nombre])
        except:
            print("Error: Revisa el nombre")
            return(False)

    def añadir(self, nombre:str, datos:str):
        """
            Añade una columna al objeto teniendo como identificador al nombre y de contenido a datos. Se permite que los datos ingresados no sean del mismo tamaño que los ingresados.
        """
        self.dicc[nombre] = datos

    def guardar(self,nombre:str = 'None'):
        """
            Una vez terminado de usar el objeto puede ser almacenado en un csv que llevará como nombre el parámtero de inicio al crear el objeto.
        """
        if nombre == 'None':
            csv_file = "{}.csv".format(self.id)
        else:
            csv_file = nombre

        encabezados = ['Fechas','Datos','S']
        
        try:
            for encabezado in self.dicc.keys():
                encabezados.append(encabezado)
        except:
            pass

        S = []
        for i in range(len(self.S)):
            if i == 1:
                for i in range(self.S[i]):
                    S.append('E')
            elif i == 2:
                for i in range(self.S[i]):
                    S.append('P')
            else:
                for i in range(self.S[i]):
                    S.append('V')

        contenidos = [self.index, self.dt, S]
        try:
            for contenido in self.dicc.keys():
                contenidos.append(self.dicc[contenido])
        except:
            pass

        dict_data = dict(zip(encabezados,contenidos))
        df = pd.DataFrame(dict_data)
        df.to_csv(csv_file,index=False)

###########Funciones

def mascara(h:int,tau:int,m:int)->list:
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

def kvecinos(objeto:object, h:int,m:int,tau:int,k:int,S:str='E',genera_huecos:bool = True,dist:list=[]):    
    """
        Genera una lista de datos
    """
    #Obtenemos los límites de los datos
    if S == 'E':
        #S = objeto.S[0]
        S1 = 0
        S2 = objeto.S[0]
    elif S == 'P':
        S1 = objeto.S[0]
        S2 = objeto.S[1]
    elif S == 'V':
        S1 = objeto.S[1]
        S2 = objeto.S[2]
    else:
        print("Conjunto no valido")
        return(False)

    #Revisamos si hay datos de entrada, sino asignamos unos propios
    if genera_huecos:
        if not dist:
            dist = [[1,2,3],[1,2,3]]
        else:
            if len(dist) != 2:
                print("Error en la entrada de las distribuciones de los huecos")
                return(False)
        #Obtenemos una lista de huecos artificiales
        huecos = objeto.genera_huecos(dist[0],dist[1])[S1:S2]
    else:
        #Obtenemos los huecos propios de los datos
        huecos = objeto.dt[S1:S2]

    #Obtenemos los indices de los huecos tamaño h
    try:
        huecos_idx = objeto.__sizedic__(huecos)[0][h]
        #print("huecos:",huecos_idx)
    except KeyError:
        print("Hueco tamaño %i no encontrado"%h)
        return False
    
    #Generamos algunas variables de ayuda
    datos = objeto.dt[S1:S2]
    msk = mascara(h,tau,m)
    #print(msk)
    msk_idx = np.where(np.asarray(msk[0]) == True)[0]
    dis = SortedList()
    resultados = {}

    #Inicia el algoritmo de reconstrucción
    #_i es la posición (indice) de los huecos tamaño h
    for _i in huecos_idx:
        if _i < msk[1]:
            #Son los primeros casos, cuando el vector de reconstrucción no se puede formar completamente
            pass
        else:
            #Caso general
            v1 = datos[_i - msk[1]: _i + msk[1] + h]
            dis.clear()
            #print(v1)
            #print(v1[:msk[1]],v1[msk[1]:msk[1] + h],v1[msk[1]+h:])
            #Verificamos que no haya nan en las posiciones que usaremos para medir
            aux = [v1[i] for i in msk_idx]
            if not any(np.isnan(aux)): #Si ninguno es nan
                #Iniciamos la comparacion en los datos
                for _j in range(msk[1],len(datos)-msk[1]-h):
                    #Excluimos el vector que tiene como centro la posición del hueco que estamos reconstruyendo
                    if _j == _i:
                        continue
                    #Creamos dos vectores auxiliares
                    v2 = datos[_j - msk[1]:_j + msk[1] + h]
                    v3 = huecos[_j - msk[1]:_j + msk[1] + h]
                    #Verifica que no haya nan en los datos reales y en los hueco artificiales
                    aux = [v2[i]*v3[i] for i in msk_idx]
                    if not any(np.isnan(aux)): #Si ninguno es nan
                        #Verificamos que haya datos en los huecos
                        aux = [v2[msk[1] + i] for i in range(h)]
                        if not any(np.isnan(aux)): #Si ninguno es nan
                            #Calcula la distancia euclindiana
                            aux = [abs(v1[i] - v2[i]) for i in msk_idx]
                            aux = sum(aux)
                            dis.add([aux,_j])
                        else:
                            continue
                    else:
                        continue
            #Terminas de comparar en todos los datos y empezamos a obtener el vector de recconstruccion
                if len(dis) == 1:
                    #Cuando solo hay un elemento
                    resultados[_i] = [datos[dis[0][1]:dis[0][1] + h],datos[_i:_i + h]]
                elif dis != []:
                    #print("i:",_i)
                    #print("distancia:",dis)
                    aux = [0 for i in range(h)]
                    valRe = []
                    for j in range(k):
                        aux = [aux[i] + datos[i + dis[j][1]] for i in range(h)]
                    #    print([aux[i] + datos[i + dis[j][1]] for i in range(h)])
                    aux = [aux[i]/k for i in range(len(aux))]
                    valRe = datos[_i:_i + h]
                    
                    #print("res (aux):", aux)
                    #print("res (valRe):", valRe)
                    resultados[_i] = [aux,valRe]
            else:
                continue
    return(resultados)




###########Implementaciones
#if __name__ == '__main__':
    #data = [0,1,2,3,np.nan,np.nan,6,7,np.nan,9,10,11,12,np.nan,np.nan,np.nan,np.nan,16,17,18,19,np.nan,21,22,23,24,25,26,27,28,29,30,np.nan,32]
    #date = ['01/01/1986 01:00:00' for i in range(len(data))]
    #n = 100
    #data = generateLorenz(n).tolist()
    #db = pd.read_csv("fCDMX.csv")
    #date = db.date.tolist()[:1000]
    #data = db.MER.tolist()[:1000]
    #Lista de fechas
    #date = ['01/01/1986 01:00:00' for i in range(n)]
    #r = AnalisisDatos(data,date,"Prueba")
    #dic = r.__sizedic__()[0]
    #print(r.genera_huecos([1,2,3,4],[1,2,3,4]))
    #r.describe()
    #h = 2
    #m = 1
    #tau = 1
    #k = 1
    #print("R: ",kvecinos(r,h,m,tau,k,S ='E',dist=[[1,2,3],[1,2,3]]))