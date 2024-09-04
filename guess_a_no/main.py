import random
import logo

easy=10
hard=5
def dificulty_lvl(lvl):
    if lvl == 'easy':
        return easy
    else:
        return hard
def check(user_guess,ans,attempt):
    # while attempt-1!=0:
        if user_guess < ans:
            print("Your guess is too low")
            return attempt-1
        # print(f"You have {attempt-1} attempts remaining to guess the number.")
        elif user_guess>ans:
            print("Your guess is too high.")
            return attempt-1
        # print(f"You have {attempt-1} attempts remaining to guess the number.")
        else:
            print(f"Your guess is right....The answer is {ans}")
            # break
def play():
    print(logo.logo)
    print("Let me think of a number between 1 to 50.")
    ans=random.randint(1,50)
    # print(ans)
    lvl=input("Choose level of difficulty....Type 'easy' or 'hard'.").lower()
    attempt=dificulty_lvl(lvl)
    user_guess=0
    while user_guess!=ans:
            print(f"You have {attempt} remaining to guess the number!")
            user_guess=int(input("Make a Guess:"))
            attempt=check(user_guess,ans,attempt)
            if attempt==0:
                print("You are out of guesses.  You lose..... Better luck next time.....")
                # return
                break
            elif user_guess!=ans:
                print("Guess again")
play()
