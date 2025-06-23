phrase = input("Add any frase with many repeated words")

phrase = phrase.lower().split()

counter = {}

for i in phrase:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
for i, times in counter.items():
    print(f"{i}:{times}")
