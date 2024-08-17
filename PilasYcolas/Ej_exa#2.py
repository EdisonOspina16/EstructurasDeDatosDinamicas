"""Cree una función que reciba una pila de pilas llenas de enteros y
 extraiga el elemento menor de cada pila"""


class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if (len(self.stack) == 0):
            raise EmptyStackException
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack[-1]


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
