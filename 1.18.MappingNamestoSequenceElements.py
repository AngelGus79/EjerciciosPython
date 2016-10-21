"""
Este ejemplo muestra como nombrar los indices de las tuplas.
Esto se hace por medio del metodo namedtuple() del modulo collections
"""

from collections import namedtuple

#esta es una instancia de la clase namedtuple
suscritor = namedtuple('suscritor',['email','telefono'])

s = suscritor('email@algo.com','0123456789')

print(s)
print(s.email)
print(s.telefono)

#esto puede reemplazar el uso de diccionarios los cuales consumen mucho espacio
#tambien se puede desempacar normalmente a comose haria con indices

email, tel = s
print(email, tel)

#ojo al ser tuplas no se puede insertar mas datos, pero se puede actualizar alguno

"""
este error marca error por tratar de modificar una tupla
s.email = 'hola@mundo.com'
"""
#Hay una manera de hacer cambios usando el metodo _replace() de un ainstancia namedtuple

s = s._replace(email='hola@mundo.com')

print(s)
"""
En este ejemplo se muetra como convertir un diccionario en un stock
"""

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
#Crea una instancia prototipo
stock_prototype = Stock('', 0, 0.0, None, None)
# Funcion que convierte un diccionario a n stock
def dict_to_stock(s):
    return stock_prototype._replace(**s) #**ss mapea los atributos del diccionario a las tuplas
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}

diccionario_A_stock = dict_to_stock(a)
print(diccionario_A_stock)
#Si se requiere usar una estructura de ddatos que se requiera hacer modificaciones
#en varios atributos usar namedtuple no es la mejor manera. En vez de esto considerese
#usar __slots_ viene en la receta 8.4


