x = 0
addition = 0

while True:
    number = input("Add any number or 'end' to fnish: ").lower()

    if number == "end":
        print("End of the summatory")
        break
    else:
        number = float(number)
        x += 1
        addition += number
        print(x,".-",number,"+",addition-number,"=",addition)
