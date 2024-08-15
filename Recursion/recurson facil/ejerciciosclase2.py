def multiplicacion(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multiplicacion(num1, num2-1)


print(multiplicacion(5, 0))
print(multiplicacion(2, 1))
print(multiplicacion(3, 2))
print(multiplicacion(4, 3))
print(multiplicacion(5, 4))
print(multiplicacion(6, 5))
print(multiplicacion(0, 5))
print("----------------------------------")

"0.1"

