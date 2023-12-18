print("\n***Excepciones***\n")

num1 = 5
num2 = "1"

#try except
try:
    #se ejecuta solo si no ocurren errores
    print(num1 + num2)
    print("No se ha producido un error")
except:
    #se ejecuta si ocurre un error
    print("Se ha producido un error")

print("\n")

#try except else
try:
    #se ejecuta solo si no ocurren errores
    print(num1 + num2)
    print("No se ha producido un error")
except:
    #se ejecuta si ocurre un error
    print("Se ha producido un error")
else: 
    #solo se ejecuta si el try no lanza nigun error
    print("La ejecución continúa correctamente")


print("\n")

#try except else finally
try:
    #se ejecuta solo si no ocurren errores
    print(num1 + num2)
    print("No se ha producido un error")
except:
    #se ejecuta si ocurre un error
    print("Se ha producido un error")
else: 
    #solo se ejecuta si el try no lanza nigun error
    print("La ejecución continúa correctamente")
finally:
    #se ejecuta con o sin error
    print("La ejecución continúa")

print("\n")

#captura de excepciones por tipo
try:
    print(num1 + num2)
    print("No se ha producido un error")
#se ejecuta solo si es un TypeError
except TypeError:
    print("Se ha producido un TypeError")
#se ejecuta solo si es un  ValueError
except ValueError:
    print("Se ha producido un ValueError")

print("\n")

#captura de la informacion de la excepcion
try:
    print(num1 + num2)
    print("No se ha producido un error")
except TypeError as e:
    print(e)#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#captura excepciones genericas
except Exception as e:
    print(e)

print("\n")

