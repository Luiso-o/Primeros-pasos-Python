print("\n***operadores***\n")

print(3 + 4) # resultado: 7
print(3 - 4) # resultado: -1
print(3 / 4) # resultado: 0.75
print(3 * 4) # resultado: 12
print(10 % 3) # modulo resultado: 1
print(10 // 3) # division entera resultado: 3
print(2 ** 3) # exponente resultado: 8
print(2 ** 3 + 3 -7 / 1 // 4) # operaciones complejas

print("\n***concatenaciones***\n")

print("hola " + "Programador") # concatenacion de string 
print("hola " + str(5)) # str convierte el tipo de dato a string
print("hola " * 5) # imprimirá el texto por la cantidad de veces que multiplique el entero
print("Mundo " * (2 ** 3)) # no dará error si el resultado es un entero

print("\n***Operadores comparativos***\n")

print("3 > 4 = " , 3 > 4)
print("3 < 4 = " , 3 < 4)
print("3 >= 4 = " , 3 >= 4)
print("3 <= 4 = " , 3 <= 4)
print("3 == 4 = " , 3 == 4)
print("3 != 4 = " , 3 != 4)

print("\n***Puedo realizar operaciones comparativas a partir de ordenaciones alfabeticas***\n")

## Ordenacion alfabetica por ASCII
print("a es mayor a: b? = " , "a " > "b")
print("c es menor a:  b? = " , "c " < "b")
print("c es mayor o igual a: c? = " , "c" >= "c")
print("d es menor o igual a: z? = " , "d" <= "z")
print("zola es igual a: hola? = " , "zola " == "hola")
print("hola no es igual a: hola? = " , "hola" != "hola")

print("\n***Operadores lógicos***\n")# and, or, not.

print(3 > 4 and "Hola" > "Python") # false && false = false
print(3 > 4 or "Hola" > "Python") # true && false = false
print(3 < 4 and "Hola" < "Python")# true && true = true
print(3 < 4 or "Hola" < "Python")# true && true = true
print(not(3 > 4)) # true

