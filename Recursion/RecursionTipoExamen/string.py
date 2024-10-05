"""
TENGO UN STRING EJEMPLO "aHexvguSiLaLuGi" Y DEBE DEVOLVER LAS CONSONANTES QUE ESTEN
ENTRE VOCALES EN OTRO STRING ES DECIR "HSLLG"

"""


def string(letras, index=0):
    vocales = "aeiou"

    if index == len(letras)-2:
        return ""

    if letras[index+1] in vocales and letras[index-1] in vocales:
        consonante = letras[index]
        return consonante + string(letras, index+1)

    return string(letras, index+1)

letras = "aHexvguSiLaLuGi"
print(string(letras))
