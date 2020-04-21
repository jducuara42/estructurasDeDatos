from Vertice import *

class Grafo(object):
 vertices = {}

 def agregarVertice(self, vertice):
  if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
   self.vertices[vertice.nombre] = vertice
   return True
  else:
   return False

 def agregarBorde(self, u, v):
  if u in self.vertices and v in self.vertices:
   self.vertices[u].agregarVecino(v)
   self.vertices[v].agregarVecino(u)
   return True
  else:
   return False

 def imprimirGrafo(self, diccionarioTroncales):
  for key in sorted(list(self.vertices.keys())):
   print("\033[1;37m   |     " + key + " - " + diccionarioTroncales[key] + ": " +  str(self.vertices[key].vecinos))