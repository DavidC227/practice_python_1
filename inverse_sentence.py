def inverse_sentence(sentence):
    
    inverse = sentence[::-1]
    return inverse

sentence = (input("Add any sentence: ").lower())
print(f"The inverse sentence of {sentence} is {inverse_sentence(sentence)}")