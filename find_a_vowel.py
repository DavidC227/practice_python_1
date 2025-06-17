word = input("Add any word: ")
counter = 0

for i in word:
    if i in "aeiou":
        counter += 1

print(f"The word {word} has {counter} vowels")