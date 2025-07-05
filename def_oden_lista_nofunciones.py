def lista_ordenada(datos):
    cantidad = len(datos)
    i = 0
    print("Datos antes de ordenar",datos)
    print("Cantidad de datos: ",len(datos))
    for i in range(cantidad - 1):
        for i in range(cantidad -1):
            if datos[i] > datos[i+1]:
                x = datos[i]
                datos[i] = datos[i+1]
                datos[i+1] = x
    return datos

datos = [60, 44, 11, 55, 66, 22]
print(lista_ordenada(datos))