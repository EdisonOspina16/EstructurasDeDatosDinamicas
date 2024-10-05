class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None
        self.prev: Node = None

    def __repr__(self):
        return f"{self.value}<->{self.next}"


class DoubleLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def __repr__(self):
        return f"{self.head}"

    "bonificacion"
    def append(self, e):
        nuevo_nodo = Node(e)
        if self.size == 0:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            self.size += 1
            return

        self.tail.next = nuevo_nodo
        nuevo_nodo.prev = self.tail
        self.tail = nuevo_nodo
    def inverse_traverse(self):
        nuevo_nodo = self.tail
        while nuevo_nodo is not None:
            print(nuevo_nodo.value)
            nuevo_nodo = nuevo_nodo.prev

    def delete_at_index(self, index):
        if (index < 0 or index >= self.size):
            raise IndexError

        self.size -= 1
        if (index == 0):  # caso en el que quieran borrar el primero
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
            return

        current_node = self.head  # variable auxiliar que empieza en la cabeza
        for i in range(index - 1):  # sólo lo uso para RECORRER
            current_node = current_node.next  # actualizo mi variable auxiliar
        current_next = current_node.next  # guardando mi next actual --> para borrarle el enlace a su next DESPUÉS
        current_node.next = current_node.next.next  # actualizando mi next
        current_next.next = None  # borrando el next del next anterior

    def pares_izquierda(self, count_derecha=0, count_izquierda=0):
        current_node = self.head

        while current_node:

            reves = current_node
            while reves:
                if reves.value % 2 ==0:
                    count_izquierda += 1
                reves = reves.prev

            derecho = current_node
            while derecho:
                if derecho.value % 2 == 0:
                    count_derecha += 1
                derecho = derecho.next

            if count_izquierda > count_derecha:
                print(current_node.value)

            count_izquierda=0
            count_derecha=0
            current_node = current_node.next



l = DoubleLinkedList()
l.append(2)
l.append(4)
l.append(5)
l.append(15)
l.append(3)
print(l)

l.pares_izquierda()