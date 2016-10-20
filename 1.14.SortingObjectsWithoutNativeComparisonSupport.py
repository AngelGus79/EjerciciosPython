"""
En este ejercicio realizamos la ordenacion de una lista de clase generica
mediante un atributo obviamente publico seleccionado
"""
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'Us:({})'.format(self.user_id)
        #al imprimir la clase usuario imprime lo que viene en el metodo __repr__
        #con el format indicado

users = [User(23), User(3), User(99)]

for u in users:
    print(u)

from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

#Tambien se puede usar oeraciones lambda pero attrgetter es un poco mas rapido
#u es el elemento dentro de la lista en este caso es una clase
print(sorted(users, key=lambda u: (u.user_id)))

#tambien es aplicable con minimos y maximos
print(min(users, key=attrgetter('user_id')))
