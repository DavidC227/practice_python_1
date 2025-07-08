from collections import Counter

string = "abacabad"

counter = Counter(string)

for i in string:
    if counter[i] == 1 :
        print(i)
        break
else:
    print(None)