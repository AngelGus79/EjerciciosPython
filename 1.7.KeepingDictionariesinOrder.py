"""
OrderedDict es una funcion que mantiene el orden de los elementos a como se van ingresando
se importa del modulo collections.
Un OrderedDict mantiene una lista doble ligada para mantener el orden, por lo que un OrderedDict
tendra un tamaño de mas del doble que un diccionario convencional
"""

from collections import OrderedDict

d=OrderedDict()
d['clave1'] = 2
d['clave2'] = 1
d['clave3'] = 4
d['clave4'] = 5

for clave in d:
    print(clave,d[clave])

