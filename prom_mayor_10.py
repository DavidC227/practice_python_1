lista_num = [0,5,10,15,3,25,18,7,12,11,9]

suma = 0
contador = 0

for i in lista_num:
    if i > 10:
        suma += i
        contador += 1 

if contador > 0:       
    print("El promedio de los numeros mayores a 10 de la lista es:",suma / contador)
else:
    print("No hay numeros mayores a 10")
        

