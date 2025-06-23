phrase = "El carro rojo esta en el garage rojo de el centro de el carro"
print(phrase)
phrase = phrase.lower().split()
print(phrase)

count = {}

for i in phrase:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
print(count)

for i, times in count.items():
    print(f"{i}:{times}")