d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}

d['a'].append(1)

print(d)
#{'a': [1, 2, 3, 1], 'b': [4, 5]}
#defaultdict inicializa un diccionario para que se comporte como list o set
#es todo lo que hace, de lo contrario se tendria que escribir por cada clave o key
# algo asi dict[clave] = [], cuando con defaultdict seria en una sola instruccion
# se especifica que todas las claves se manejaran como listas


from collections import defaultdict

#Esta seria la forma normal
"""
d = {}
for key, value in pairs:
if key not in d:
d[key] = []
d[key].append(value)
"""
#Esta seria la forma con defaultdict
"""
d = defaultdict(list)
for key, value in pairs:
d[key].append(value)
"""

#Otra manera de inicializar pero al momento de agregar es la funcion setdefault( como se
#muestra a continuacion, es un poco antinatural por que se hace una nueva instancia
#en cada llamada con la lista vacia[]

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)


#ejecrcicios

#forma convencional de usar diccionarios

dic = {}
dic['numeros']= [1,2,3]
dic['vocales']=['a','e','i']
dic['consonantes'] = ['b','c','d']

dic['numeros'].append(4)
# dic['simbolos'].append('%') esta linea manda error porque no he inicializado con lista esa clave
print(dic)



dic = defaultdict(list)

dic['numeros']= [1,2,3]
dic['vocales']=['a','e','i']
dic['consonantes'] = ['b','c','d']
dic['numeros'].append(4)
dic['simbolos'].append('%') #ya no manda error porque ya ha sido inicializado

print(dic)

#otra forma de inicializar usando setdefault
dic = {}

dic.setdefault('numeros',[]).append(1)
dic.setdefault('numeros',[]).append(2)
dic.setdefault('numeros',[]).append(3)
dic.setdefault('numeros',[]).append(4)

print(dic)





