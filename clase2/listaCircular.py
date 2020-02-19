class Item:
    def __init__(self, obj):
        self.item = obj
        self.nxt = None

class ListCircular(object):

    def __init__(self, head):
        self.head = head
        self.size = 0
        self.head.nxt = head
        self.size += 1

    def add_element(self, ele):
        #print("E-Pos: ", ele, self.size)
        i = 1
        elem = self.head
        while i < self.size:
            i += 1
            prev = elem
            elem = elem.nxt
        element = elem
        ele.nxt = element.nxt
        element.nxt = ele
        self.size += 1

    def remove_element(self, val):
        if val < 0:
            print("Valor fuera del rango...")
        else:
            if val > 1:
                #print("I-p: ", val-1)

                j = 1
                elem = self.head
                while j < val-1:
                    j += 1
                    prev = elem
                    elem = elem.nxt
                prev = elem
            else:
                #print("E-p: ", val-1)

                elem = self.head
                while elem.nxt !=self.head:
                    pre = elem
                    elem = elem.nxt

                prev = elem
                self.head = prev.nxt.nxt
            prev.nxt = prev.nxt.nxt

    def print_list(self):
        item = self.head
        for i in range(self.size-1):
            print(item.item, item.nxt)
            #print(item.item)
            item =  item.nxt

item = Item(1)
listaC = ListCircular(item)
item = Item(2)
listaC.add_element(item)
item = Item(3)
listaC.add_element(item)
item = Item(4)
listaC.add_element(item)
item = Item(5)
listaC.add_element(item)
item = Item(6)
listaC.add_element(item)
listaC.print_list()
print 'cantidad de elementos de la lista: ',listaC.size
print("se va eliminar el 3o elemento de la lista...")
listaC.remove_element(3)
listaC.print_list()
print 'cantidad de elementos de la lista: ',listaC.size