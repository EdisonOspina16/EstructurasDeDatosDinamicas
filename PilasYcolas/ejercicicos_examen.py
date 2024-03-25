"""E8. Cree una función que reciba una cola de colas.
En estas colas hay objetos de tipo cliente con un atributo nombre y otro prioridad
(1, 2 o 3). Esta función se enfocará en atender cada una de las colas internas por prioridad,
es decir, primero atenderá a todos los de prioridad 1 de todas las colas,
luego los de prioridad 2, etc. Cada vez que se atienda un cliente,
saldrá su nombre, prioridad y la cola donde está."""
class Queue_is_Empty(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        return self.items.pop(0)  # Return the dequeued element

    def first(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        return self.items[0]

class Cliente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"Cliente: {self.nombre}, Prioridad: {self.prioridad}"


cliente1 = Cliente("edison", 1)
cliente2 = Cliente("Daniel", 2)
cliente3 = Cliente("sofia", 3)

ColaPrincipal = Queue()

Cola2 = Queue()
Cola2.enqueue(cliente1)
Cola2.enqueue(cliente2)
Cola2.enqueue(cliente3)

ColaPrincipal.enqueue(Cola2)
