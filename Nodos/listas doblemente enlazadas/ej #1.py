class DNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Doblell:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def append(self, value):
        new_node = DNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    "02"

    def search(self, e):
        current_node = self.head
        while current_node is not None:
            if current_node.value == e:
                return True
            current_node = current_node.next
        return False

    def recursive_search(self, e, current_node):
        if current_node is not None:
            if current_node.value == e:
                return True
            else:
                current_node = current_node.next
                return self.recursive_search(e, current_node)
        return False

    "0.3"
    def replace(self, node, valor_buscar, valor_reemplazar):
        if self.head is None:
            return "no hay nada en la lista"
        while node is not None:
            if node.value == valor_buscar:
                node.value = valor_reemplazar
                return node
            node = node.next

    def recursive_replace(self, node, valor_buscar, valor_reemplazar):
        if self.head is None:
            return
        if node is not None:
            if node.value == valor_buscar:
                node.value = valor_reemplazar
            self.recursive_replace(node.next, valor_buscar, valor_reemplazar)

    def replace_solo_uno(self, node, valor_buscar, valor_reemplazar):
        if node is None:
            return "no hay nada en la lista"
        while node is not None:
            if node.value == valor_buscar:
                node.value = valor_reemplazar
                break
            node = node.prev

dll = Doblell()
dll.append(9)
dll.append(9)
dll.append(5)
dll.append(2)
dll.append(7)


"""print(dll.search(9))
print(dll.search(6))
print(dll.search(7))
print(dll.search(8))
print(dll.search(4))
print(dll.search(1))"""

dll.traverse()
print("--------")
dll.replace(dll.head, 9, 100)
dll.traverse()
#dll.replace_solo_uno(9, 100)

"""dll.traverse()
print("-------")
dll.recursive_replace(dll.head, 7, 100)
dll.traverse()"""



"""dll.recursive_search(1, 0)
dll.recursive_search(3, 0)
dll.recursive_search(9, 0)
dll.recursive_search(8,0)
dll.recursive_search(2,0)
dll.recursive_search(7,0)"""
