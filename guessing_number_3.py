import random

tries = 0
random_number = random.randint(1,100)
findout = False

while not findout:
    tries += 1
    guessing_number = int(input("Add any number from 1 to 100: "))

    if guessing_number == random_number:
        findout == True
        print("Congrats you guessed the number")
        break
    elif guessing_number > random_number:
        print("It´s an smaller number")
    elif guessing_number < random_number:
        print("It´s a bigger number")
    