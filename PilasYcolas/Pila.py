class EmptyStackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)
