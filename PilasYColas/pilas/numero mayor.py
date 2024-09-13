import Pila


def numero_mayor(pila):
    s = Pila.Stack()
    maximo = 0
    for _ in range(len(pila)):
        valor_actual = s.pop()
        s.push(valor_actual)
        if maximo < valor_actual:
            maximo = valor_actual

    while True:
        pila.push(s.pop())
        if Pila.EmptyStackException():
            return maximo


s = Pila.Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)

print(s)
print(f"máximo: {numero_mayor(s)}")
print(s)