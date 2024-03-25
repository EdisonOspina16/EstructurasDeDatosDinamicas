class Lista_Vacia(Exception):
    pass
class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self,e):
        self.item.append(e)

    def dequeue(self):
        if (len(self.item)==0):
            raise Lista_Vacia
        self.item.pop(0)

    def frist(self):
        if (len(self.item)==0):
            raise Lista_Vacia
        return self.item.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.frist())
print(q)
