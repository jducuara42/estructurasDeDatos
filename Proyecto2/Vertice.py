class Vertice(object):

 def __init__(self, n):
  self.nombre = n
  self.vecinos = list()

 def agregarVecino(self, v):
  if v not in self.vecinos:
   self.vecinos.append(v)
   self.vecinos.sort()