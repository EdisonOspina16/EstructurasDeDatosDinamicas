"""def imprimir_numeros(n):
    if n == 1:
        return 1
    else:
        print(n)
        return imprimir_numeros(n-1)


print(imprimir_numeros(4))"""
"0.3"

" Defina una función recursiva que reciba una lista para determinar cuántos numeros pares hay en ella"

"""def es_par(n, index=0, count=0):
    if index == len(n):
        return count
    if n[index] % 2 == 0:
        count += 1
    return es_par(n, index+1, count)


lista = [1, 2, 3, 4, 5]
print(es_par(lista))
print("-------------------")


def es_par_sin_cola(n, index=0):
    if index == len(n):
        return
    if n[index] % 2 == 0:
        re
        return es_par_sin_cola(n, index+1)


lista = [1, 2, 3, 4, 5]
print(es_par_sin_cola(lista))


print("-------------------")



" Imprimir todos los elementos de una lista"
"""


def imprimir_elementos(lista, index=0):
    if index == len(lista):
        return
    print(lista[index])
    return imprimir_elementos(lista, index + 1)


l = [1, "hola", 2, 1.5]
print(imprimir_elementos(l))


