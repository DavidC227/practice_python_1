import random
random_num = random.randint(1,10)

tries = 0

while tries < 3:
    tries += 1
    guessed_number = int(input("Add any int number from 1 -10"))

    if tries == 3:
        print(f"Thanks for try it, you have {3 - tries} left, the missing number was {random_num}")
    elif guessed_number != random_num:
        print(f"Try again, you still have {3 -tries} shots")
    elif guessed_number == random_num:
        print(f"Congrats!!!! you find the missing number {random_num}")
        break