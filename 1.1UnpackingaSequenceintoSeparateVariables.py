#tupla
p = (4,5)
x, y = p
print(x)
print(y)

#Lista
arreglo = ['h', 'o', 'l', 'a', 1,(17,10,2016)]
a,b,c,d,r,fecha = arreglo
print(fecha)
print(fecha[0])

#Tupla dentro de lista
a,b,c,d,r,(dia, mes, ano) = arreglo
print("mes: " + str(mes))

#Si no coincide el numero de variables con el numero de iterables manda error

#aqui un ejemplo con cadena, puede ser cualquier iterable
a,s,d,f = "hola"

print(a)

_,s,d,f = "hola"
