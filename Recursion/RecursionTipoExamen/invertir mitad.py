"""E2. Cree una función no recursiva de cola que invierta sólo la segunda mitad de un string.

Por ejemplo, si la función recibe "Hola", deberá retornar "Hoal".
Asuma que el punto medio es tamaño//2"""


def e2(word, index=0):
    if index == len(word):
        return ""
    if index < len(word) // 2:
        return word[index] + e2(word, index+1)
    return e2(word, index+1) + word[index]


print(e2("hola"))
print(e2("jhonatan"))
