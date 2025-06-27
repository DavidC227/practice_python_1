list = [6,7,4,9,5,10,11,1,12,13,2,16,15,3,14]
print(f"The formal list is: ", sorted(list))
n = len(list)  + 1

sum_arithmetic_sequence = (n * (n + 1)) // 2
sum_list_no_ordered = sum(list)

absence_num = sum_arithmetic_sequence - sum_list_no_ordered

print(f"The absence number is: {absence_num}")