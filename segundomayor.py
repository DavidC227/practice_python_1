num_list_1 =[10, 20, 4, 45, 99]  
print("Antes de ordenar",num_list_1)
num_list_2 = [5, 5, 5] 

length = len(num_list_1)

i = 0

for i in range(length -1):
    for i in range(length -1):
        if num_list_1[i] > num_list_1[i+1]:
            x = num_list_1[i]
            num_list_1[i] = num_list_1[i+1]
            num_list_1[i+1] = x
print("Despues de ordenar",num_list_1)
print("Imprimir el segundo mayo: ",num_list_1[length -2])