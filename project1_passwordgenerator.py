import random

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
         'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
print("Welcome to Password Generator")
n_numbers=int(input("How many numbers you want in password:\n"))
n_symbols=int(input("How many symbols you want in password:\n"))
n_letters=int(input("How many letters you want in password:\n"))
password=[]
for i in range(0,n_numbers):
    a=random.choice(numbers)
    password+=a
for i in range(0,n_symbols):
    a=random.choice(symbols)
    password+=a
for i in range(0,n_letters):
    a=random.choice(letters)
    password+=a
random.shuffle(password)
print(password)
str=""
for o in password:
    str+=o
print(str)