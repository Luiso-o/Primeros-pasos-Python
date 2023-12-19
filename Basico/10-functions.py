print("\n***Funciones***\n")

######################################################
#creamos una funcion
def my_funtion():
    print("Esta es mi primera funcion en python :)")

#llamo my_funtion
my_funtion()
######################################################

print("\n")

######################################################
#creamos una funcion con parametros
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

#llamo my_funtion
sum_two_values(8,3)
######################################################

print("\n")

######################################################
#creamos una funcion donde se devuelve un parametro especifico
def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

#llamo my_funtion
my_result = sum_two_values_with_return(10,20)
print(my_result)
######################################################

print("\n")

######################################################
def print_name(name, surname):
    print(f"Mi nombre es {name} {surname}")

#llamo my_funtion
print_name("Luis","Trujillo")
#Cambiar posicion de los parametros usando el nombre d ela variable
print_name(surname="Trujillo",name="Luis")
######################################################

print("\n")

######################################################
#parametros por defecto
def print_name_with_deft(name, surname, cuenta = "Sin cuenta"):
    print(f"Mi nombre es {name} {surname} y mi cuenta de github es {cuenta}")

#sin pasar el parametro cuenta
print_name_with_deft("Luis","Trujillo")
#Cambiar posicion de los parametros
print_name_with_deft(surname="Trujillo",name="Luis",cuenta="Luiso-o")
######################################################

print("\n")

######################################################
#funcion con un numero de parametros dinámico *
def print_texts(*texts):
    print(texts)


print_texts("Hola")
print_texts("Hola","Python")
print_texts("Hola","Python","Java")
print_texts("Hola","Python","Angular")
######################################################

print("\n")

######################################################
#funcion con un numero de parametros dinámico *
def print_texts(*texts):
    for text in texts:
        print(text.upper())


print_texts("Hola")
print_texts("Hola","Python")
print_texts("Hola","Python","Java")
print_texts("Hola","Python","Angular")
######################################################

print("\n")