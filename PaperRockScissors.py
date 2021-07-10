import random
A = {
    1:"Rock",
    2:"Scissors",
    3:"Paper"
}
c = 0
u = 0
while True:

    choose = random.randint(1,3)
    computer = A[choose]
    print("------------------------\nComputer; {} User; {}\n------------------------".format(c,u))
    user = A[int(input("1-Rock 2-Scissors 3-Paper\n;"))]
    print("Computer Choose {}".format(computer))
    if user == "Rock" and computer != "Paper":
        print("User Won")
        u +=1

    elif user == "Scissors" and computer !="Rock":
        print("User Won")
        u +=1

    elif user == "Paper" and computer != "Scissors":
        print("User Won")
        u +=1
    else:
        print("Computer Won")
        c +=1

    #   Rock > Scissors > Paper > Rock







