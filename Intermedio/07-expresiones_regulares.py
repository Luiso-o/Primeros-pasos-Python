print("\n***Regular Expressions***\n")

import re

my_string = "Esta es la lección numero 7: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección numero 6: Manejo de ficheros"

#busca caracteres en una cadena de string, busca desde el principio
print(re.match("Esta es la lección", my_string))#<re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match("Esta es la lección", my_other_string))#None
print(re.match("Expresiones regulares", my_other_string))#None

match = re.match("Esta es la lección", my_string, re.I)
print(match)
stard, end = match.span()#(0, 18)
print(my_string[stard : end])

match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    print(match)
    stard, end = match.span()
    print(my_other_string[stard : end])

print(re.match("Expresiones regulares", my_string))

#search busca desde cualquier posicion
search = re.search("Esta es la lección", my_string, re.I)
print(search)#<re.Match object; span=(0, 18), match='Esta es la lección'>   

search = re.search("lección", my_string, re.I)
print(search)#<re.Match object; span=(11, 18), match='lección'>

#findall busca la cantidad de elementos iguales
findall = re.findall("Esta es la lección", my_string, re.I) #re.I case sensitive
print(findall)#['Esta es la lección']

findall = re.findall("lección", my_string, re.I)
print(findall)#['lección', 'Lección']

#split busca un patron y divide a partir de allí
split = re.split(":",my_string)
print(split)#['Esta es la lección numero 7', ' Lección llamada Expresiones regulares'] 

#sub modifica el caracter que elijas de la cadena
sub = re.sub("Expresiones", "expresiones", my_string)
print(sub)#Esta es la lección numero 7: Lección llamada expresiones regulares

sub = re.sub("lección|Lección", "LECCION", my_string)
print(sub)#Esta es la LECCION numero 7: LECCION llamada Expresiones regulares

print("\n***Patrones personalizados***\n")
my_string = "Esta es la lección numero 7: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección numero 6: Manejo de ficheros"


pattern = r"[lL]ección"
print(re.findall(pattern, my_string))#['lección', 'Lección']

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))#['lección', 'Lección', 'Expresiones']

pattern = r"[a-z]" #devuelve todas las letras
print(re.findall(pattern, my_string))
'''
['s', 't', 'a', 'e', 's', 'l', 'a', 'l', 'e', 'c', 'c', 'i', 'n', 'n', 'u', 'm', 'e', 'r', 'o', 'e', 'c', 'c', 'i', 'n', 'l', 'l', 'a', 'm', 'a', 'd', 'a', 
'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']
'''

pattern = r"[0-9]" #devuelve todos los numeros
print(re.findall(pattern, my_string)) #['7']

pattern = r"\d" 
print(re.findall(pattern, my_string))#['7']

pattern = r"\D" 
print(re.findall(pattern, my_string))
'''
['E', 's', 't', 'a', ' ', 'e', 's', ' ', 'l', 'a', ' ', 'l', 'e', 'c', 'c', 'i', 'ó', 'n', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', ':', ' ', 'L', 'e', 'c', 
'c', 'i', 'ó', 'n', ' ', 'l', 'l', 'a', 'm', 'a', 'd', 'a', ' ', 'E', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', ' ', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']
'''
pattern = r"[l]." 
print(re.findall(pattern, my_string))#['la', 'le', 'll', 'la']

email = "cheportillo@gmail.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

print("\n")