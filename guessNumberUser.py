import random

def guess():
    print("Keep in mind a number between 1 and 20 and the computer will try to guess ???")
    low = 1
    high = 21
    count = 0
    decleration = ""
    while decleration !="c":
        count +=1
        guess = random.randint(low, high)
        print(f"The computer's guess is {guess} ?")
        decleration = input("If guess is low, Enter 'L', If guess is high, Enter 'H', If guess is correct, Enter 'C': ")
        if decleration.lower() == "l":
            low = guess +1
        elif decleration.lower() == "h":
            high = guess -1
        elif decleration.lower() == "c":
            print(f"{guess} number that's correct number was found in {count}. guess")
            break
guess()