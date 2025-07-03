list_nums = []
print("¿How many elements do you want?")
wanted_elements = int(input("Add the number of element you want: "))
i = 0

while i < wanted_elements:
    print("Write the element number",i + 1)
    element = input("Add any name or number: ")
    print(element)
    list_nums.append(element)
    i += 1

list_nums.sort()
print(list_nums)