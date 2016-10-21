"""
Para hacer una reduccion (sum(), min(), max()) de elementos filtrados, una de las
formas en la que se puede hacer es como sigue
"""
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(sum(n for n in numeros if n > 5))


import os
archivos = os.listdir('C:\Ejercicios Python')

#si cualquiera de los archivos en la ruta tiene extensoion .py
if any(name.endswith('.py') for name in archivos):
    print("debe ser python!")
else:
    print("No es python")

s = ('ACME', 50, 123.45)

"""
Print(",".join(s))
este codigo marca error debido a que hay enteros que no se pueden unir como cadena
por lo tanto se presenta la siguiente opcion
"""

print(','.join(str(x) for x in s))


"""
En una estructura como un diccionario
"""
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},]

#ojo es una lista de diccionarios, si fuera un diccionario se deberia usar items() para iterar
#toma en cuenta que devuelve un generador, no es necesario convertir a tupla o lista
#y la coversioin tiene un costo de tiempo
print(min(s['shares'] for s in portfolio))

#otra manera de hacerlo
print(min(portfolio,key=lambda k: k['shares'])) #{'name': 'AOL', 'shares': 20}
