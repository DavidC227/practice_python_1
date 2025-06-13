list_nums = [4, 7, 10, 3, 5, 2, 8, 11, 6]

count_even = 0
count_odd = 0

for i in list_nums:
    if i % 2 == 0:
        count_even += 1
    elif i % 2 != 0:
        count_odd += 1
print(f"The total amount of even numers are {count_even} and the odd numbers are {count_odd}")