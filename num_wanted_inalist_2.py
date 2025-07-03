
def elementos_definidos_lista():
    print("Cuantos elementos quieres en la lista?")
    num_elementos = int(input("Agregar numero de elementos deseados"))
    print(num_elementos)

    lista_nums = []
    i = 0

    while i < num_elementos:
        print("Agrega el elemento deseado numero",i+1)
        elemento_deseado = input("Agrega el elemeto deseado")
        print(elemento_deseado)
        lista_nums.append(elemento_deseado)
        i += 1
    lista_nums.sort()
    print(lista_nums)

elementos_definidos_lista()