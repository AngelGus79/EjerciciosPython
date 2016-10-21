"""
Lista de comprehension, sirven para filtrar secuencias usando un criterio
"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([i for i in mylist if i > 0])

#a veces el criterio no es tan sencillo y se puede expresar con la funcion filter


values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def es_entero(numero):
    if numero.isdigit():
        return True
    else:
        return False

#valida cada elemento del arreglo y evalua
print(list(filter(es_entero, values)))



#Se puede transformar la informacion al mismo tiempo con la lista de comprension
from math import sqrt

print([sqrt(i) for i in mylist if i > 0])

#Otra forma de filtrar es reemplazando valores que no cumplan el criterio
#(ojo no es una instruccion if normal ya que en el else estableces el valor que devuelve
#en vez de solo descartar para esto
#se cambia el criterio de ubicacion


print([i if i > 0 else 0 for i in mylist]) #si i es mayor que 0 deja el numero sino pon 0


#Tambien se puede evaluar una expresion y devolver falso o verdadero
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

masDe5 = [n>5 for n in counts] #[False, False, True, False, False, True, True, False]

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]


from itertools import compress

print(list(compress(addresses, masDe5)))
#la clave fue crear una secuencia de bolleanos para poder elegir cual valor
#seleccionaria desde la lista. No importa si no coincide el numero de true o false
#con la lista que se va a seleccionar. compress y filter normalmente devuelven un iterador
#por lo tanto se usa list para convertirlo a lista


