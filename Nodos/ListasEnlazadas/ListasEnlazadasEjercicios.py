class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None

    def __repr__(self):
        return f"{self.value}->{self.next}"


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def __repr__(self):
        return f"{self.head}"


    "0.1"
    def preppend(self, e): # Agregar al principio
        nuevo_nodo = Node(e)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    "0.1"
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

    "0.1"
    def traverse(self):  # Recorrer la lista enlazada.
        nodo_actual = self.head.next
        while nodo_actual is not None:
            print(nodo_actual.value)
            nodo_actual = nodo_actual.next

    def delete_first(self):
        if self.head is None:
            return
        nodo_viejo = self.head
        self.head = self.head.next
        nodo_viejo = None

    " SEGUNDA CLASE DE LISTAS ENLAZADAS "

    "0.1"
    def delete(self):  # Eliminar al final.
        if self.head is None:
            return

        nodo_actual = self.head
        while nodo_actual.next.next:
            nodo_actual = nodo_actual.next

        nodo_actual.next = None


    "0.1"
    def search(self, e):  # Buscar un elemento en una lista enlazada.
        if self.head is None:
            return False

        nodo_actual = self.head
        while nodo_actual:
            if nodo_actual.value == e:
                return True
            else:
                nodo_actual = nodo_actual.next
        return False

    "0.1"
    def size(self, count=0):  # Obtener tamaño de la lista enlazada.
        if self.head is None:
            return

        nodo_actual = self.head
        while nodo_actual is not None:
            count += 1
            nodo_actual = nodo_actual.next
        return count

    "0.1, recursion 0.2"
    def append_recursive(self, e, nodo_actual):
        if self.head is None:
            self.head = Node(e)
            return

        if nodo_actual.next is None:
            nodo_actual.next = Node(e)
            return
        return self.append_recursive(e, nodo_actual.next)

    def traverse_recursive(self, nodo_actual):
        if self.head is None:
            return

        if nodo_actual is None:
            print(nodo_actual)
            return
        return self.traverse_recursive(nodo_actual.next)

    " TERCERA CLASE DE LISTAS ENLAZADAS "
    def delete_a_position(self, index):  # Eliminar una posicion arbitraria.
        if index < 0 or index >= self.size:
            return IndexError
        self.size -= 1
        cabeza_vieja = self.head

        nodo_actual = self.head
        for i in range(index-1):
            nodo_actual = nodo_actual.next
        actual_siguiente = nodo_actual.next
        nodo_actual.next = nodo_actual.next.next
        nodo_actual.next = None

    def compare_two_linked_lists(self):  # Comparar dos listas enlazdas.
        pass

    def add_at_a_position(self):  # Agregar en una posicion arbitraria.
        pass

    def reverse(self):  # Invertir lista enlasaza.
        pass

    def sort(self):  # Ordenar lista enlazada.
        pass

("0.3 ---> para colas")
class EmptyQueue(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, e):  # Agregar al principio
        nuevo_nodo = Node(e)
        if not self.queue.head:
            self.queue.head = nuevo_nodo
        else:
            nodo_actual = self.queue.head
            while nodo_actual.next:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_nodo

    def dequeue(self):  # Eliminar al principio y retornar
        if not self.queue.head:
            raise EmptyQueue

        nodo_viejo = self.queue.head
        self.queue.head = self.queue.head.next
        nodo_viejo.next = None
        return nodo_viejo.value

    def frist(self):  # Retorna el primer elemento
        if not self.queue.head:
            raise EmptyQueue
        return self.queue.head.value

    def __str__(self):
        return str(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)
print(q.frist())
print(q.dequeue())
print(q)
print(q.frist())
print(q)
print(q.frist())
print(q.dequeue())
print(q)
print(q.frist())
print(q)
print(q.frist())
print(q.dequeue())
print(q)
print(q.frist())
print(q)
print(q.frist())
print(q.dequeue())
print(q)
print(q.frist())
print(q)
print(q.frist())
print(q.dequeue())
print(q)
print(q.frist())