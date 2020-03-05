class Nodo:
    def __init__(self, valor):
        self.data = valor
        self.siguiente = None

    def getData(self):
        return self.data

    def getSiguiente(self):
        return self.siguiente

    def setData(self, valor):
        self.data = valor

    def setSiguiente(self, valor):
        self.siguiente = valor

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def vacio(self):
        return self.cabeza is None

    def agregar(self, item):
        nuevoNodo = Nodo(item)
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


    def imprimirLista(self):
        nodoActual = self.cabeza

        while nodoActual is not None:
            print(nodoActual.getData())
            nodoActual = nodoActual.getSiguiente()

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregarCola(0)
lista.imprimirLista()
