class Node:
     def __init__(self, value):
         self.value = value
         self.next = None

"0.2"


def recorrer(Nodo):
    if Nodo.next is None:
        print(Nodo.value)
        return
    else:
        print(Nodo.value)
        recorrer(Nodo.next)


def agregar(Nodo,x):
    if Nodo.next is None:
        Nodo.next = x(Node)
        return
    else:
        print(Nodo.value)
        return


h = Node("h")
o = Node("o")
l = Node("l")
a = Node("a")


h.next = o
o.next = l
l.next = a

recorrer(h)
agregar(h)

