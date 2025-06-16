import random
random_num = random.randint(1,100)

tries = 0

while True:
    guessing_num = int(input("Add any number from 1 to 100, you have 5 shots: "))
    tries +=1 
    if tries == 5:
        print(f"It´s not the # {guessing_num}, Thanks for try it, this was your last chance, the missing number was {random_num}")
        break
    elif guessing_num == random_num:
        print(f"Congrats you found the missing numer {random_num}!! with {tries} attempts")
        break
    elif guessing_num > random_num:
        print(f"It´s not the # {guessing_num}, You need an smaller number,this is your attempt # {tries}, you have {5 - tries} attempts left")
    elif guessing_num < random_num:
        print(f"It´s not the # {guessing_num}, You need an bigger number,this is your attempt # {tries}, you have {5 - tries} attempts left")