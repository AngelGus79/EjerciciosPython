"""
En este ejemplo se muestra como buscar coincidencias usando el patron del shell de unix
o windows con las funciones fnmatch() y fnmatchcase()

"""
from fnmatch import fnmatch, fnmatchcase


print(fnmatch('archivo.txt','*.txt')) #True por que archivo.txt se ajusta


#Un uso interesate es el siguiente

import os

lista = os.listdir('.') #devuelve una lista de los archivos de la ubicacion actual

a = [nombre for nombre in lista if fnmatch(nombre,'*.txt')]

print(a)

"""
Este metodo se ajusta a las reglas de mayuscula y minuscula del sistema de archivos
subyacente, osea en caso de ejecutarse sobre windows y linux sera diferente ya que
en windows no hay diferencia entre mayusculas y minusculas. Para evitar esto
existe la funcion fnmatchcase que respeta mayusculas y minisculas
"""

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

print([v for v in addresses if fnmatchcase(v,'* ST')])
