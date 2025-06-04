print()
lista_numeros = []


for i in range (5):
    i += 1
    numero = int(input("Ingresa cualquier numero: "))
    lista_numeros.append(numero)
print()
print(lista_numeros)
print()
mayor = max(lista_numeros)
print()
print(f"El numero mayor de la lista de 5 numeros es: {mayor}")
print()