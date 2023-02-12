import random

# S> P, R > S, P > R

def is_win(player, computer):
    if (player.lower() == 'r' and computer == 's') or (player.lower() == 's' and computer == 'p') or (
            player.lower() == 'p' and computer == 'r'):
        return True
    else:
        return False


def rps(x):
    pc_count = 0
    your_count = 0
    mylist = ['r', 's', 'p']

    while pc_count != x and your_count != x:
        pc = random.choice(mylist)
        user = input("Enter 'R' for Rock,  Enter 'P' for Paper, Enter 'S' for Scissors: ")
        print(f"The Computer's choise is: {pc} ")

        if user.lower() == pc:
            print("Scoreless!")

        elif is_win(user, pc):
            your_count += 1
            print("You win!")

        else:
            pc_count += 1
            print("The Computer win!")

        print(f"You: {your_count}, The Computer: {pc_count} ")


rps(3)
