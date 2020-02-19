
class Item():
  def __init__(self, obj):
    self.item = obj
    self.nxt = None

class ListDynamic(object):

  def __init__(self):
    self.head = None
    self.size = 0  

  def add_element(self, ele):
    new_item = Item(ele)
    if self.size == 0:
      self.head = new_item
    else:
      elem = self.head
      while(elem.nxt != None):
        elem = elem.nxt
      elem.nxt = new_item
    self.size += 1

  def remove_tail(self):
    item = self.head
    for i in range(self.size):
      if i == (lista.size - 2):
        #print("esta en el ultimo elemento",item.nxt)
        item.nxt = None
        self.size -= 1
      else:
        #print("else::: - ",item.nxt)
        previous = item.item
        item = item.nxt
    
  def remove_element(self, val):
    #print("valor: ",val);
    item = self.head
    val_pos = 0
    valBool = False

    for i in range(self.size):
      if item.item == (val):
        val_pos = i-1
        valBool = True
      item = item.nxt

    if (valBool):
      print("Si esta....", val_pos)

      item2 = self.head

      for k in range(self.size):
        if k == val_pos:
          siguiente = item2.nxt
        item2 = item2.nxt

      item3 = self.head

      j = 0
      while(j < self.size-1):
        if(j == (val_pos)):
          print("Es igual: ", val_pos - 1, j, item3.nxt, item3.item)
          item3.nxt = siguiente.nxt
          item3 = item3.nxt
          self.size -= 1
        else:
          print("Es diferente: ", val_pos - 1, j, item3.nxt, item3.item)
          item3 = item3.nxt
        j = j + 1
    else:
      print("El valor no esta en la lista")

  def print_list(self):
    item = self.head
    for i in range(self.size):
      print(item.item)
      item =  item.nxt

lista = ListDynamic()
lista.add_element(10)
lista.add_element(20)
lista.add_element(30)
lista.add_element(40)
lista.add_element(50)
lista.add_element(60)
lista.add_element(70)
lista.add_element(80)
lista.print_list()
print 'cantidad de elementos de la lista: ',lista.size
print("se va eliminar el ultimo elemento de la lista...")
lista.remove_tail()
lista.print_list()
print("Cantidad de elementos de la lista: ")
print(lista.size)
valorLista = int(input('ingrese el valor a buscar: '))
lista.remove_element(valorLista)
#lista.remove_element(30)
lista.print_list()
print 'cantidad de elementos de la lista: ',lista.size
lista.print_list()