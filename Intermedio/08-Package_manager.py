print("\n***Manejo de paquetes Python***\n")

#instalar numpy : pip install numpy
import numpy

print(numpy.version.version) #1.26.2

numpy_array = numpy.array([34,54,34,56,79,32])
print(numpy_array) #[34 54 34 56 79 32]

#Multiplicar cada elemento de las listas por 2
print(numpy_array * 2) #[ 68 108  68 112 158  64]

#instalar pandas : pip install pandas
import pandas

#pip list : listado de las librerias instaladas
#pip uninstall nombre_de_paquete : desinstalar un paquete
#pip show nombre_de_paquete : ver informacion de un paquete

#instalar requests : pip install requests
import requests

#peticiones a una api
response = requests.get("https://github.com/Luiso-o")
print(response) #<Response [200]>
print(response.status_code) #200
#print(response.json()) #traera informacion en formato json

#importar paquete local
from challenges import Anagramas

print(Anagramas.is_anagram("amor", "roma"))

print("\n")