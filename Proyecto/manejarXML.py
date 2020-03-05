from xml.dom import minidom
from ListaEnlazada import *

class ManejarXML:
    def __init__(self):
        print("\033[0;32m" + "*** Loading XML...***")
        self.arbol = minidom.parse("/Users/jehisond/PycharmProjects/TM/tm.xml")
        self.troncales = self.arbol.getElementsByTagName("troncal")
        self.rutas = self.arbol.getElementsByTagName("rutas")
        print("*** XML OK***")

    def leerTroncales(self):
        print("*** Reading XML...***")
        print("*** Mapping troncales...***")
        self.diccionarioTroncales = {}

        for troncal in self.troncales:
            self.diccionarioTroncales[troncal.getAttribute("letra")] = troncal.getAttribute("nombre")
            cantidadEstaciones = troncal.getElementsByTagName("cantidadEstaciones")[0]
            #print("cant: " + cantidadEstaciones.firstChild.data)

    def leerRutas(self):
        print("\033[0;32m" + "*** Reading XML...***")
        print("\033[0;32m" + "*** Mapping Rutas...***")
        self.diccionarioRutas = {}

        for ruta in self.rutas:
            #self.diccionarioTroncales[ruta.getAttribute("letra")] = ruta.getAttribute("nombre")
            id = ruta.getElementsByTagName("id")[0].firstChild.data
            ruta1 = ruta.getElementsByTagName("ruta1")[0].firstChild.data + " - " + ruta.getElementsByTagName("ruta2")[0].firstChild.data
            letra1 = ruta.getElementsByTagName("letra1")[0].firstChild.data
            letra2 = ruta.getElementsByTagName("letra2")[0].firstChild.data
            #print("id: " + id + " ruta1: " + ruta1 + " - ruta2: " + ruta2)
            self.diccionarioRutas[id] = ruta1

    def leerRuta(self, idSeleccionado):
        print("\033[0;32m" + "*** Reading XML...***")
        print("\033[0;32m" + "*** Mapping Rutas...***")
        self.tuplaRuta = ()

        for ruta in self.rutas:
            id = ruta.getElementsByTagName("id")[0].firstChild.data
            if idSeleccionado is id:
                ruta1 = ruta.getElementsByTagName("ruta1")[0].firstChild.data
                ruta2 = ruta.getElementsByTagName("ruta2")[0].firstChild.data
                letra1 = ruta.getElementsByTagName("letra1")[0].firstChild.data
                letra2 = ruta.getElementsByTagName("letra2")[0].firstChild.data
                self.tuplaRuta = (id, ruta1, ruta2, letra1, letra2)
            else:
                #print("No se encontro el ID")
                pass

    def obtenerTroncalOrigen(self,direccion):
        if direccion == 1:
            return self.tuplaRuta[3]
        else:
            return self.tuplaRuta[4]

    def obtenerTroncalDestino(self,direccion):
        if direccion == 1:
            return self.tuplaRuta[4]
        else:
            return self.tuplaRuta[3]


    def leerEstaciones(self, letra):
        print("\033[0;32m" + "*** Reading XML...***")
        print("*** Mapping estaciones...***")
        self.diccionarioEstaciones = {}
        nom = ""

        for troncal in self.troncales:
            if troncal.getAttribute("letra") is letra:
                self.estaciones = troncal.getElementsByTagName("estaciones")
                for estaciones in self.estaciones:
                    self.estacion = estaciones.getElementsByTagName("estacion")
                    for estacion in self.estacion:
                        self.diccionarioEstaciones[estacion.getElementsByTagName("id")[0].firstChild.data] = estacion.getElementsByTagName("nombre")[0].firstChild.data

    def imprimirTroncales(self):
        print("\033[1;37m " + "- - - - - - - - - - - - - - ")
        for key in self.diccionarioTroncales:
            print("\033[1;37m | " + key + " - Troncal " + self.diccionarioTroncales[key])
        print("\033[1;37m " + "- - - - - - - - - - - - - - ")

    def imprimirEstaciones(self):
        print("\033[1;37m " + "- - - - - - - - - - - - - - ")
        for key in self.diccionarioEstaciones:
            print("\033[1;37m | " + key + " - Estacion " + self.diccionarioEstaciones[key])
        print("\033[1;37m " + "- - - - - - - - - - - - - - ")

    def imprimirRutas(self):
        print("\033[1;37m " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
        for key in self.diccionarioRutas:
            print("\033[1;37m | " + key + " - " + self.diccionarioRutas[key])
        print("\033[1;37m " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")

    def imprimirRuta(self):
        print("\033[1;37m " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\033[1;37m | 1. " + self.tuplaRuta[1] + " a " + self.tuplaRuta[2])
        print("\033[1;37m | 2. " + self.tuplaRuta[2] + " a " + self.tuplaRuta[1])
        print("\033[1;37m " + "- - - - - - - - - - - - - - - - - - - - - - - - - -")

    def imprimirTroncal(self, letra):
        return self.diccionarioTroncales[letra]

    def imprimirEstacion(self, numero):
        return self.diccionarioEstaciones[numero]

    def cargarListaEstaciones(self,origen, destino):
        lista = ListaEnlazada()
        self.cargarEstaciones(origen, lista)
        self.cargarEstaciones(destino, lista)
        lista.imprimirLista()

    def cargarEstaciones(self, letra, lista):
        print("\033[0;32m" + "*** Reading XML...***")
        print("*** Listing estaciones...***")
        self.diccionarioEstaciones = {}
        nom = ""

        for troncal in self.troncales:
            if troncal.getAttribute("letra") is letra:
                self.estaciones = troncal.getElementsByTagName("estaciones")
                for estaciones in self.estaciones:
                    self.estacion = estaciones.getElementsByTagName("estacion")
                    for estacion in self.estacion:
                        id = estacion.getElementsByTagName("id")[0].firstChild.data
                        nombre = estacion.getElementsByTagName("nombre")[0].firstChild.data
                        latitud = estacion.getElementsByTagName("latitud")[0].firstChild.data
                        longitud = estacion.getElementsByTagName("longitud")[0].firstChild.data
                        tupla = (id, nombre, latitud, longitud)
                        lista.agregar(tupla)
                        #print(nombre)

    def mostrarListaEstaciones(self):
        lista = ListaEnlazada()
        lista.imprimirLista2()