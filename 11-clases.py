print("\n***Clases***\n")

# definir una clase
class MyEmptyPerson:
    pass #palabra reservada que devuelve un null (return null;)

#se puede instanciar las clases con o sin parentesis
print(MyEmptyPerson)#<class '__main__.MyPerson'>
print(MyEmptyPerson())#<__main__.MyPerson object at 0x00000233B17EE810>

class Person:
    #constructor                       valor por defecto
    def __init__(self,name,surname, alias = "Sin alias"): 
        self.full_name = f"{name} {surname} ({alias})"
        self__name = name #propiedad privada

    #getter
    def get_name(self):
        return self.__name

    #funcion de la clase persona
    def walk (self):
       print(f"{self.full_name} está caminando.")

  
    


#Instancia de la clase persona
my_person = Person("Luis","Trujillo") 
print(my_person.full_name)
#llamando al metodo walk
my_person.walk()#Luis Trujillo Sin alias está caminando.

print("\n")

my_other_person = Person("Carlos", "Mendoza", "Charlie")
my_other_person.walk()#Carlos Mendoza Charlie está caminando.

#puedo modificar una clase como me de la gana
my_other_person.full_name = "(Estoy usando Python)"
print(my_other_person.full_name)

print("\n")