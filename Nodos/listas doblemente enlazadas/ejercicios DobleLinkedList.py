class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None
        self.prev: Node = None

    def __repr__(self):
        return f"{self.value}->{self.next}"


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        return f"{self.head}"


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

    def delete_at(self, index):
        pass

l = DoubleLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
print(l)