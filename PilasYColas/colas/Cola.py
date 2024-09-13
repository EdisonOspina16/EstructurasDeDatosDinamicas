class EmptyStack(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if len(self.queue) == 0:
            raise EmptyStack
        return self.queue.pop()

    def frist(self):
        if len(self.queue) == 0:
            raise EmptyStack
        return self.queue[-1]

    def __str__(self):
        return str(self.queue)


