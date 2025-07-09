nums = [2, 11, 7, 15]
suma = 9
dicc = {}

for i , valor in enumerate(nums):
    suma_objetivo = suma - valor
    if suma_objetivo in dicc:
        print("Los indices donde se encuentra la suma son:",dicc[suma_objetivo],"y",i)
    dicc[valor] = i