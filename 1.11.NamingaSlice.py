"""
En este ejemplo se nombra la porcion de la cadena a utilizar
"""
numero = '123456768901234567689112345676890123456768901234567689012345676890123456768901234567689012345676890123456768901234567689012345676890123456768901234567689012345676890123456768901234567689012345676890123456768901234567689012345676890123456768901234567689012345676890'

costo = int(numero[20:24]) * float(numero[40:48])

print(costo)
#En vez de hacer esto se puede establecer un nombre al rango

ventas = slice(20,24)#fijate que no esta asociado aqui a ninguna cadena por que solo indica un rango
precio = slice(40,48)

print (int(numero[ventas]) * float(numero[precio]))

#Ojo el rango es el nombrado, esto es para darle legibilidad al codigo

"""
los parametros de la funcion slice hacen los siguiente

(a,b,c)
a = indice de inicio, se puede. Con la propiedad start se puede ver su valor
b = la posicion a donde quieres que llegue le restas 1. Con la propiedad stop se puede ver su valor
c = indica por ejemplo si solo se quiere que tome los caracteres de 2 en 2 o 3 en 3 etc
Con la propiedad step se puede ver su valor

(start, stop, step)
"""
s = 'HelloWorld'
#solo quiero tomar de World las palabras en posicion par osea W r d
rango = slice(5,10,2)

print(rango.start)
print(rango.stop)
print(rango.step)

print(rango.indices(len(s))) #(5,5,2)


for i in range(*rango.indices(len(s))):
    print(s[i])

#con el * la informacion que arroja informacion separada por comas si le quito el * regresa una tupla
