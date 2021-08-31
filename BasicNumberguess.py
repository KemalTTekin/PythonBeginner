import random

computer = random.randint(1,500)
guess = 10
print("Guess Number 1-500 you have 10 chance ")
while True:

    user = int(input("Your Guess; "))
    if user == computer:
        print("You Found computer guess",computer)
    elif user < computer:
        guess-= 1
        print("Please choose a higher number ")
    elif user > computer:
        guess -= 1
        print("Please choose a lower number ")

