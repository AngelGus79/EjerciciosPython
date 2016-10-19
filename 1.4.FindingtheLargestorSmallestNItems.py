#devuelve los n numeros mas grandes o mas pequeños
import heapq

l= [-1,-3,10,1,3,70,200,24]

print(heapq.nlargest(3,l))
print(heapq.nsmallest(3,l))

#Tambien tiene un parametro key que permite realizar selecciones rn rdytucturas mas complejas

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

barato = heapq.nsmallest(3,portfolio,key=lambda s: s['price'])
caro = heapq.nlargest(3,portfolio,key=lambda s:s['price'])


print(barato) #devuelve un diccionario con los 3  mas baratos y sus demas elementos
print(caro)


#cuando el tamaño de la lista es muy grande en comparacion con la busqueda que se requiere
#encontrar de los numeros mas grandes y mas pequeños, este modulo tiene una manera de
#mejorar el rendimiento

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

#paso 1 se vuelve lista, debe hacerse obligatoriamente
h = list(nums)
#En este paso lo ordena de una manera conveniente para poder realizar busquedas de manera
#mas veloz
#heapq.heappop() method, which pops off the first item and replaces it with the next smallest item (an operation that
#requires O(log N) operations where N is the size of the heap)
heapq.heapify(h)
print(h)

heapq.heappop(h) #devuelve el menor y lo elimina
heapq.heappop(h) #devuelve el 2do menor
heapq.heappop(h)
print(h)
#ojo.. esto es solo para encontrar varios numeros mayores o menores si se requiere
#encontrar solo el mayor o el menor max() y min() es mas rapido
