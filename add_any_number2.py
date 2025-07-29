x = 0
summatory = 0

while True:
    number = input("add any number or 'end' to finish the summatory: ").lower()
    if number == "end":
        print("the summatory is over")
        break

    else:
        try:
            number = float(number)
            x += 1
            summatory += number
            print(x,".-",number,"+",summatory -number,"=",summatory)
        except:
            print("You can only add a number or 'end' to finish the summatory")  