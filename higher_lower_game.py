import random
import design
import datas
def display_details(ac):
    name=ac['name']
    category=ac['category']
    country=ac['country']
    return f" {name}, a {category} from {country}."
score=0
print(design.high)
print(f"You are right. Your score is {score}")
def check(guess,follow1,follow2):
    if follow1<follow2:
        if guess==1:
            return False
        else:
            return True
            # return follow2
    else:
        if guess==1:
            return True
            # return follow1
        else:
            return False
ac1=random.choice(datas.data)
# ac2=random.choice(datas.data)
# def again():
#     if follow2>follow1:
#         ac1=ac2
gameover=True
while True:
    # ac1 = random.choice(datas.data)
    ac2 = random.choice(datas.data)
    while ac1==ac2:
        ac2 = random.choice(datas.data)
    print(f'compare 1: {display_details(ac1)}')
    print(design.vs)
    print(f"compare 2: {display_details(ac2)}")
    guess=int(input("Who has more Followers? Type 1 or Type 2: "))
    follow1=ac1['followers']
    follow2=ac2['followers']
    correct=check(guess,follow1,follow2)
    if correct==True:
        score+=1
        print(f"You are right. Your score is {score}.")
        if follow2>follow1:
            ac1=ac2
    else:
        print(f"You are wrong. Your final score is {score}.")
        gameover=False
        break
print("Game Over")