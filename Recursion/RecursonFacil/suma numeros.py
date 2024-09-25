def suma_numeros(n):
    if n == 0:
        return 0
    else:
        return n + (suma_numeros(n-1))


print(suma_numeros(0))
print(suma_numeros(1))
print(suma_numeros(2))
print(suma_numeros(3))
print(suma_numeros(4))
print(suma_numeros(5))
