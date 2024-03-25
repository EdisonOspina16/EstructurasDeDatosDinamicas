class EmptyStackException(Exception):
  pass

class Stack:
  def __init__(self):
    self.__stack = []

  def push(self, e):
    self.__stack.append(e)

  def pop(self):
    if(len(self.__stack) == 0):
      raise EmptyStackException
    return self.__stack.pop()

  def top(self):
    if(len(self.__stack) == 0):
      raise EmptyStackException
    return self.__stack[-1]
  def __str__(self):
    return str(self.__stack)


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