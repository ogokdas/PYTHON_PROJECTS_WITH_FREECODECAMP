import random


def guess():
    random_number = random.randint(1, 21)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input("Enter an integer number between 1 and 20: "))
        except:
            print("Sorry! You entered not an integer number.")
            continue

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congrat! {random_number} is the correct number.")
guess()