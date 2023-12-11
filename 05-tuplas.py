print("\n***tuples***\n")

#manera de instanciar una tuple
my_tuple = tuple()
my_other_tuple = (35,60,30)

#bastante parecidas a las listas
my_tuple = (35,1.86,"Luis","Trujillo","Luis")
print(type(my_tuple))#<class 'tuple'>
print(my_tuple)#(35, 1.86, 'Luis', 'Trujillo', 'Luis')

print(my_tuple[0])#35
print(my_tuple[-1])#Luis

print("\n***operaciones***\n")

#cuenta la cantidad de elementos con el mismo valor en la lista
print(my_tuple.count("Luis"))#1
print(my_tuple.count(45))#0

#busca el primer indice que encuentra con el elemnto asignado
print(my_tuple.index("Trujillo"))#3

"""
Una diferencia entre tuple y list es que no se pueden
modificar los valores contenidos en tuple:


my_tuple[1] = 1.80
print(my_tuple) #TypeError: 'tuple' object does not support item assignment
"""

# concatenar tuples
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)#(35, 1.86, 'Luis', 'Trujillo', 'Luis', 35, 60, 30)

#imprime los valores desde el punto x al punto y
print(my_sum_tuple[3:6])#('Trujillo', 'Luis', 35)

# convertir una tuple a list
my_tuple = list(my_tuple)
print(type(my_tuple))#<class 'list'>

#Cambiar la estructura del list
my_tuple[4] = "Portillo"
my_tuple.insert(1,"Azul")
print(my_tuple) #[35, 'Azul', 1.86, 'Luis', 'Trujillo', 'Portillo']

#convertir la list en una tuple
my_tuple = tuple(my_tuple)
print(type(my_tuple))#<class 'tuple'>
print(my_tuple)#(35, 'Azul', 1.86, 'Luis', 'Trujillo', 'Portillo')

#los tuples no se pueden eliminar, aquí eliminamos la variable
del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined

print("\n")