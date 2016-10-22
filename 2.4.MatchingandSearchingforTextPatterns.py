"""
Si se quiere realizar busquedas por una literal simple se puede hacer con
startwith() o endswith() o con find() que devuelve el indice de la primer coincidencia
pero para casos mas complicados se pueden usar expresiones regulares con el metodo
match del modulo re
"""

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

print(bool(re.match(r'\d+/\d+/\d+', text1))) #True
print(bool(re.match(r'\d+/\d+/\d+', text2))) #False

#si se van a ejecutar muchas busquedas de coincidencias usando el mismo patron,
#se suele precompilar un patron de expresion regular en un objeto

patron = re.compile(r'\d+/\d+/\d+')

print(bool(patron.match(text1))) #Yes
print(bool(patron.match(text2))) #False

#match() siempre trata de encontrar el patron al inicio de la cadena. Si se requiere
#buscar en toda la cadena se usa findall() este no devuelve un boleano sino
#una lista de las coincidencias

text = 'Hoy es 11/27/2012. PyCon comienza 3/13/2013.'

print(patron.findall(text))

"""
cuando se definen expresiones regulares comunmente se escriben las partes entre parentesis
para que posteriormente puedan ser llamadas ejemplo
"""
patron = re.compile(r'(\d+)/(\d+)/(\d+)')

m = patron.match('11/27/2012')

print(m.group(0)) #'11/27/2012'
print(m.group(1)) #'11'
print(m.group(2)) #'27'
print(m.group(3)) #'2012'

mes, dia, ano = m.groups()

print(mes, dia, ano)


#Ahora usando el mismo patron pero con el metodo findall
print(patron.findall(text)) #[('11', '27', '2012'), ('3', '13', '2013')]

for mes, dia, ano in patron.findall(text):
    print('{}-{}-{}'.format(ano, mes, dia))
    #Ojo asi se da formato a la salida

#Si se requieren buscar coincidencias iterativamente se usa finditer() en vez de findall()

for m in patron.finditer(text):
    print(m.groups())


#Ojo match() busca coincidencia al principio de la cadena en caso por lo que
#buscar coincidencia en 12/12/12 regresa True al igual que 12/12/12asdsdsd
# en caso de querer una busqueda exacta excribir al final en el patro $

patron = re.compile(r'(\d+)/(\d+)/(\d+)$')

#Recordar que tambien se puede omitir el patron, este se usa cuando se van a realizar
#varias busquedas
re.findall(r'(\d+)/(\d+)/(\d+)', text)

