print("\n***resolviendo retos en python***\n")

"""
El FAMOSO "FIZZ BUZZ":
Escribe un programa  que muestre por consola los números del 1 al 100
ambos incluidos y con un salto de linea entre cada impresión, sustituyendo
lo siguiente:
- Multiplos de 3 por la palabra "FIZZ".
- Multiplos de 5 por la palabra "BUZZ".
- Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("FIZZ")
        elif index % 5 == 0:
            print("BUZZ")
        else:
            print(index)

fizzbuzz()        