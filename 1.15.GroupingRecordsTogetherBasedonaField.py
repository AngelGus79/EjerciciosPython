def funcion(i):
    for n in range(i):
        yield n


s = funcion(5)
#devuelve un generator que si lo quiero imprimir solo me manda su direccion en memoria
for i in s:
    print(i)

"""
El siguiente ejemplo muestra como agrupar registros por un elemento dado
primero se ordenara la lista y posteriormente se agrupara

ojo hasta el momento se ha estado trabajando con una lista de diccionarios
"""


rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

"""
Es importante ordenar antes de agrupar ya que solo agrupa los campos iguales consecutivas
"""

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('---------->',i)
