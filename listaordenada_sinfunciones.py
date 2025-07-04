datos = [60, 44, 11, 55, 66, 22]
print("Lista desordenada",datos)
cantidad = len(datos)
i = 0

for i in range(cantidad -1):       #rango(5) (0 al 4) el ciclo solo necesita 5 vueltas por el tema de los pares vecinos.
    for i in range(cantidad -1):
        if datos[i] > datos[i+1]:
            x = datos[i]           # x = al primer elemento,                      x = 60
            datos[i] = datos[i+1]  # el primer elemento igul al segundo elemento, datos[i] = 44
            datos[i+1]= x          #  el segundo elemento igual ala variable x,   datos[i+1] = 60
print("Lista ordenada",datos)