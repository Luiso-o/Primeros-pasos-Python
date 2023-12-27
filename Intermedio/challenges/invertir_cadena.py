'''
Crea un programa que invierta el orden de una cadena de texto sin usar
funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola Mundo" nos retornaría "odnuM aloH"
'''


def invertir_cadena(cadena):
    texto_invertido = ""
    longitud_texto = len(cadena)

    for index in range (0, longitud_texto):
        texto_invertido += cadena[longitud_texto - index - 1]
    return texto_invertido


print(invertir_cadena("Hola Mundo"))
