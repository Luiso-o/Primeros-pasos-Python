print("\n***dicts***\n")

#instanciar un dict
my_dict = dict()
print(type(my_dict))#<class 'dict'>


my_other_dict = {}
print(type(my_other_dict))#<class 'dict'>

#Introducir datos a un dict
my_other_dict = {"Nombre" : "Luis", "Apellido" : "Trujillo", "Edad" : 32, 1 : "Python" }
print(my_other_dict)#{'Nombre': 'Luis', 'Apellido': 'Trujillo', 'Edad': 32, 1: 'Python'}

my_dict = {
   'Nombre': 'Luis', 
   'Apellido': 'Trujillo', 
   'Edad': 32, 
   'Lenguajes' : {'Python', 'Java', 'Angular'},
   1:1.68
}

print(my_dict)
'''{'Nombre': 'Luis',
'Apellido': 'Trujillo', 
'Edad': 32,
'Lenguajes': {'Angular', 'Python', 'Java'},
1: 1.68
'''

print(my_other_dict)

#numero de caracteres del dict
print(len(my_dict))#5
print(len(my_other_dict))#4

#buscar por nombre de la clave
print(my_dict["Nombre"])#Luis

#Actualizar valor de la clave
my_dict["Nombre"] = 'Pedro'
print(my_dict["Nombre"])#Pedro

#Agregar datos a nuetro dict
my_dict["Calle"] = "Calabria"
print(my_dict)
'''
{'Nombre': 'Pedro', 
'Apellido': 'Trujillo', 
'Edad': 32, 
'Lenguajes': {'Python', 'Angular', 'Java'}, 
1: 1.68, 
'Calle': 'Calabria'}
'''

print("\n***Operaciones de dict***\n")

#para eliminar un solo elemento del diccionario solo podemos contal con la funcion del
del my_dict["Calle"]
print(my_dict)
'''
{'Nombre': 'Pedro', 
'Apellido': 'Trujillo', 
'Edad': 32, 
'Lenguajes': {'Python', 'Java', 'Angular'}, 
1: 1.68}
'''

#Existe la clave x en mi dict?
print("Apellido" in my_dict)#true
print(32 in my_dict)#false: es el valor, no la clave

#listado de cada uno de los items
print(my_dict.items())
'''
dict_items([('Nombre', 'Pedro'),
('Apellido', 'Trujillo'), 
('Edad', 32), 
('Lenguajes', {'Angular', 'Python', 'Java'}), 
(1, 1.68)])
'''

#devuelve un listado de las keys (claves)
print(my_dict.keys())
'''
dict_keys(['Nombre',
 'Apellido', 
 'Edad', 
 'Lenguajes', 
 1])
'''

#devuelve todos los valores
print(my_dict.values())
'''
dict_values(['Pedro', 
'Trujillo', 
32, {'Angular', 'Python', 'Java'},
1.68])
'''

#crear un diccionario nuevo sin valores
print(my_dict.fromkeys(("Nombre",1,"Piso")))#{'Nombre': None, 1: None, 'Piso': None}

print("\n")