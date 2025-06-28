def repeated_list(lists):
    counter = {}
    
    for i in lists:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    
    max_value = max(counter.values())

    if max_value > 1:
        return False
    else:
        return True

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 2, 5]

print(repeated_list(list_1))
print(repeated_list(list_2))