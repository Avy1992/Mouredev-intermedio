### Python Package Manager ###

# PIP
# https://pypi.org/ para descargar dependecias y modulos
# py -m pip install libreria    >>>para instalar libreria
# py -m pip list    >>>para ver las librerias instaladas
# py -m pip uninstall libreria     >>>para desinstalar libreria

"""Si no reconoce la libreria aunque este instalada,comprobar si estas en un entorno
virtual y añadir lospaquetes alinterprete manualentedesde Settings>project>interpreter>+"""

import numpy
print(numpy.version.version)
numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array*2)

import pandas

import requests

# My New Package
from MyNewPackage import Arithmetics
print(Arithmetics.sum(3,15))