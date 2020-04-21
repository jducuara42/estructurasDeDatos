class tablaHash:
    def __init__(self):
        self.tam = 117
        self.tabla = [None] * self.tam;
        self.tablaAnidada = [[] for _ in range(self.tam)]

    def Hash(self, id):
        llave = 0
        for indice in range(0, len(id)):
            llave += ord(id[indice])
        return llave % self.tam

    def Hash2(self,id):
        return id % len(self.tabla)

    def insertar(self, id, valor):
        elementoHash = self.Hash2(id)

        if self.tabla[elementoHash] is None:
            self.tabla[elementoHash] = valor

    def buscar(self, id):
        elementoHash = self.Hash2(id)

        if self.tabla[elementoHash] is None:
            print("elemento no encontrado...")
            return None
        else:
            upz = self.tabla[elementoHash]
            print("\033[1;37m   | UPZ |" + " NUMERO: " + str(upz["numero"]) + " NOMBRE: " + upz["nombre"] + " HABITANTES: " + str(upz["habitantes"]))

            return self.tabla[elementoHash]
            #return hex(id(self.tabla[elementoHash]))

    def eliminar(self, valor):
        elementoHash = self.Hash2(valor)
        if self.tabla[elementoHash] is None:
            print("No se enconttreo el elemento...")
        else:
            self.tabla[elementoHash] is None
            print("Se elimino el elemento " + valor)