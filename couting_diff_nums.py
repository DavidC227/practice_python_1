num_list = [5, -3, 0, 9, -1, 0, 7, -4, 0, 2]
positive_count = 0
negative_count = 0
zero_count = 0

for i in num_list:
    if i == 0:
        zero_count += 1
    elif i < 0:
        negative_count += 1
    else:
        positive_count += 1
        
print(f"Total 0s: {zero_count}, total negatives: {negative_count} and total positives: {positive_count}")