"""
En este ejemplo se muestra como realizar busquedas y reemplazar. Para reemplazos simples
se usa replace, pero para reemplazos de patrones se usa sub() del modulo re, como podria
ser buscar todos los patromes de fechas(busqueda del patron) y reemplazarlas con un
nuevo formato
"""


text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2', text)
#\3 se refiere al grupo 3 y asi suscesivamente en donde se requiera posicionar

#tambien se puede compilar si se van a realizar sustituciones repetidas

patron = re.compile(r'(\d+)/(\d+)/(\d+)')
#devuelve una cadena con los reemplazos realizados
text2 = patron.sub(r'\3-\1-\2', text)

print(text)
print(text2)

"""
Para reemplazos mas complicados en donde se pueda reemplazar la fecha con el nombre
del mes
"""
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

#OJO aqui se le paso el patron resultante por medio de una funcion
text3 = patron.sub(change_date, text)
print(text3) #Today is 27 Nov 2012. PyCon starts 13 Mar 2013.

"""
Para saber cuantas sustituciones fueron realizadas ademas de obtener la
cadena sustituida resultante se usa re.subn()
"""
txtsustituido, n = patron.subn(r'\3-\1-\2', text)
print(txtsustituido, n) #Today is 2012-11-27. PyCon starts 2013-3-13. 2


