import json
from ListaEnlazada import *
from Grafo import *
from Vertice import *


class ManejarJSON:
    def __init__(self):
        print("\033[0;32m" + "*** Loading JSON...***")

        with open("/Users/jehisond/PycharmProjects/TM2/tm.json") as archivoJSON:
            self.arbol = json.loads(archivoJSON.read())
            self.troncales = self.arbol["troncales"]
            self.rutas = self.arbol["rutas"]
            self.esquinas = []
            self.grafo = None

        print("*** JSON OK***")

    def leerTroncales(self):
        print("\033[0;32m" + "*** Reading JSON...***")
        print("\033[0;32m" + "*** Mapping Troncales...***")
        self.grafo = Grafo()
        self.diccionarioTroncales = {}

        for troncal in self.troncales:
            letra = troncal["letra"]
            nombre = troncal["nombre"]
            C1 = troncal["conexion1"]
            C2 = troncal["conexion2"]
            C3 = troncal["conexion3"]
            C4 = troncal["conexion4"]
            C5 = troncal["conexion5"]
            C6 = troncal["conexion6"]

            self.diccionarioTroncales[letra] = nombre

            self.grafo.agregarVertice(Vertice(letra))

            if C1 != "": self.esquinas.append(letra + C1)
            if C2 != "": self.esquinas.append(letra + C2)
            if C3 != "": self.esquinas.append(letra + C3)
            if C4 != "": self.esquinas.append(letra + C4)
            if C5 != "": self.esquinas.append(letra + C5)
            if C6 != "": self.esquinas.append(letra + C6)

        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
        for esquina in self.esquinas:
            self.grafo.agregarBorde(esquina[:1], esquina[1:])
        self.grafo.imprimirGrafo(self.diccionarioTroncales)
        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")

    def leerRutas(self):
        print("\033[0;32m" + "*** Reading JSON...***")
        print("\033[0;32m" + "*** Mapping Rutas...***")
        self.diccionarioRutas = {}

        for ruta in self.rutas:
            id = ruta["id"]
            ruta1 = ruta["ruta1"] + " - " + ruta["ruta2"]
            self.diccionarioRutas[id] = ruta1

    def imprimirRutas(self):
        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
        for key in self.diccionarioRutas:
            print("\033[1;37m   |     " + str(key) + " - " + self.diccionarioRutas[key])
        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")

    def leerRuta(self, idSeleccionado):
        print("\033[0;32m" + "*** Reading JSON...***")
        print("\033[0;32m" + "*** Mapping Rutas...***")
        self.tuplaRuta = ()

        for ruta in self.rutas:
            id = int(ruta["id"])
            if idSeleccionado is id:
                ruta1 = ruta["ruta1"]
                ruta2 = ruta["ruta2"]
                letra1 = ruta["letra1"]
                letra2 = ruta["letra2"]
                self.tuplaRuta = (id, ruta1, ruta2, letra1, letra2)
            else:
                # print("No se encontro el ID")
                pass

    def imprimirRuta(self):
        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\033[1;37m   | 1. De " + self.tuplaRuta[1] + " a " + self.tuplaRuta[2])
        print("\033[1;37m   | 2. De " + self.tuplaRuta[2] + " a " + self.tuplaRuta[1])
        print("\033[1;37m   " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")

    def obtenerTroncalOrigen(self, direccion):
        if direccion == "1":
            return self.tuplaRuta[3]
        else:
            return self.tuplaRuta[4]

    def obtenerTroncalDestino(self, direccion):
        if direccion == "1":
            return self.tuplaRuta[4]
        else:
            return self.tuplaRuta[3]

    def leerEstaciones(self, letra):
        print("\033[0;32m" + "*** Reading XML...***")
        print("*** Mapping estaciones...***")
        self.diccionarioEstaciones = {}
        nom = ""

        for troncal in self.troncales:
            if troncal["letra"] is letra:
                self.estaciones = troncal["estaciones"]
                for estaciones in self.estaciones:
                    self.diccionarioEstaciones[estaciones["id"]] = estaciones["nombre"]

    def imprimirEstaciones(self):
        print("\033[1;37m   " + "- - - - - - - - - - - - - - ")
        for key in self.diccionarioEstaciones:
            print("\033[1;37m   | " + str(key) + " - Estacion " + self.diccionarioEstaciones[key])
        print("\033[1;37m   " + "- - - - - - - - - - - - - - ")

    def imprimirEstacion(self, numero):
        return self.diccionarioEstaciones[numero]

    def cargarListaEstaciones(self, origen, destino, viaje):
        lista = ListaEnlazada()

        # print("viaje: ", viaje[2])

        if viaje[2] == '1':
            self.cargarEstaciones(origen, lista)
            self.cargarEstaciones(destino, lista)
            # print("ingreso 1")
            lista.imprimirLista(viaje)

        if viaje[2] == '2':
            self.cargarEstaciones(destino, lista)
            self.cargarEstaciones(origen, lista)
            # print("ingreso 2")
            lista.imprimirLista2(viaje)

    def cargarEstaciones(self, letra, lista):
        print("\033[0;32m" + "*** Reading XML...***")
        print("*** Listing estaciones...***")
        self.diccionarioEstaciones = {}
        nom = ""

        for troncal in self.troncales:
            if troncal["letra"] is letra:
                self.estaciones = troncal["estaciones"]
                for estaciones in self.estaciones:
                    id = estaciones["id"]
                    nombre = estaciones["nombre"]
                    latitud = estaciones["latitud"]
                    longitud = estaciones["longitud"]
                    tupla = (id, nombre, latitud, longitud)
                    lista.agregar(tupla)
