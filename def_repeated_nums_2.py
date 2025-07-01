def dubpl_nums(lists):
    
    sawn_nums = set()
    for i in lists:
        if i in sawn_nums:
            return True
        sawn_nums.add(i)
    return False

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 2, 5]

print(dubpl_nums(list_1))
print(dubpl_nums(list_2))