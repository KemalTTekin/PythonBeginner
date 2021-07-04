def lcm(x,y):
# finding greater because LCM must be greater than or equal
    if x > y:
        greater = x
    else:
        greater = y
# getting loop find the number can divide x,y
    while True:
        if greater % x == 0 and greater % y == 0:
            lc = greater
            break
        greater +=1
    return lc
def gcf(x,y):
   if x > y:
       lower = y
   else:
        lower = x
   for i in range(1, lower+1):
        if x % i == 0 and y % i == 0:
                gcf = i
   return gcf
# Taking inputs
number1 = int(input('; '))
number2 = int(input('; '))
# Sending to function
print('Least Common Multiple ----> {}\nGreatest Common Factor ----> {}'.format(lcm(number1,number2),gcf(number1,number2)))

