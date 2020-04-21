from math import *
from Nodo import *

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.latitudAnterior = 0
        self.longitudAnterior = 0
        self.latitudActual = 0
        self.longitudActual = 0
        self.distancia = 0
        self.distanciaTotal = 0

    def vacio(self):
        return self.cabeza is None

    def agregar(self, item):
        nuevoNodo = Nodo(item)

        if self.cabeza is None:
            self.cabeza = nuevoNodo
            self.cola = self.cabeza
        else:
            nuevoNodo.setAnterior(self.cola)
            self.cola.setSiguiente(nuevoNodo)
            self.cola = nuevoNodo

    def agregarCabeza(self, item):
        nuevoNodo = Nodo(item)

        self.cabeza.setAnterior(nuevoNodo)
        nuevoNodo.setSiguiente(self.cabeza)
        self.cabeza = nuevoNodo

    def size(self):
        contador = 0
        nodoActual = self.cabeza

        while nodoActual is not None:
            contador = contador + 1
            nodoActual = nodoActual.getSiguiente()
        return contador

    def buscar(self, item):
        nodoActual = self.cabeza
        encontrar = False

        while nodoActual is not None and not encontrar:
            if nodoActual.gerData() is item:
                encontrar = True
            else:
                nodoActual = nodoActual.getSiguiente()
        return encontrar

    def eliminar(self, item):
        nodoActual = self.cabeza
        nodoPrevio = None
        encontrar = False

        while nodoActual is not None and not encontrado:
            if nodoActual.getData() is item:
                encontrar = True
            else:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.getSiguiente()

        if encontrar is True:
            if nodoPrevio is None:
                self.cabeza = nodoActual.getSiguiente()
            else:
                nodoPrevio.setSiguiente(nodoActual.getSiguiente())
        else:
            raise ValueError
            print("Valor no encontrado :/")

    def insertar(self, posicion, item):
        if posicion > self .size() - 1:
            raise IndexError
        print("Indice fuera de rango...")

        nodoActual = self.cabeza
        nodoPrevio = None
        pos = 0

        if posicion == 0:
            self.agregar(item)
        else:
            nuevoNodo = Nodo(item)

            while pos < posicion:
                pos = pos + 1
                nodoPrevio = nodoActual
                nodoActual = nodoActual.getSiguiente()

            nodoPrevio.setSiguiente(nuevoNodo)
            nuevoNodo.setSiguiente(nodoActual)

    def index(self, item):
        nodoActual = self.cabeza
        posicion = 0
        encontrar = False

        while nodoActual is not None and not encontrar:
            if nodoActual.getData is item:
                encontrar = True
            else:
                nodoActual = nodoActual.getSiguiente()
                posicion += 1

        if encontrar is True:
            pass
        else:
            posicion = None

        return pos

    def agregarCola(self, item):
        nodoActual = self.cabeza
        nodoPrevio = None
        posicion = 0
        tamano = self.size()

        while posicion < tamano:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.getSiguiente()
            posicion += 1

        nuevoNodo = Nodo(item)
        if nodoPrevio is None:
            nuevoNodo.setSiguiente(nodoActual)
            self.cabeza = nuevoNodo
        else:
            nodoPrevio.setSiguiente(nuevoNodo)


    def imprimirLista(self, viaje):
        nodoActual = self.cabeza
        iniciarViaje = False
        contador = 0

        while nodoActual is not None:
            if(int(viaje[0]) is int(nodoActual.getID())):
                iniciarViaje = True

            if(iniciarViaje):
                latitud = nodoActual.getLatitud()
                longitud = nodoActual.getLongitud()

                if contador > 0:
                    self.latitudAnterior = self.latitudActual
                    self.longitudAnterior = self.longitudActual
                    self.latitudActual = latitud
                    self.longitudActual = longitud
                    self.distancia = self.hallarDistancia(float(self.latitudAnterior), float(self.longitudAnterior), float(self.latitudActual), float(self.longitudActual))
                else:
                    self.latitudActual = latitud
                    self.longitudActual = longitud
                print("\033[0;37m   " + nodoActual.getData(), "   --> ditancia recorrida: {0:.1f}m".format(self.distancia))
                self.distanciaTotal += self.distancia
                contador += 1

            if(int(viaje[1]) == int(nodoActual.getID())):
                iniciarViaje = False

            nodoActual = nodoActual.getSiguiente()
        print("\033[0;31m " + "Distancia total recorrida: {0:.1f} km".format(self.distanciaTotal / 1000))

    def imprimirLista2(self, viaje):
        nodoActual = self.cola
        iniciarViaje = False
        contador = 0

        while nodoActual is not None:
            #print("viaje[0]: " + viaje[0] +" viaje[1]: " + viaje[1] + " - DATA: " + nodoActual.getID())

            if (int(viaje[0]) == int(nodoActual.getID())):
                iniciarViaje = True
            if (iniciarViaje):
                latitud = nodoActual.getLatitud()
                longitud = nodoActual.getLongitud()

                if contador > 0:
                    self.latitudAnterior = self.latitudActual
                    self.longitudAnterior = self.longitudActual
                    self.latitudActual = latitud
                    self.longitudActual = longitud
                    self.distancia = self.hallarDistancia(float(self.latitudAnterior), float(self.longitudAnterior), float(self.latitudActual), float(self.longitudActual))
                else:
                    self.latitudActual = latitud
                    self.longitudActual = longitud
                print("\033[0;37m   " + nodoActual.getData(), "   --> ditancia recorrida: {0:.1f}m".format(self.distancia))
                self.distanciaTotal += self.distancia
                contador += 1

            if (int(viaje[1]) == int(nodoActual.getID())):
                iniciarViaje = False

            nodoActual = nodoActual.getAnterior()
        print("\033[0;31m " + "Distancia total recorrida: {0:.1f} km".format(self.distanciaTotal/1000))

    def hallarDistancia(self,lat2, lon2, lat1, lon1):
        """
        print("lat2: ", lat2, " lat1: ", lat1)
        print("lon2: ", lon2, " lon1: ", lon1)
        """
        lat2, lon2, lat1, lon1 = map(radians, [lat2, lon2, lat1, lon1])
        latitudTotal = lat2 - lat1
        lontitudTotal = lon2 - lon1

        resultado = (sin(latitudTotal/2)**2 + cos(lat1) * cos(lat2) * sin(lontitudTotal/2)**2)
        resultadoFinal = (2 * 6367 * atan(sqrt(resultado)))*1000
        return resultadoFinal
        #print("{0:.2f} metros".format(resultadoFinal))