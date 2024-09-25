import Pila


def invertir(cadena):
    s = Pila.Stack()
    for letras in cadena:
        s.push(letras)
    cadena_invertida = ""
    while True:
        try:
            cadena_invertida += s.pop()
        except Pila.EmptyStackException:
            break
    return cadena_invertida


cadena = "edison"
cadena_invertida = invertir(cadena)
print(cadena_invertida)