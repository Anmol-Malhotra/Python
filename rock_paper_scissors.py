from numpy import random
print("------#ROCK, PAPER, SCISSORS GAME#------")
print("")
your_points = 0
computer_points = 0
def select():
    print("")
    print("Select the desired option:\n1. ROCK\n2. PAPER\n3. SCISSORS\n0. Exit")
while True:
    select()
    choice = int(input("Enter your choice number: "))
    if choice == 0:
        print("---Game Summary---")
        print("Your points are:",your_points)
        print("Computer points are: ", computer_points)
        if your_points > computer_points:
            print("Congratularions!! You won😃...")
        elif computer_points > your_points:
            print("Better luck next time😒")
        else:
            print("It's a tie.")
        print("Exiting the program...")
        break
    match choice:
        case 1:
            print("Your choice: ROCK")
            choice = "ROCK"
        case 2:
            print("Your choice: PAPER")
            choice = "PAPER"
        case 3:
            print("Your choice: SCISSOR")
            choice = "SCISSORS"
        case _:
            print("Invalid choice")
            continue
    x = random.choice(["ROCK", "PAPER", "SCISSORS"])
    print("Computer's choice:",x)
    if (choice == x):
        print("It's a tie.")
    elif (choice == "ROCK" and x == "SCISSORS") or (choice == "PAPER" and x == "ROCK") or (choice == "SCISSORS" and x == "PAPER"):
        print("You Won.")
        your_points += 1
    else:
        print("Computer Won")
        computer_points += 1