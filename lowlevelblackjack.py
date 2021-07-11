import random


while True:
    card1 = random.randint(1,20)
    card2 = random.randint(1,20)
    print("{}  {}\n"
          "__  __  ".format(card1,card2))
    if card1 + card2 == 21:
        print("You Won 21\n")
    elif card1+card2 > 21:
        print("You lost greater than 21\n")
    else:

        userchoose = input("Add+/-Stay ;")
        if userchoose == "+":
            card3 = random.randint(1,20)
            print("{}  {}  {}\n"
                  "__  __  __".format(card1, card2,card3))
            if card1+card2+card3 > 21:
                print("You Lost\n")
            elif card1 + card2 + card3 == 21:
                print("You Won")
            else:
                comp = random.randint(10,21)
                print("Computer ;",comp)
                if comp >= card1+card2+card3:
                        print("Computer WOn\n")
                else:
                    print("You Won\n")
        elif userchoose == "-":
            comp = random.randint(10, 21)
            print("Computer ;", comp)
            if comp > card1 + card2 :
                print("Computer WOn\n")
            else:
                print("You Won")
