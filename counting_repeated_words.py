from collections import Counter

phrase = "El carro rojo esta en el garage rojo de el centro de el carro"
phrase = phrase.lower()
split_words = phrase.split()
print(split_words)

counting_words = Counter(split_words)
print(counting_words)