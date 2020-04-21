import json
from tablaHash import *

class manejarJSON_UPZ:
    def __init__(self):
        print("\033[0;32m" + "*** Loading JSON UPZ...***")

        with open("/Users/jehisond/PycharmProjects/TM2/UPZ.json") as archivoJSON:
            self.arbol = json.loads(archivoJSON.read())
            self.UPZs = self.arbol["UPZs"]
        print("*** JSON UPZ OK***")

    def leerUPZ(self):
        print("\033[0;32m" + "*** Reading JSON UPZ...***")
        print("\033[0;32m" + "*** Mapping UPZ...***")
        tabla_Hash = tablaHash()

        for UPZ in self.UPZs:
            tabla_Hash.insertar(UPZ["numero"], UPZ)

        return tabla_Hash

    def buscarUPZ(self, id, tabla_Hash):
        print("\033[0;32m" + "*** searching UPZ...***")
        tabla_Hash.buscar(id)