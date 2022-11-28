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
    "languages": ["Python", "JavaScript", "C++"],
    "example": "https://jason.org"}
json.dump(json_test, json_file, indent=2 )
json_file.close()
with open('myFile.json', 'r') as my_other_file:
    for line in my_other_file.readlines():
        print(line[0:-1])
json_dict = json.load(open('myFile.json'))  # Carga un diccionariode un fichero json a una variable
print(json_dict)
print(type(json_dict))


# .csv file
import csv

csv_file = open('myFile.csv', 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(json_dict.keys())
csv_writer.writerow(json_dict.values())
csv_file.close()


# .xlsx file
#import xlrd #Modulo externo, se debe instalar a parte


# .xml file
import xml