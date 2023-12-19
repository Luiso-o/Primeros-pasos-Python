print("\n***Sucesion de Fibonacci***\n")

"""
Escribe un programa que imprima los primeros 50 números de la sucesión de 
Fibonacci empezando por 0.
- La serie Fibonacci se compone por una sucesión de números en la que 
el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

#opcion tradicional
def fibonacci():

    prev = 0
    next = 1

    for index in range(0,51):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()
print("\n")