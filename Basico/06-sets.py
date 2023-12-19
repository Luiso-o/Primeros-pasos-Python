print("\n***sets***\n")

my_set = set()
my_other_set = {}

print(type(my_set))#<class 'set'>
print(type(my_other_set))#<class 'dict'> es un diccionario?

my_other_set = {"Luis", "Trujillo", 32}
print(type(my_other_set))#<class 'set'>  ahora ya no es un diccionario?
print(my_other_set)#{32, 'Trujillo', 'Luis'}

#Diccionario y set se instancian con {} pero el leguaje interpreta que es un set cuando agregamos las variables.

print("\n***Operaciones de sets***\n")

#cuenta el numero de elemtos del set
print(len(my_other_set))

#Guardar elementos a un set
my_other_set.add("Luiso-o")
print(my_other_set)#{32, 'Luis', 'Luiso-o', 'Trujillo'} Un set no es una estructura ordenada

my_other_set.add("Luiso-o")
print(my_other_set)#{32, 'Luiso-o', 'Luis', 'Trujillo'} Un set no admite repetidos

#verificar que un elemento existe en mi set
print("Luiso-o" in my_other_set) #True
print("Luiso" in my_other_set) #False

#Eliminar elemento de set
my_other_set.remove("Luiso-o")
print(my_other_set)#{'Luis', 'Trujillo', 32}

#Eliminar todos los elementos de mi set
my_other_set.clear()
print(my_other_set)#set()
print(len(my_other_set))#0

'''del es una funcion del sistema no de set, o list, o tuple
del elimina el objeto, no su contenido '''
del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Luis", "Trujillo", 32}
my_other_set = {"Java", "Angular", "Python"}

#Unir dos sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)#{32, 'Trujillo', 'Angular', 'Luis', 'Python', 'Java'}

#Buscando en que se diferencia my_new_set de my_set
print(my_new_set.difference(my_set))#{'Java', 'Angular', 'Python'}

print("\n")