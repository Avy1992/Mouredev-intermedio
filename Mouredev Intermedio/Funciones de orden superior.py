### Funciones de orden superior ###
"""Son funciones que pueden ejecutar otras funciones entradas como parametro
de la función"""
import functools


def sum_one(value):
    return value+1

def sum_two_values(first_val, second_val, fsum_one):
    return fsum_one(first_val+second_val)

#print(sum_two_values(5, 12, sum_one))


### Closures  ###
"""Funcion que define una funcion y que devuelve una funcion, que despues puedes
almacenarla en una variable etc"""
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(1)(5))


###Built-in higher order functions ###

numbers = [2, 3, 5, 21, 3, 32, 15]

# Map

def multiply_by2(number):
    return number*2

print(list(map(multiply_by2, numbers)))
print(list(map(lambda number: number*2, numbers)))


# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number>10, numbers)))


# Reduce

def sum_two_values(value1, value2):
    print(value1)
    print(value2)
    return value1 + value2

print(functools.reduce(sum_two_values, numbers))  # redude opera con el valor acual y el acumulado, esta en el modulo functools