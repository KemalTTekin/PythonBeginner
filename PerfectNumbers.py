from functools import reduce
number = int(input("Number; "))

divisors = list(filter(lambda x : number % x == 0,range(1,number) ))

total = reduce(lambda a,b: a+b,divisors)

if total == number:
        print("Perfect Number ✓ ")
else:
        print("Regular Number ")
