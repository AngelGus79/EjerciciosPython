"""
En este ejercicio se realizan busquedas de lo que puedan tener en comun dos diccionarios
values o keys o items que consiste en el par value y key. para esto se realizan operaciones de conjuntos (set) comunies 
"""
a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

print(a.keys() & b.keys()) #interseccion { 'x', 'y' }

print(a.items() & b.items()) # { ('y', 2) }

print(a.keys() - b.keys()) # { 'z' }

#en este ejemplo se muestra como seleccionar especificos en un diccionario
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c) # {'y': 2, 'x': 1}
