"""
tambien existen diccionarios de comprension

"""
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

subconjunto = {key:value for key, value in prices.items() if value >38}

#Diferencias de cuando devuelve un diccionario
#1.- Las llaves {}
#2.- key:value
#3.- es posible poner en el for key, value
#4.- se usa el metodo items()

print(subconjunto)

#Comparando dos diccionarios
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
subconjunto2 = {key:value for key, value in prices.items() if key in tech_names }

print(subconjunto2)



"""
otras formas de hacer los mismo pero con menor rendimiento
"""

#Mucho de lo creado en los diccionarios de compresioin tambien puede llevarse a cabo
#mediante tuplas, pero el diccionario de comprension es un poco mas rapido (aprox. 2 veces
#mas rapido sobre todo en este ejemplo de prices)

s1 = dict((key,value) for key, value in prices.items() if value > 38)
print(s1)

#otra manera de escribir lo mismo seria, pero esta solucion es 1.6 veces mas lenta que la primera

s2 = {key:prices[key] for key in prices.keys() & tech_names}
print(s2)
