print("\n***Funciones de orden superior***\n")

#Funciones dentro de otra funcion
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

#usamos una variable f_sum donde las funciones pueden ser llamadas
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5 , 2, sum_one))
print(sum_two_values_and_add_value(5 , 2, sum_five))

print("\n***Clousers***\n")

def sum_ten(original_value):
    def add (value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)   
print(add_closure(5))

#concatenar funciones
print((sum_ten(5)(1)))

print("\n***Built-in higher Order Funtions***\n")

from functools import reduce

numbers = [2 , 5, 10, 21, 3, 30]

#Map
def multiply_two(number):
    return number * 2

#con funciones de orden superior
print(list(map(multiply_two, numbers)))#[4, 10, 20, 42]

#con lambda
print(list(map(lambda number : number * 2 , numbers)))#[4, 10, 20, 42]

#filter
def filter_greater_ten(number):
    if number > 10:
        return True
    return False

#con funciones de orden superior
print(list(filter(filter_greater_ten, numbers)))#[21, 30]

#con lambda
print(list(filter(lambda number : number > 10, numbers)))#[21, 30]

#Reduce
def sum_two_values(first_value,second_value):
    return first_value + second_value

#con funciones de orden superior
print(reduce(sum_two_values, numbers))#71


print("\n")