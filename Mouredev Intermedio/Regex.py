### Regular expressions ###

import re

my_string = "Esta es la leccion numero 7: Leccion Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: manejo de ficheros"

# match

match = re.match("Esta es la leccion", my_string, re.I)
#print(match)
span = match.span()
start, end = span
#print(my_string[start:end])
#print(match)
#print(re.match("Esta es la leccion", my_other_string))
#print(re.match("Expresiones Regulares", my_string))
#No hay match porque no COMIENZA por ese string, aunque lo contenga

match2 = re.match("Esta no es la leccion", my_other_string)
#print(match2)
if match2 is not None:
    start, end = match2.span()
   # print(my_other_string[start:end])


# search
"""encuentra el primer match de la RE en el string"""
search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall
"""encuentra todos los match de la RE en el string y los devuelve en una lista"""
findall = re.findall("leccion", my_string, re.I)
print(findall)


# split
"""Devuelve una lista con el string original troceado por el substring que 
queramos, eliminandolo"""
print(re.split(":", my_string))


# sub
"""sustituye el primer substring por el segundo en el string que queramos y
devuelve el nuevo string"""
sub = re.sub(": ", "\n", my_string)
print(sub)


# Patterns

pattern = r'[l|L]eccion'
print(re.findall(pattern, my_string))

pattern = r'[l|L]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r'[\D]'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# email validation with regex
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$'
    print(re.findall(pattern,email))
is_valid_email('adri23458@gmail')