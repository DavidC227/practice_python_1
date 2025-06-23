integer_num = input("Add any integer number with more than 2 digits")

sum = 0

for i in integer_num:
    sum += int(i)

print(f"The total addition of the digists of the number {integer_num} is {sum}")