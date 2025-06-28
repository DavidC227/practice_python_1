lista_anidada = [1, 2, [3, 4], 5, [6], 7]
addition = 0
for i in lista_anidada:
    if isinstance(i, list):
        addition += sum(i)
    else:
        addition += i

print(addition)