class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None

    def __str__(self):
        return str(self.value)


n1 = Node(4)
n2 = Node(10)
n3 = Node(50)

n1.next = n2
n2.next = n3



class LinkedList:
    def __init__(self):
        self.head: Node = None

    def preppend(self, e):  # Agregar al principio
        nuevo_nodo = Node(e)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def append(self, e):  # Agregar al final
        if self.head is None:
            self.head = Node(e)
            return
        nodo_actual = self.head

        while nodo_actual is not None:
            if nodo_actual.next is None:
                nodo_actual.next = Node(e)
                return
            nodo_actual = nodo_actual.next

    def travel(self):  # Recorrer la lista enlazada
        pass

    def get_size(self):  # Obtener tamaño de la lista enlazada
        pass

    def search_element(self, e): # Buscar un elemento en una lista enlazada
        pass


    def compare_two_linked_lists(self): # Comparar dos listas enlazdas
        pass


    def predelete(self):
        pass


    def delete(self):
        pass


L = LinkedList()
L.append(10)
L.append(20)
L.append(30)
print(L.head.next.next.value)

L.preppend(60)
print(L.head.value)
