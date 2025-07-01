from collections import Counter

caracteres = input("ingresa una palabra o frase: ")

caracteres = caracteres.lower().replace(" ","")

count = Counter(caracteres)

print(count)

llave, valor = count.most_common(1)[0]

print(f"{llave}:{valor}")