import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator():
    n1=int(input("Enter the first no:"))
    print("+\n-\n*\n/")
    continue_pgm=True
    while continue_pgm:
        op=input("Pick the operator:")
        n2=int(input("Enter the second no:"))
        if op=='+':
            ans=add(n1,n2)
            print(f"{n1} + {n2} = {ans}")
        elif op=='-':
            ans=sub(n1,n2)
            print(f"{n1} - {n2} = {ans}")
        elif op=='*':
            ans=mul(n1,n2)
            print(f"{n1} * {n2} = {ans}")
        elif op=='/':
                ans=div(n1,n2)
                print(f"{n1} / {n2} = {ans}")
        else:
            print("Invalid Operator u entered.")
        play=input(f"Enter 'y' to continue with {ans} or 'n' to start a new calculation or 'x' to exit.").lower()
        if play=='y':
            n1=ans
        elif play=='n':
            continue_pgm=False
            os.system('cls')
            calculator()
        else:
            continue_pgm=False
            print("End")
calculator()