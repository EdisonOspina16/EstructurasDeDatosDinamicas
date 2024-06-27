""""class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)

n1.next = n2
n2.next = n3
n3.next = n4

class LinkedList:
    def __init__(self):
        pass
    
    def head(self):
        pass


    def traverse(node):
        while node is not None:
            print(node.value)
            node = node.next
        pass

    def append(self, value, node):
        pass
    def preppend(self, valor, node):
        new_node = Node(value)
        self.head = new_node
        new_node.next = node
        pass

    def delete_at_index(self, del_index, node, pos=0):
        if del_index >= 
        if del_index == 0:
            self.head = self.head.next
            return
        pass

        if pos == del_index-1:
            next_next = node.next.next
            node.next.next = None
            node.next = next_next
            return
        self.delete_at_index(del_index, node.next, pos+1)""""


