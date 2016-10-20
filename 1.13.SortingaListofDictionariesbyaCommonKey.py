"""
En este ejercicio se muestra como ordenar una lista de diccionarios por alguno de sus
valores. esto se hace con la funcion itemgetter del modulo operator
"""

from operator import itemgetter

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

porNombre = sorted(rows, key=itemgetter('fname'))

for i in porNombre:
    print(i)

"""
la salida esta ordenada por el nombre
{'uid': 1004, 'lname': 'Jones', 'fname': 'Big'}
{'uid': 1003, 'lname': 'Jones', 'fname': 'Brian'}
{'uid': 1002, 'lname': 'Beazley', 'fname': 'David'}
{'uid': 1001, 'lname': 'Cleese', 'fname': 'John'}
"""

#itemgetter tambien puede admitir varios valores

PorNombreyApellido = sorted(rows,key=itemgetter('fname','lname'))

print('-'*20)
for i in PorNombreyApellido:
    print(i)

#otra manera de hacerlo en con las funciones lambda sin embargo usando
#itemgetter es un poco mas rapido

s = sorted(rows, key=lambda k: (k['fname'], k['lname']))
print(20*'-')
for i in s:
    print(i)
#tambien puede ser aplicado a las fucniones min y max
print(20*'-' + 'minimo')
minimo = min(rows,key=itemgetter('fname'))
print(minimo)
print(20*'-' + 'maximo')
maximo = max(rows,key=itemgetter('fname'))
print(maximo)



