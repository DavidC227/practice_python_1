
import random
missig_number = random.randint(1,10)
tries = 1

while tries < 4:
    tries += 1

    guessed_number = int(input("\nFind the missing, add number from 1 to 10: "))

    if tries == 4:
        print(f"\nThanks for try it, the missing number was {missig_number}")
    elif guessed_number != missig_number:
        print("\ntry again")
    elif guessed_number == missig_number:
        print(f"\nCongrats you find the missing number {missig_number}, here your reward\n")
        break
    
