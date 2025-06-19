list_nums = [4, 7, 10, 3, 8, 5, 6]
pair_count = 0

for i in list_nums:
    if i % 2 == 0:
        pair_count += 1

print(f"The total amount of pair numbers: {pair_count}")