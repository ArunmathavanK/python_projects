import game
# questions=[
#     {"text":"Who is known as God of Cricket?"},{"text":"Who is GOAT of Football?"},
#     {"text":"What does RAM stands _________ "},{"text":"Which is the capital of India"},
#     {"text":"Who is the CM of Tamilnadu?"}
# ]
# answers=["A","C","B","A","D"]
# options=[["A.Sachin Tendulkar","B.Virat Kholi","C.MS Dhoni","D.Yuvraj Singh"],
#          ["A.Cristiano Ronaldo","B.Neymar JR","C.Lional Messi","D.Pele"],
#          ["A.Read Access Memory","B.Random Access Memory","C.Read Only Memory","D.Random Only Memory"],
#          ["A.Delhi","B.Chennai","C.Mumbai","D.Kolkata"],["A.Seeman","B.Vijay","C.RN Ravi","D.Stalin"]]
print("**************************************")
print("\nWelcome to My quiz game...")
# print("**************************************")
score=0
qo_no=0
for i in range(len(game.questions)):
    print("\n*************************************\n")
    print(game.questions[i]["text"])
    for j in game.options[qo_no]:
        print(j)
    guess=input("Enter your answers(A/B/C/D):").upper()
    if guess== game.answers[qo_no]:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
        print(f"The correct answer is {game.answers[qo_no]}.")
    qo_no+=1
    print(f"Your score is:{score}/{qo_no}")
print(f"The final score is {score}")
