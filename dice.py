import random

while True:
        input("Press enter to roll the dice")
        dice = random.randint(1,6)
        print(f"you got the number: {dice}")

        again = print("do you want to roll the dice again? s/n?")
        if again.lower() != "s":
                print("see you")
                break