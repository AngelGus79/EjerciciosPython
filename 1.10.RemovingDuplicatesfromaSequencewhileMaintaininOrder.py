"""
En este ejemplo se muestra como eliminar duplicados mientras se manteniendo
el orden del resto de los elementos.
Esto ya es posible hacerlo usando set, pero el detalle con esto es que:
1.-No se puede hacer en elementos genericos
2.-No queda ningun tipo de orden en los elementos. Con orden se refiere al orden en
el que fueron ingresados

"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a))) #[1, 5, 2, 9, 10] con el orden se refiere a orden de insercion

print(set(a)) #{1, 2, 10, 5, 9} directamente no guarda ningun tipo de orden

"""
si se intentan guardar duplicados en un tipo unhashable como los diccionarios. Esta funcion
tambien puede servir para datos genericos

key es para programar funciones lambda
"""

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item  #se devuelve el diccionario que es unhashed
            seen.add(val) 
            


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
#[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
