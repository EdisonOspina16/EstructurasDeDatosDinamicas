def suma_digitos(n):
    if n == 0:
        return 0
    else:
        ultimo_digito = n % 10
        numero_restante = n // 10
    return ultimo_digito + suma_digitos(numero_restante)


print(suma_digitos(123))
print(suma_digitos(456))
print(suma_digitos(789))

