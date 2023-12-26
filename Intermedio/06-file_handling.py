print("\n***File Handling***\n")

#manejo de ficheros

print("\n***txt file***\n")
#.txt file : directorio del archivo + w : write | r : read | r+ : read and write
txt_file = open("Intermedio\my_file.txt", "w+")

#txt_file.write("Mi nombre es Luis\nMi appellido es Trujillo\nMi edad es 32\nEstoy Aprendiendo Python\nTambien se programar en Java") #escribe en el archivo txt  

#print(txt_file.read()) #lee todo el contenido del archivo txt

#print(txt_file.read(10)) #lee los 10 primeros caracteres

#print(txt_file.readline()) #lee por lineas

#print(txt_file.readlines()) #Itera el archivo txt

'''
for line in txt_file.readlines():
    print(line) #Recorro linea por linea del archivo txt
'''
    
#from os import remove
#remove(txt_file) #Elimina el fichero txt

txt_file.close()

print("\n***json file***\n")

import json
json_file = open("Intermedio\my_file.json", "w+")

json_text = {
    "Nombre" : "Luis" ,
    "Apellido" : "Trujillo" ,
    "Edad" : 32 ,
    "Lenguaje" : "Python",
    "Alias" : "Luiso-o"}

json.dump(json_text, json_file, indent = 2) #crear un archivo.json

json_file.close()

with open("Intermedio\my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio\my_file.json")) #parseando json a dict
print(json_dict)
print(json_dict["Nombre"])

print("\n***csv file***\n")

import csv
csv_file = open("Intermedio\my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Nombre", "Edad", "Ciudad"])
csv_writer.writerow(["Luis", 32, "Barcelona"])
csv_writer.writerow(["", 32, ""])

csv_file.close()

with open("Intermedio\my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#xml file
import xml

print("\n")