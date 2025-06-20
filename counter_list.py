from collections import Counter

nums = [3, 5, 7, 3, 9, 3, 5, 2, 3, 10]

list_num = int(input("Add any number in the list"))

print("Original list:",nums)
print("Organized list:",sorted(nums))
print("Organized list vice versa:",sorted(nums,reverse=True))
print("Total nums of the list:",len(nums))
print("Number:",list_num,"is repeated",nums.count(list_num),"times")
print("repeated numbers total list:",Counter(nums))