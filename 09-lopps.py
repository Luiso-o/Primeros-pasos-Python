print("\n***loops-while***\n")

#############################################
my_condition = 0

while my_condition < 10:
    print(my_condition, " es menor a 10 ")
    my_condition +=2

print("Salimos del bucle\n")
##############################################

##############################################
#En python podemos agregar un else
my_condition = 0

while my_condition < 10:
    print(my_condition, " es menor a 10 ")
    my_condition +=2
else:
    print("El numero es igual 10")

print("Salimos del bucle\n")
##############################################

##############################################
my_condition = 10
#bucle while y condicional if usando break
while my_condition < 20:
    print(my_condition," es menor a 15") 
    my_condition +=1
    if my_condition == 15:
        print("Mi condicion es 15")
        break
##############################################

print("\n***loops-For***\n")

my_list = {35,24,62,52,30,30,17}
my_tuple = (35,1.77,"Luis","Trujillo","Luiso-o")
my_set = {"Luis","Trujillo",32}
my_dict = {"Nombre" : "Luis", "Apellido" : "Trujillo", "Edad" : 32, 1 : "Python" }

print("\nfor lista:")
##############################################

for element in my_list:
    print(element)
##############################################

print("\nfor tuple:")
##############################################
for element in my_tuple:
    print(element)
##############################################

print("\nfor set:")
##############################################
for element in my_set:
    print(element)
##############################################

print("\nfor dict:")
##############################################
for element in my_dict:
    print(element)
##############################################

print("\nSalimos del bucle")

print("\n")