class EmptyStackException(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        print(s)
        print(f"máximo: {encontrar_maximo(s)}")
        print(s)
        self.stack.append(e)

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)