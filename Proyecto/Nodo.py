class Nodo:
    def __init__(self, valor):
        self.id = valor[0]
        self.data = valor[1]
        self.latitud = valor[2]
        self.longitud = valor[3]
        self.siguiente = None
        self.anterior = None

    def getID(self):
        return self.id

    def getData(self):
        return self.data

    def getLatitud(self):
        return self.latitud

    def getLongitud(self):
        return self.longitud

    def getSiguiente(self):
        return self.siguiente

    def getAnterior(self):
        return self.anterior

    def setID(self, id):
        self.id = id

    def setData(self, valor):
        self.data = valor

    def setLatitud(self, latitud):
        self.latitud = latitud

    def setLongitud(self, longitud):
        self.longitud = longitud

    def setSiguiente(self, valor):
        self.siguiente = valor

    def setAnterior(self, valor):
        self.anterior = valor