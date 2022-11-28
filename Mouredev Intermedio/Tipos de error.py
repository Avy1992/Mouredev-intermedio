### Types of error ###

"""Todas las excepciones de python"""

# Syntax Error
# print "Hola mundo"  # falta de parentesis, de puntuacion, etc. No compila
print("Hola mundo")


# Name Error
# print(name)  # hacer referencia a una variable no declarada
name = 'Adrian'
print(name)


# Index Error
languages = ['python', 'java', 'kotlin', 'c#']
# print(languages[8]) # indice fuera de rango o no valido


# Module not found error
# import maths  # Modulo no existe
import math


# Attribute error
# print(math.PI)  # el modulo no contiene ese atributo
print(math.pi)


# Key error
my_dict = {'Name': 'Adrian', 'Country': 'Spain', 'Language': 'Python'}
# print(my_dict['name'])  # key no definida en el diccionario
print(my_dict['Name'])


# Type Error
# print(languages['0'])  # Espera un tipo de dato diferente (los indices como int y no string)
print(languages[0])


# Import error
# from math import PI  # lo que quieres importar del modulo no existe
from math import pi


# Value error
edad = int('30')
#edad2 = int('30 años')   # No puede convertir el string a entero porque contiene letras


# Zero divisiuon error
#num = 14/0  # Division por cero