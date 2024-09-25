class EmptyStack(Exception):
    pass


class Stack:

    def __init__(self):
        self.stack = {}

    def push(self, e):
        clave = len(self.stack)
        if clave not in self.stack:
            self.stack[clave] = e

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStack
        ultimo_indice = len(self.stack)-1
        ultimo_elemento = self.stack[ultimo_indice]
        del self.stack[ultimo_indice]
        return ultimo_elemento

    def peek(self):
        if len(self.stack) == 0:
            raise EmptyStack
        return len(self.stack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)



print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())

print(s.stack)
print(s.pop())
print(s.peek())