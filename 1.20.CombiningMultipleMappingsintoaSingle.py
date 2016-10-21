"""
En este ejercicio se muestra como unir diccionarios con el metdo ChainMap del modulo
collections.

c = ChainMap(a,b) en donde a y b son dos diccionarios. c mantiene una lista de referencias
de los elementos y se puede ejecutar sobre c las operaciones de un diccionario.

Pero si se quiere modificar un valor solo se modificara la del primer diccionario si se
intenta actualizar algun elemento del 2do diccionario (b) enviara error.

IMPORTANTE: las siguientes funciones realizan la union de diccionarios por la clave
si tienen claves iguales con diferentes valores se pierde el 2do diccioinario
"""


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap

c = ChainMap(a,b)
print(c) #ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(c['x']) #  1 ( tomado de a)
print(c['y']) #  2 ( tomado de b)
print(c['z']) #  3 ( tomado de a)

print(list(c.keys())) #['x', 'y', 'z'] si hay duplicados toma los del diccionario a
c['x'] = 20
print(c) #ChainMap({'x': 20, 'z': 3}, {'y': 2, 'z': 4})
del c['x']
print(c) #ChainMap({'z': 3}, {'y': 2, 'z': 4})

"""
del c['y']
esta instruccion manda error debido a que solo realiza los metodos en el primer dict osea a

Tambien se puede usar ChainMap para usar como estructura jerarquica
"""

valores= ChainMap()
valores['x'] = 1
valores = valores.new_child()
valores['x'] = 2
valores = valores.new_child()
valores['x'] = 3

print(valores) #ChainMap({'x': 3}, {'x': 2}, {'x': 1})

#para acceder a los valores anidados

print(valores['x']) #3

valores = valores.parents

print(valores['x']) #2

valores = valores.parents

print(valores['x']) #1


"""
Otra manera de hacer estas operaciones es usar la usar el metodo update de un diccioinario
Pero este metodo devuelve un nuevo diccionario, no afecta a los originales, y si los
diccioinarios cambian no se reflejaran los cambios

"""

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = dict(b)
c.update(a)

print(c) #{'x': 1, 'y': 2, 'z': 3}








