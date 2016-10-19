#se desea implementar una cola que ordene los elementos por una priorodad dada y siempre regrese el elemento
#que tenga la proioridad mas alta en cada operacion pop
import heapq

class colaPriorizada:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, prioridad):
        heapq.heappush(self._queue,(-prioridad, self._index, item))
#se pone prioridad negativa porque busca el menor, el orden de agregacion y el elemento
#para que cuando caiga un elemento con la misma prioridad regrese el primero ingresado
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class elemento:
    def __init__(self, name):
        self.name = name
    def __repr__(self): #regresa un string con un formato determinado
        return 'Item({!r})'.format(self.name)

q = colaPriorizada()
q.push(elemento('foo'), 1)
q.push(elemento('bar'), 5)
q.push(elemento('spam'), 4)
q.push(elemento('grok'), 1)



p = q.pop()
print(p)

p = q.pop()
print(p)

p = q.pop()
print(p)

p = q.pop()
print(p)

#trabajando con tuplas priorizadas, solo basta con anexar a la tupla un numero para poder
#realizar comparaciones entre ellas, sin el numero manda error

a = (1,"programar en hackerranck")
b = (2,"Realizar actividades")
c =(1,"leer el libro de python")
d = (2, "aprender las demas herramientas")


if a > b:
    print(a, "es mas importante")
else:
    print(b, "es mas importante")


#ahora si agregamos el index, el que indica que el orden de llegada
a = (1, 0, "tarea1")
b = (5, 1, "tarea2")
c = (1, 2, "tarea3")
print(a < b)

print(a<c) #en este caso en el que la prioridad es la misma, toma el index menor





