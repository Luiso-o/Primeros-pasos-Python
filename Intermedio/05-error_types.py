print("\n***Tipos de excepciones***\n")

#SyntaxError
#print "Hola Mundo!" #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print ("Hola Mundo!")

#NameError
#print(name) #NameError: name 'name' is not defined

name = "Luis"
print(name)

#IndexError
list = [1,2,3,4,5,6]
#print(list[6]) #IndexError: list index out of range

print(list[-1])
print(list[5])

#ModuleNotFount
#import maths #ModuleNotFoundError: No module named 'maths'

import math

#AttributeError
#print(math.PI)#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

print(math.pi)

#KeyError
dict = {"nombre" : "Luis", "Apellido" : "Trujillo", "alias" : "Luiso-o", "edad" : 32}
#print(dict["eda"]) #KeyError: 'eda'

print(dict["edad"])

#TypeError
list = [1,2,3,4,5,6]
#print(list["1"]) #TypeError: 'list' object is not callable

print(list[1])

#ImportError
#from math import PI #ImportError: cannot import name 'PI' from 'math' (unknown location)  

from math import pi
print(pi)

#ValueError
#my_int = int("10 Anos") # ValueError: invalid literal for int() with base 10: '10 Anos'

my_int = int("10")
print(type(my_int))

#ZeroDivisionError
#print(2 / 0) #ZeroDivisionError: division by zero

print(2 / 2)

print("\n")