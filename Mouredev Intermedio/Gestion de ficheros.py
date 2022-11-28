### Gestion de ficheros ###

import os

# Fichero .txt
file = open('myFile.txt', 'w+')
file.write("Mi nombre es Adrian\nMi apellido es Vargas\nTengo 30 anos\nProgramo en Python")
#print(file.read(10))  #escribe los 10 primeros caracteres
#print(file.readlines())  #hace una lista de todas las lineas del  archivo
for line in file.readlines():
    print(line[0:-1])
file.write("\nPero tambien he tocado JavaScript")
file.close()
#os.remove('myFile.txt')


# Fichero .json
import json

json_file = open('myFile.json', 'w+')
json_test = {
    "name": 'Adrian',
    "country": "Spain",
    "language": "Python",
    "example": "https://jason.org"}
json.dump(json_test, json_file, indent=4)
