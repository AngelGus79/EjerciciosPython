"""
Procesamiento de cadenas. Una funcion mas flexible que el metodo split para la division
de cadenas, es el split del modulo re para realizar divisiones con multiples delimitadores
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*', line)) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
#acepta punto y coma (;) coma (,) espacios en blanco (\s) seguidos por cualquier cantidad
#de espacios en blanco \s*

"""
Otro ejemplo de procesamiento de texto
"""
#una de las diferencias mas destacadas entre esta exp. regular y la anterior son los
#parentesis en vez de corchetes
campos = re.split(r'(;|,|\s)\s*', line) 
print(campos) #['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

valores = campos[::2] #se obtienen los elementos en posicion par de la lista

print(valores) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

#Ahora para obtener los delimitadores
delimitadores = campos[1::2] #desde el indice 1 de 2 en 2
print(delimitadores) # [' ', ';', ',', ',', ',']

#si quiero agregar un delimitador mas a la lista

delimitadores += ['']

print(delimitadores)

#Para volver a juntar la cadena OJOO se forman pares del elemento en el indice 0 de
#valores con el elemento en el indice 0 en los delimitadores y asi suscesivamente

Unido = ''.join(v+d for v,d in zip(valores, delimitadores))

print(Unido) #'asdf fjdk; afed, fjek,asdf, foo'



#EJERCICIOS


s = 'palabra1 palabra2; palabra3'

print(s.split()[::2])

sep = re.split(r'(,|;|\s)\s*', s)
print(sep)
val = sep[::2]
print(val)
deli = sep[1::2] + [" "]
print(deli)
union = ''.join(v+d for v,d in zip(val,deli))
print(union)







