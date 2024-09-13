import Pila


def invertir_mitad(cadena):
    s = Pila.Stack()
    longitud = len(cadena)
    mitad = longitud // 2

    for letras in range(mitad):
        s.push(cadena[letras])

    mitad_invertida = ""
    while True:
        try:
            mitad_invertida += s.pop()
        except Pila.EmptyStackException:
            break
    cadena_invertida = mitad_invertida + cadena[mitad:]
    return cadena_invertida


c = "hola"
print(c)
print(invertir_mitad(c))



