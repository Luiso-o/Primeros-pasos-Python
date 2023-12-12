print("\n***Condifional if***\n")

my_condition = False

#######Estructura condicional
if my_condition: #true por defecto
    print("Se ejecuta la condicion if")

print("La ejecucion continua")
########

#########
my_condition = 5*5

if my_condition == 10:
    print("la oprecación es igula a 10")#si la condicion es True
else:
    print("la opreacion no es igual a 10")#si la condicion es False
##########

#########
if my_condition > 10:
    print("la oprecación es mayor a 10")#si la condicion es True
else:
    print("la opreacion no es mayor a 10")#si la condicion es False
##########

#Mas condiciones utilizando operadores
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es Igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual a 20 o distinto a 25")
############

#Ingresando texto desde consola detectando si no se ingresa nada
my_String = input()

#not: verifica que la variable esté vacía
if not my_String:
    print("My cadena de texto está vacía")
else:
    print(my_String)

print("\n")