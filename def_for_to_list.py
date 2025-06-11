def lista_for(start,end):
    list_1 = [i for i in range(start,end +1 )]
    return list_1


start = int(input("Ingresa el primer numero de la lista: "))
end = int(input("Ingresa el ultimo numero de la lista: "))

print(lista_for(start,end))