class Node:
    def __repr__(self, level=0):
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def __init__(self, value):
        self.value: any = value
        self.children: [Node] = []

class GeneralTree:
    def __init__(self):
        self.root: Node = None

    def __repr__(self):
        if not self.root:
            return "<empty tree>"

        return self.root.__repr__()

    def insert(self, valor, padre, actual):
        if not self.root:

            nuevo_padre = Node(padre)
            nuevo_hijo = Node(valor)
            nuevo_padre.children.append(nuevo_hijo)
            self.root = nuevo_padre
            return

        if actual.valor == padre:
            nuevo_hijo = Node(valor)
            
        self.insert(valor, padre)


