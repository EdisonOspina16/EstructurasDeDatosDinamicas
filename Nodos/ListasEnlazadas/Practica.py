from ListasEnlazadasEjercicios import *


class EmptyQueue(Exception):
  pass
class PriorityQueue:
  def __init__(self, priority):
    self.__queue = []
    self.priority = priority

  def enqueue(self, e):
    if(self.priority == "max"):
      for idx, element in enumerate(self.__queue):
        if(e > element):
          self.__queue.insert(idx, e)
          return
      else:
        self.__queue.append(e)
    elif(self.priority == "min"):
      for idx, element in enumerate(self.__queue):
        if(e < element):
          self.__queue.insert(idx, e)
          return
      else:
        self.__queue.append(e)


  def dequeue(self):
    if(len(self.__queue) == 0):
      raise EmptyQueue("Cola vacía...")
    return self.__queue.pop(0)

  def first(self):
    if(len(self.queue) == 0):
      raise EmptyQueue("Cola vacía...")
    return self.queue[0]

  def __repr__(self):
    return str(self.__queue)

q = PriorityQueue("min")
q.enqueue(5)
q.enqueue(1)
q.enqueue(7)
q.enqueue(5)
q.enqueue(7)
q.enqueue(1)
q.enqueue(1)
print(q)