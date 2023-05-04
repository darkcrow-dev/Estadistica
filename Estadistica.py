import numpy as np

class Estadistica:

    def __init__(self, datos):
        self.datos = datos

class Mediana(Estadistica):
    def __init__(self, datos):
        super().__init__(datos)

    def calcular(self):
        datosIniciales = np.array(datos)
        datosOrdenados = np.array(datos)
        mediana = int((len(datos) + 1)/2)

        for i in range(0, len(datosIniciales)):
            for j in range(0, len(datosIniciales) - 1):
                if(datosOrdenados[j] > datosOrdenados[j + 1]):
                    auxiliar = datosOrdenados[j]      
                    datosOrdenados[j] = datosOrdenados[j + 1]
                    datosOrdenados[j + 1] = auxiliar

        if( mediana % 2 == 0):
            datoCentral = ( datosOrdenados[int( (len(datosOrdenados) + 1)/2 ) - 1] + datosOrdenados[int( (len(datosOrdenados) + 1)/2 )] )/2
        else:
            datoCentral = datosOrdenados[int( (len(datosOrdenados) + 1)/2 ) - 1]

        print(f"Datos ingresados: {datosIniciales}")
        print(f"Datos ordenados: {datosOrdenados}")
        print(f"La mediana es: {datoCentral}")

class Media(Estadistica):
    def __init__(self, datos):
        super().__init__(datos)

    def calcular(self):
        datosIniciales = np.array(datos)
        sumaTotal = 0

        for i in range(0, len(datos)):
            sumaTotal += datos[i]

        mediaAritmetica = sumaTotal/len(datos)

        print(f"Datos ingresados: {datosIniciales}")
        print(f"La media es: {mediaAritmetica}")

datos = [3, 3, -1, 5, -5, 0, 0, -4, 12, 20, 11, -6, -1, 10, 1, 1, 1, 2, -2, -1, 5]

mediana = Mediana(datos)
media = Media(datos)
mediana.calcular()
media.calcular()
