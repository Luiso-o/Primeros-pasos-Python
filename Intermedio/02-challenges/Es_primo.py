print("\n***Es un número primo?***\n")

"""
Escribe un programa que se encargue de comprobar si un número es o 
no primo.
Hecho esto, imprime los números del 1 y 100.
"""

def es_primo():

    for numero in range(1,101):

        if numero  >= 2:

            is_divisible = False
        
            for index in range(2,numero ):
                if numero  % index == 0:
                    is_divisible = True
                    break
            
            if not is_divisible:
                print(numero )
            
es_primo()


print("\n")