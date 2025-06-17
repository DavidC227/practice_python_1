def num_vowels(word):

    counter = 0
    for i in word:
        if i in "aeiou":
            counter += 1
    return counter

word = input("Add any word: ")
print(f"The word {word} has {num_vowels(word)} vowels")