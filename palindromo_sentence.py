random_sentence = input("Add any sentence you want")
random_sentence_low_no_space = (random_sentence.lower()).replace(" ","")
inverse_sentence = random_sentence_low_no_space[::-1]


if random_sentence_low_no_space == inverse_sentence:
    print(f"The sentence: {random_sentence} is a palindromo due to it can be read from left to right and vice versa, look at it: {inverse_sentence}")
else:
    print(f"The sentence: {random_sentence} isnt a palindromo because it cant be read equal from right to left, look at it: {inverse_sentence}")