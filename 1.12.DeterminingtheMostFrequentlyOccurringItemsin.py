"""
Se pretende encontrar los valores mas frecuentes, para esto se importa lafuncion Counter
del modulo collections
"""
from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

palabrasAContar = Counter(words)
print(palabrasAContar)
#Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "you're": 1, 'under': 1, "don't": 1, 'not': 1})
#Agrupa todas las palabras

#imprime las 3 mas comunes o las que tienen mas frecuencia
print(palabrasAContar.most_common(3))
#[('eyes', 8), ('the', 5), ('look', 4)]

#Se puede modificar la cantidad de los items
palabrasAContar['eyes'] += 1
print(palabrasAContar)

morewords = ['why','are','you','not','looking','in','my','eyes']
wc = Counter(morewords)


"""
el parametro dentro de la funcion update es una lista.
lo que hace esta funcion es unir lo que ya tiene con la nueva lista y
realizar el recuento
"""
palabrasAContar.update(morewords)

print(palabrasAContar)

"""
tambien se puede unir 2 Counter o restar
"""
a = Counter(words)
b = Counter(morewords)

c = a + b

print(c)

c = a - b

print(c)
#se puede usar para realizar busquedas como en los diccionarios
print(min(zip(a.values(),a.keys())))





