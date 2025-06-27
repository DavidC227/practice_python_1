phrase_word = input("Add any phrase or word")

phrase_word_1 = phrase_word.lower().replace(" ","")
phrase_word_2 = phrase_word.lower().replace(" ","")

if phrase_word_1 == phrase_word_2[::-1]:
    print(f"Yes {phrase_word} is a palindromo due to it can be read from right to left: {phrase_word_2[::-1]}")
else:
    print(f"No {phrase_word} is not a palindromo due to it can´t be read from right to left: {phrase_word_2[::-1]}")