""" CREA UNA FUNCION RECURSIVA QUE RECIBA UNA MATRIZ Y DEVUELVA CUAL ES LA POSICION
    DE LA COLUMNA DONDE ESTA UBICADO EL NUMERO MAYOR DE LA MATRIZ
 """


def buscar(matriz, filas=0, columnas=0, num_mayor=-999):
    if filas == len(matriz):
        return num_mayor
    if columnas == len(matriz[filas]):
        return buscar(matriz, filas + 1, 0, num_mayor)

    if matriz[filas][columnas] > num_mayor:
        num_mayor = matriz[filas][columnas]

    return buscar(matriz, filas, columnas+1, num_mayor)


m = [[8,2000,4,6], [4, 456, 6],]
print(buscar(m))
print("------------------------")

"""
Cree una función recursiva sin cola que reciba una lista L y un elemento E para determinar
si el elemento está o no está dentro de la lista. El retorno debe ser de tipo booleano
"""


def e2(e, lista, index=0, result = False):
    if index == len(lista):
        return result
    if e == lista[index]:
        result = True
        return result
    else:
        result = e2(e, lista, index+1)

    return result


l = ["tepho", 45, 1.5]
print(e2("tepho", l))
print(e2(20, l))
print(e2("chofi", l))
print(e2(1.5, l))
