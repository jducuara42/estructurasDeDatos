#####################################################################################
# CODIGO BASADO DE: Lars Nieradzik, L. N. (2019, 27 julio).
# Wavelet Trees and full-text search indices.
# Recuperado 1 abril, 2020, de https://lars76.github.io/various/wavelet-trees-python/
######################################################################################



class Nodo(object):
    def __init__(self):
        self.valor = [0]
        self.izquierda = None
        self.derecha = None

class arbolWavelet(object):
    def __init__(self, vector, alphabet_size):
        self.raiz = Nodo()
        self.Wavelet(0, alphabet_size, vector, self.raiz)

    def Wavelet(self, inicio, final, vector, nodo):
        media = (inicio + final) // 2
        #print("Media: ", media, " inicio: ", inicio, " final: ", final)
        s = 0
        izquierda = []
        derecha = []

        for elemento in vector:
            if elemento <= media:
                s = s + 1
                izquierda.append(elemento)
            else:
                derecha.append(elemento)
            nodo.valor.append(s)

        #print("media: ", media, " izq: ", izquierda, " - der: ", derecha)
        print("izq: ", izquierda, " - der: ", derecha)

        if (inicio == final):
            #print("Nodo hoja")
            print("")
            return nodo

        nodo.izquierda = self.Wavelet(inicio, media, izquierda, Nodo())
        nodo.derecha = self.Wavelet(media+1, final, derecha, Nodo())

        return nodo

    def rango(self, final1, final2, node, out, length):
        if not node or not node.izquierda or not node.derecha:
            out[length] = final2 - final1
            return length+1

        length = self.rango(node.valor[final1], node.valor[final2], node.izquierda, out, length)
        length = self.rango(final1 - node.valor[final1], final2 - node.valor[final2], node.derecha, out, length)

        return length

vectorOriginal = [3,1,9,1,2,0,7,5,4,8,9,4,3,7,5,9,2,7,1,5,1,3]
print(vectorOriginal)
vectorOrdenado = sorted(set(vectorOriginal))
inicioElemento = vectorOrdenado[0]
finalElemento = vectorOrdenado[-1]
#media = (finalElemento + inicioElemento) // 2
sigma =  finalElemento - inicioElemento
tamano = len(vectorOriginal)
intervalo = (0, len(vectorOriginal) - 1)

print("elemento menor: ", inicioElemento)
print("elemento mayor: ", finalElemento)
print("sigma: ", sigma)
print("tamano: ", tamano)
objWT = arbolWavelet(vectorOriginal, sigma)
out = [0] * (sigma + 1)
objWT.rango(intervalo[0], intervalo[1], objWT.raiz, out, 0)
print("Rango: ", [(i, x) for i, x in enumerate(out)])