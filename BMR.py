print('BMR CALCULATOR FOR Revised Harris-Benedict Equation Method')
gender = input('Are you male ?(y/n);')
age = int(input('Age; '))
height = float(input('Height in cm; '))
weight = float(input('Weight in kg; '))
if gender == 'y':
    Man = True
else:
    Man = False

if Man == True:
    bmr = 88.362 + (13.397* weight) + (4.799 * height) - (5.677 * age)
else:
    bmr = 447.593 + (9.247* weight) + (3.098 * height) - (4.330 * age)

bmr = round(bmr)
print(bmr)
