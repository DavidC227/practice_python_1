
numer_list = [2,3,4,2,6,7,3,2]

counter = { }

for number in numer_list:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

    print(counter)

max_key = max(counter, key=counter.get)
max_value = max(counter.values())

print(f"El numero {max_key} se repite {max_value} veces")  

