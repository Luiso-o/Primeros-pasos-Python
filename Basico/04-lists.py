print("\n***Listas***\n")

#se puesden instanciar listas de la siguiente manera
my_list = list()
my_other_list = []

print(len(my_list))#0

#agregando elmentos a la lista 
my_list = [32,24,62,45,32,34,12,65,98]
print(my_list)
print(len(my_list))

#En las listas se pueden agregar elementos de diferentes tipos
my_other_list = [35,1.77,"Luis","Trujillo"]
print(type(my_other_list))
print(my_other_list)

print("\n***Acceder a un valor de la lista***\n")
print(my_other_list[0])#35
print(my_other_list[1])#1.77
print(my_other_list[2])#Luis
print(my_other_list[3])#Trujillo

#numeros negativos contará la lista desde el final al principio
print(my_other_list[-1])#Trujillo
print(my_other_list[-4])#35

#puedo contar cuantas veces ocurre el mismo valor en la lista
print(my_list.count(32))#hay dos enteros con valor 32 en la lista

#my_other_list = [35,1.77,"Luis","Trujillo"] puedo crear varibles de los componentes de la lista
age,height,name,surname = my_other_list
print(name)#Luis

print("\n***concatenar dos listas***\n")
print(my_list + my_other_list)


print("\n***Operaciones de lista***\n")

#agregar elementos a la lista
my_other_list.append("Canarias")
print(my_other_list)#[35, 1.77, 'Luis', 'Trujillo', 'Canarias']

#insertar en una posicion especifica de la lista
my_other_list.insert(1, "Azul")
print(my_other_list)#[35, 'Azul', 1.77, 'Luis', 'Trujillo', 'Canarias']

#cambiar el valor de un elemento buscandolo por su indice
my_other_list[2] = 1.68
print(my_other_list)#[35, 'Azul', 1.68, 'Luis', 'Trujillo', 'Canarias']

#Eliminar elementos de la lista
my_other_list.remove("Azul")
print(my_other_list)#[35, 1.77, 'Luis', 'Trujillo', 'Canarias']

#remove eliminará el primer elemento que encuentre con ese valor
my_list.remove(32)
print(my_list)#[24, 62, 45, 32, 34, 12, 65, 98]

#Elimina el un elemento por su indice
my_list.pop(2)
print(my_list)#[24, 62, 32, 34, 12, 65, 98]

#otra manera de eliminar por indice
del my_list[2]
print(my_list)#[24, 62, 34, 12, 65, 98]

#si no se especifica un indice, se eliminará el ultimo indice por defecto
my_list.pop()
print(my_list)#[24, 62, 32, 34, 12, 65]

#copiar una lista
my_new_list = my_list.copy()
print(my_new_list)

#Eliminar todos los valores de una lista
my_list.clear()
print(my_list)#[]

#cambia el orden de los elementos del ultimo al primero
my_new_list.reverse()
print(my_new_list)

#ordenacion de mayor a menor
my_new_list.sort()
print(my_new_list)#[12, 24, 34, 62, 65]

#imprimir elementos comprendidos entre el indice x al y
print(my_new_list[1:3])#[24, 34]

print("\n")