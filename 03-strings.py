print("\n***Strings en Python***\n")

my_string = "Soy un string" 
my_other_string = 'Tambien soy un string' 

print(len(my_string))#13
print(len(my_other_string))#21

print("\n***Strings concatenados***\n")
print(my_string + " " + my_other_string)

print("\n***Strings con saltos de linea***\n")
my_new_line_string = "Este es un string\ncon salto de linea."
print(my_new_line_string)

print("\n***Strings con tabulacion***\n")
my_tab_string = "\tEste es un string con tabulacion."
print(my_tab_string)

print("\n***Formateando cadenas de texto***\n")

name, surname, age = "Luis", "Trujillo", 32

print("Mi primer nombre es {} {} y mi edad es {}".format(name,surname,age)) #format
print("Mi primer nombre es %s %s y mi edad es %d" %(name,surname,age)) #%
print(f"Mi primer nombre es {name} {surname} y mi edad es {age}")

print("\n***Desenmpaquetado de caracteres***\n")

language = "python"
a,b,c,d,e,f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("\n***Division***\n")

language_slice = language[1:3]
print(language_slice) #yt

language_slice = language[1:]
print(language_slice)#ython

language_slice = language[-2]
print(language_slice)#o

language_slice = language[0:6:2]
print(language_slice)#y

print("\n***Reverse***\n")

reverse_language = language[::-1]
print(reverse_language)#nohtyp

print("\n***funciones del sistema***\n")

#Imprime la primera letra en mayuscula
print(language.capitalize())

#Imprime todo en mayuscula
print(language.upper())

#Imprime todo en minusculas
print(language.lower())

#Paso a mayusculas y luego pregunto si la cadena es en mayuscula
print(language.upper().isupper()) #true

#cuantos caracteres con x valor tiene la cadena de texte
print(language.count("t"))

#si es un numero(boolean)
print(language.isnumeric())#false
print("1".isnumeric())#true

#Preguntar si la cadena empieza por...
print(language.startswith("py"))#true

print("\n")