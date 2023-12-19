# no hace falta especificar el tipo de variable
print("\n***Variables***\n")
my_string_variable = "My string variable" 
print(my_string_variable) # My string variable

my_int_variable = 3
print(my_int_variable) # 3

my_int_to_str_variable = str(my_int_variable) #str convierte cualquier tipo de dato en string
print(my_int_to_str_variable) # 3
print(type(my_int_to_str_variable)) # string


my_bool_variable = True
print(my_bool_variable) # True

# puedo compilar dos variables separadas por una coma
print(my_string_variable, my_int_variable,my_bool_variable)
print("tambien se puede concatenar variables con cadenas de texto",my_int_variable)

# funciones del sistema: len() cuenta los caracteres de las variables
print(len(my_string_variable)) 

# variables en una sola linea
name, surname, alias, age = "Luis", "Trujillo", "Luiso-o", 32
print("Me llamo",name,surname,"mi edad es:",age, "y mi alias es:",alias)

#input
nombre = input("Cual es tu nombre?")
edad = input("y cual es tu edad?")

print('Me llamo',nombre,"y mi edad es:",edad)