
"""
En este ejemplo se realizan operaciones para buscar el max y min de los valores en un
diccionario. la funcion Zip se usa para poder realizar la busqueda por el valor del diccionario
no por la clave, lo hace intercambiando la "posicion" en donde originalmente es
clave, valor, este lo intercambia con valor, clave ya que si se hace una busqueda del minimo
en el diccionario realiza la busqueda por la clave no por el valor.

Tambien cabe destacar de los metodos de un diccionario dict.keys() y dict.values()
"""

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

#El resultado es el minimo lexicograficamente de las claves
mini = min(prices)
print(mini)

#El resultado es el menor valor, tambien se podria poner unicamente prece.values()
#pero no devolveria el valor de la clave
min_price = min(zip(prices.values(),prices.keys()))

print (min_price)

#tambien se puede ordenar por el precio de la misma manera
prices_sorted = sorted(zip(prices.values(), prices.keys()))

for key, value in prices_sorted:
    print(key, value)
"""
Cuando se hagan estos calculos con zip crea un iterador que solo puede consumirse una vez

Este codigo provocaria un error

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

"""
#Otra manera de realizar las operaciones de min y max
#pero solo devuelven uno de dos el valor o la clave
print("Minimo: ",min(prices, key=lambda k: prices[k]))

print("Minimo: ", prices[min(prices, key=lambda k: prices[k])])
