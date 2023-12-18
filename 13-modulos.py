print("\n***Modulos***\n")
#importacion de librerias en python, 
#importante que el nombre de los ficheros NO empiecen por números.
import modulo

#importar una funcion de un fichero
from modulo_sumar import sum_two_values 

#instancias el modulo para acceder a sus funciones
modulo.sumValues(1,2,3)
modulo.print_value("Hola Python")

#funcion importada del archivo modulo sumar
sum_two_values(3,4)

print("\n")
#modulos predeterminados creados por el sistema
import math

print(math.factorial(5))#120
print(math.pow(2,8))#256.0

                #Alias para la funcion pi
from math import pi as PI_VALUE
print(PI_VALUE)

#imprimir un numero random del 1 al 10
import random
print(random.randint(1,10))

print("\n")

