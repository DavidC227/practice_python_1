def detec_anagram(word_1,word_2):
    if sorted(word_1.lower().replace(" ","")) == sorted(word_2.lower().replace(" ","")):
        return True
    else:
        return False
    
random_word_1 = "Roma" #input("Write any word or phrase")
random_word_2 = "Amor" #input("Write any word or phrase again")

print(detec_anagram (random_word_1,random_word_2))