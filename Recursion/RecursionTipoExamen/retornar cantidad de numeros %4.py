""" Cree una función recursiva de cola que reciba un entero y retorne cuántos dígitos
 de este número son múltiplos de 2 y de 4. Ignore el cero.

Por ejemplo: si la función recibe el número 34523, deberá retornar 1
 ya que hay sólo un número que es múltiplo de ambos números (el 4).
"""


def e1(n, counter=0):
    if n == 0:
        return counter
    digit = n % 10
    if digit != 0 and digit % 4 == 0:
        counter += 1
    n = n // 10
    return e1(n, counter)


print(e1(348120))
