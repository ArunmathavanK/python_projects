import random

def play():
    while True:
        user=int(input("Enter ur choice: 0 for Rock 1 for paper 2 for scissor."))
        if user>2 or user<0:
            print("You entered invalid number. You lose.")
        else:
            computer = random.randint(0, 2)
            print("Computer choose:")
            print(computer)
            if user == computer:
                print("It's a Draw.")
            elif computer == 0 and user == 2:
                print("You lose.")
            elif user == 0 and computer == 2:
                print("You win.")
            elif computer > user:
                print("You lose.")
            elif user > computer:
                print("You win.")
        again=input("If u want to play again (y/n):").lower()
        if again!='y':
            print("Thanks for playing..")
            break
play()
