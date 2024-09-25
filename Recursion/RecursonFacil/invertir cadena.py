def invertir_cadena(cadena):
    if len(cadena) == 0 or len(cadena) == 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])


print(invertir_cadena("hola"))
print(invertir_cadena("jhonatan"))
print(invertir_cadena("ana"))
print(invertir_cadena("e"))
print(invertir_cadena(""))

print("-------------------------------")


# invertir cadena sin usar slicing
def invertir_cadena_aux(cadena, inicio, fin):
    if inicio >= fin:  # Caso base
        return ""
    else:  # Llamada recursiva
        return cadena[fin - 1] + invertir_cadena_aux(cadena, inicio, fin - 1)


def invertir_cadena(cadena):
    return invertir_cadena_aux(cadena, 0, len(cadena))


# Pruebas
print(invertir_cadena("hola"))  # Debería devolver "aloh"
print(invertir_cadena("recursion"))  # Debería devolver "noisrucer"
