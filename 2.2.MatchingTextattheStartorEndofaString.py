"""
Una manera de checar extensiones o principios de una cadena como para validar si es una
url son los metodos str.startswith() o str.endswith() que devuelven valor booleano
"""

url = "http://holamundo.com"

print(url.startswith('http://')) #True
#en caso de ser muchos parametros se debe poner solamente en TUPLA 
print(url.endswith(('.com','.net','.org'))) #True 

import os

archivos = os.listdir() #devuelve una lista de los nombres de los archivos en la ubicacion actual

l = [nombre for nombre in archivos if nombre.endswith(('.txt','.py'))]
print(l) #devuelve la lista de los archivos que terminan en .py y .txt

#El parametro de any es un generador de booleanos o un listado de boleanos
#[True,True, False...] que se forma a partir de preguntar a cada nombre de archivo
#si termina en .py. Y si cualquiera (any)  es verdadero devuelve verdadero

print(any(nombre.endswith('.py') for nombre in archivos))


"""
Otro ejemplo usando url

esta funcion devuleve el contenido de la pagina pero antes preguna si es una http,
https o ftp
"""
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

print(read_data("http://www.google.com"))

"""
Esta tarea tambien se puede realizar con slices o con re.match(), sin embargo con
startswith() y endswith() es mas rapido
"""

url  = 'http://www.google.com'

if url[:5] == 'http:' or url[:6]:
    print(True)

import re

print(re.match('http:|https:|ftp:',url)) #<_sre.SRE_Match object; span=(0, 5), match='http:'>





