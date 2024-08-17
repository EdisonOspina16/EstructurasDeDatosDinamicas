class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)    # Agrega un elemento a la pila

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack.pop()   # Elimina y retorna

    def top(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack[-1]   # Retorna la ultima posicion de la pila

    def __str__(self):
        return str(self.stack)


s = Stack()
s.push(5)
s.push(6)
s.push(7)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.top())
print(s)
print(s.pop())
print(s)
print(s.pop())
