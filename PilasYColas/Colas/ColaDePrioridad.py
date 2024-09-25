class EmptyQueue(Exception):
    pass

class PriorityQueue:

    def __init__(self, priority):
        self.queue = []
        self.priority = priority

    def enqueue(self, e):
        if self.priority == "max":
            for idx, element in enumerate(self.queue):
                if e > element:
                    self.queue.insert(idx, e)
                    return
            else:
                self.queue.append(e)
        elif self.priority == "min":
            for idx, element in enumerate(self.queue):
                if e < element:
                    self.queue.insert(idx, e)
                    return
            else:
                self.queue.append(e)

    def dequeue(self):
        if len(self.queue)== 0:
            raise EmptyQueue (" Cola Vacía... ")
        return self.queue.pop(0)

    def first(self):
        if len(self.queue)== 0:
            raise EmptyQueue (" Cola Vacía... ")

    def __repr__(self):
        return str(self.queue)


q = PriorityQueue("max")
q.enqueue(5)
q.enqueue(1)
q.enqueue(7)
q.enqueue(5)
q.enqueue(7)
q.enqueue(1)
q.enqueue(1)
print(q)