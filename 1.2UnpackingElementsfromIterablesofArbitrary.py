datos = ['Angel', 'Gustavo', '3454333',10,9.9,10, '2 Semestre']

#Sabiendo que a partir de la entrada 4 vienen las calificaciones hasta la
#penultima entrada pero sin saber cuantas calificaciones vienen, se puede
#recuperar de la siguiente manera

nombre1, nombre2, tel, *calif, grado = datos

print(sum(calif)/len(calif))

#forma de recorrer arreglo de tutplas
registros = [("ingreso", 12000, 23000),
             ("egreso", 2300, 3400, 500),
             ("ingreso", 12500, 25600),
             ("egreso", 120, 2300)]

ingresoTotal = 0
egresoTotal = 0
for transaccion, *cantidad in registros:
    if transaccion == "ingreso":
        ingresoTotal += sum(cantidad)
    else:
        egresoTotal += sum(cantidad)
print("Ganancia: ", ingresoTotal - egresoTotal)

#Otra manera de desempacar

cadena = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

nombre,*otros, homedir, sh = cadena.split(':')

print(homedir)

    
