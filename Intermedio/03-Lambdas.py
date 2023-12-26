print("\n***Lambdas***\n")

#palabra reservada + valor/es + : + lógica de la lambda
sum_two_values = lambda first_value, second_value : first_value + second_value
print(sum_two_values(3,4))

multiply_values = lambda first_value, second_value : first_value * second_value
print(multiply_values(3,2))

#Lambda dentro de una funcion
def sum_three_values(value):
    return lambda first_value, second_value : first_value + second_value + value
print(sum_three_values(5)(2,4))

print("\n")