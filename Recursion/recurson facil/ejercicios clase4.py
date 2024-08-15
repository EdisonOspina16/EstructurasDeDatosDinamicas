def imprimir_elementos(lista, index=0):
    if index == len(lista):
        return
    print(lista[index])
    return imprimir_elementos(lista, index+1)


l = [1, "edison", 1.2]
print(imprimir_elementos(l))

"0,1"
print("--------------------------------")


def imprimir_elementos_matrix(matriz, filas=0, columnas=0):
    if filas == len(matriz):
        return
    if columnas == len(matriz[filas]):
        return imprimir_elementos_matrix(matriz, filas+1, 0)
    else:
        print(matriz[filas][columnas])
    return imprimir_elementos_matrix(matriz, filas, columnas+1)


m = [[1, 2, 3, 4],[5, 6, 7, 8]]
imprimir_elementos_matrix(m)


print("------------------------")

def es_par_matriz(matriz, filas=0, columnas=0):
    if filas == len(matriz):
        return
    if columnas == len(matriz[filas]):
        return es_par_matriz(matriz, filas+1, 0)
    if matriz[filas][columnas] % 2 == 0:
        print(matriz[filas][columnas])
    return es_par_matriz(matriz, filas, columnas + 1)

mx = [[1, 2, 3, 4], [5, 6, 7, 8]]
es_par_matriz(mx)


