from collections import deque

#breve ejemplo de yield. Es parecido a un return pero este te devuelve un iterable.

def eyield(n):
    while n >= 0:
        yield n
        n -= 1

#devuelve un objeto generador,  que se tendria que recorrer
c = eyield(5)
for i in c:
    print(i)

#para transformarlo a lista
c = list(eyield(5))
print(c)


#Un deque es un objeto que tiene funciones de pila y cola tiene funciones para
#agregar/eliminar por la izquierda o derecha etc.
#en este ejemplo se buscan lineas con ciertos patrones y un maximo de historial
#Al establecerle el maxlen=2 al deque, solo guarda los ultimos 2 datos iterados


def buscar(lineas, patron, historial):
    lineas_anteriores = deque(maxlen=historial)
    for l in lineas:
        if patron in l:
            yield l, lineas_anteriores
        lineas_anteriores.append(l)

lineas = ['Linea12', 'Linea23', 'Linea34', 'Linea41', 'Linea51', 'Linea61','Linea61' ]

c = buscar(lineas, "1", 2)

for l, p in c:
    print(l,p)

#Otro ejemplo pero leyengd archivos

if __name__ == '__main__': #Si el modulo que estas ejecutando es el modulo principal?
    with open('prueba.txt') as f:
        for linea, lineaPrevia in buscar(f, '1', 4):
            for pline in lineaPrevia:
                print(pline, end='')
            print(linea, end='')
            print('-'*20)


#formas de crear dequeue
q =deque(maxlen=2) #se restringe que solo pueda contener 2 elementos
q.append(1) #agrega a la derecha si no se especifica un maxlen no tendra ninguna restriccion
q.append(2)
q.append(3)

print(q)

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)

print(d)

d.pop()
d.popleft()
print(d)




            
